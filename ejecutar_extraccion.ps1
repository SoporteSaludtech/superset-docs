$ServerInstance = "localhost"
$Database       = "HVT_HOSVITAL"
$Username       = "Superset"
$Password       = "Superset"
$OutputDir      = "C:\Users\sopor\Documents\ProyectosBI\superset-docs\docs\diccionario-general"

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$ConnectionString = "Server=$ServerInstance;Database=$Database;User Id=$Username;Password=$Password;TrustServerCertificate=True;Connect Timeout=30;"

$SqlQuery = @"
SELECT 
    t.name AS TABLE_NAME,
    t.type_desc AS OBJECT_TYPE,
    c.name AS COLUMN_NAME,
    ty.name + 
    CASE 
        WHEN ty.name IN ('varchar', 'char', 'nvarchar', 'nchar') THEN '(' + CASE WHEN c.max_length = -1 THEN 'MAX' ELSE CAST(c.max_length AS VARCHAR) END + ')'
        WHEN ty.name IN ('decimal', 'numeric') THEN '(' + CAST(c.precision AS VARCHAR) + ',' + CAST(c.scale AS VARCHAR) + ')'
        ELSE ''
    END AS DATA_TYPE_FULL,
    CASE WHEN c.is_nullable = 1 THEN 'SÍ' ELSE 'NO' END AS IS_NULLABLE,
    CASE WHEN pk.column_id IS NOT NULL THEN 'PK' ELSE '' END AS IS_PK,
    ISNULL(CAST(ep.value AS NVARCHAR(MAX)), 'Sin descripción documentada') AS COLUMN_DESCRIPTION
FROM sys.objects t
JOIN sys.columns c ON t.object_id = c.object_id
JOIN sys.types ty ON c.user_type_id = ty.user_type_id
LEFT JOIN sys.extended_properties ep 
    ON ep.major_id = t.object_id AND ep.minor_id = c.column_id AND ep.name = 'MS_Description'
LEFT JOIN (
    SELECT ic.object_id, ic.column_id
    FROM sys.indexes i
    JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
    WHERE i.is_primary_key = 1
) pk ON pk.object_id = t.object_id AND pk.column_id = c.column_id
WHERE t.type IN ('U', 'V') AND t.is_ms_shipped = 0
ORDER BY t.name, c.column_id;
"@

$QueryFKs = @"
SELECT 
    tp.name AS ParentTable,
    cp.name AS ParentColumn,
    tr.name AS ReferencedTable,
    cr.name AS ReferencedColumn,
    fk.name AS ForeignKeyName
FROM sys.foreign_keys fk
JOIN sys.tables tp ON fk.parent_object_id = tp.object_id
JOIN sys.tables tr ON fk.referenced_object_id = tr.object_id
JOIN sys.foreign_key_columns fkc ON fk.object_id = fkc.constraint_object_id
JOIN sys.columns cp ON fkc.parent_object_id = cp.object_id AND fkc.parent_column_id = cp.column_id
JOIN sys.columns cr ON fkc.referenced_object_id = cr.object_id AND fkc.referenced_column_id = cr.column_id;
"@

$Connection = New-Object System.Data.SqlClient.SqlConnection($ConnectionString)
$DtCols = New-Object System.Data.DataTable
$DtFKs  = New-Object System.Data.DataTable

try {
    Write-Host "Conectando a HVT_HOSVITAL..." -ForegroundColor Yellow
    $Connection.Open()
    
    $CmdCols = New-Object System.Data.SqlClient.SqlCommand($SqlQuery, $Connection)
    $AdapterCols = New-Object System.Data.SqlClient.SqlDataAdapter($CmdCols)
    [void]$AdapterCols.Fill($DtCols)

    $CmdFKs = New-Object System.Data.SqlClient.SqlCommand($QueryFKs, $Connection)
    $AdapterFKs = New-Object System.Data.SqlClient.SqlDataAdapter($CmdFKs)
    [void]$AdapterFKs.Fill($DtFKs)

    $Connection.Close()
    Write-Host "Metadata extraída exitosamente." -ForegroundColor Green
}
catch {
    Write-Host "Error de conexión: $_" -ForegroundColor Red
    exit
}

$FkLookup = $DtFKs | Group-Object -Property ParentTable -AsHashTable
$Tables   = $DtCols | Group-Object -Property TABLE_NAME

foreach ($Table in $Tables) {
    $TableName = $Table.Name
    $ObjType   = if ($Table.Group[0].OBJECT_TYPE -eq "USER_TABLE") { "Tabla Transaccional" } else { "Vista SQL" }

    $Lines = [System.Collections.Generic.List[string]]::new()
    $Lines.Add("# $TableName")
    $Lines.Add("")
    $Lines.Add("**Tipo de Objeto:** $ObjType  ")
    $Lines.Add("**Base de Datos:** ``HVT_HOSVITAL``  ")
    $Lines.Add("**Esquema:** ``dbo``")
    $Lines.Add("")
    $Lines.Add("---")
    $Lines.Add("")
    $Lines.Add("## Estructura de Campos")
    $Lines.Add("")
    $Lines.Add("| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |")
    $Lines.Add("| :-: | :--- | :--- | :-: | :--- |")

    foreach ($Row in $Table.Group) {
        $pk   = if ($Row["IS_PK"] -eq "PK") { "🔑" } else { "" }
        $col  = $Row["COLUMN_NAME"]
        $tipo = $Row["DATA_TYPE_FULL"]
        $nul  = $Row["IS_NULLABLE"]
        $desc = $Row["COLUMN_DESCRIPTION"]
        $Lines.Add("| $pk | **``$col``** | ``$tipo`` | $nul | $desc |")
    }

    if ($FkLookup.ContainsKey($TableName)) {
        $Lines.Add("")
        $Lines.Add("---")
        $Lines.Add("")
        $Lines.Add("## Relaciones con Otras Tablas (Foreign Keys)")
        $Lines.Add("")
        $Lines.Add("| Columna Origen | Tabla Destino | Columna Destino | Nombre Constraint |")
        $Lines.Add("| :--- | :--- | :--- | :--- |")

        foreach ($Fk in $FkLookup[$TableName]) {
            $pCol   = $Fk["ParentColumn"]
            $rTab   = $Fk["ReferencedTable"]
            $rCol   = $Fk["ReferencedColumn"]
            $fkName = $Fk["ForeignKeyName"]
            $Lines.Add("| **``$pCol``** | [``$rTab``]($rTab.md) | ``$rCol`` | ``$fkName`` |")
        }
    }

    $FilePath = Join-Path $OutputDir "$TableName.md"
    [System.IO.File]::WriteAllLines($FilePath, $Lines, [System.Text.Encoding]::UTF8)
}

Write-Host "Completado: $($Tables.Count) fichas tecnicas generadas sin errores de interpolacion." -ForegroundColor Green
