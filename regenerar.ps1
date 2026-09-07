$ServerInstance = "localhost"
$Database       = "HVT_HOSVITAL"
$Username       = "Superset"
$Password       = "Superset"
$OutputDir      = "C:\Users\sopor\Documents\ProyectosBI\superset-docs\docs\diccionario-general"

Write-Host "Iniciando regeneracion de diccionario..." -ForegroundColor Cyan

# Asegurar y limpiar archivos viejos para evitar lecturas de cache
if (Test-Path $OutputDir) {
    Get-ChildItem -Path $OutputDir -Filter "*.md" | Where-Object { $_.Name -ne "index.md" } | Remove-Item -Force
} else {
    New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
}

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
    CASE WHEN c.is_nullable = 1 THEN 'SI' ELSE 'NO' END AS IS_NULLABLE,
    CASE WHEN pk.column_id IS NOT NULL THEN 'PK' ELSE '' END AS IS_PK,
    ISNULL(CAST(ep.value AS NVARCHAR(MAX)), '') AS COLUMN_DESCRIPTION
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

$Connection = New-Object System.Data.SqlClient.SqlConnection($ConnectionString)
$DataTable = New-Object System.Data.DataTable

try {
    $Connection.Open()
    $Command = New-Object System.Data.SqlClient.SqlCommand($SqlQuery, $Connection)
    $Adapter = New-Object System.Data.SqlClient.SqlDataAdapter($Command)
    [void]$Adapter.Fill($DataTable)
    $Connection.Close()
}
catch {
    Write-Host "Error de conexion: $_" -ForegroundColor Red
    exit
}

$DictHosvital = @{
    'MPNFAC'      = 'Numero consecutivo de factura / cuenta de cobro'
    'MATIPDOC'    = 'Tipo de documento de identificacion del paciente'
    'MPTDOC'      = 'Numero de documento / identificacion del paciente'
    'HISTORIAPAC' = 'Numero de historia clinica del paciente'
    'GLONUM'      = 'Numero consecutivo de radicacion de glosa'
    'GLOITEM'     = 'Item o renglon glosado dentro de la factura'
    'GLOEDO'      = 'Estado normativo / ciclo de vida de la glosa'
    'GLOVLR'      = 'Valor economico objetado / glosado'
    'GLOVLRLEV'   = 'Valor economico levantado a favor de IPS'
    'GLOVLRACE'   = 'Valor economico aceptado por IPS'
    'GLSCOD'      = 'Codigo de motivo de glosa'
    'PRNCON'      = 'Codigo interno de producto / CUPS en MAEPRO'
    'PRNCON1'     = 'Codigo de homologacion CUPS / CUM'
    'PRNOMB'      = 'Descripcion del procedimiento o servicio'
    'MAECOD'      = 'Codigo de aseguradora / EPS'
    'MAENOM'      = 'Razon social de aseguradora'
    'FECING'      = 'Fecha y hora de ingreso'
    'FECEGR'      = 'Fecha y hora de egreso'
    'CODSER'      = 'Codigo del servicio hospitalario'
    'NOMSER'      = 'Nombre del servicio'
    'CODCAM'      = 'Codigo de cama'
    'ESTCAM'      = 'Estado operativo de la cama'
    'USUREG'      = 'Usuario que registro'
    'FECREG'      = 'Fecha de registro'
}

$Tables = $DataTable | Group-Object -Property TABLE_NAME

foreach ($Table in $Tables) {
    $TName   = $Table.Name
    $RawType = $Table.Group[0]['OBJECT_TYPE'].ToString()
    $ObjType = if ($RawType -eq 'USER_TABLE') { 'Tabla Transaccional' } else { 'Vista SQL' }

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add("# " + $TName)
    $lines.Add("")
    $lines.Add("**Tipo de Objeto:** " + $ObjType + "  ")
    $lines.Add("**Base de Datos:** \`HVT_HOSVITAL\`  ")
    $lines.Add("**Esquema:** \`dbo\`")
    $lines.Add("")
    $lines.Add("---")
    $lines.Add("")
    $lines.Add("## Estructura de Campos")
    $lines.Add("")
    $lines.Add("| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |")
    $lines.Add("| :-: | :--- | :--- | :-: | :--- |")

    foreach ($Row in $Table.Group) {
        $pkIcon = if ($Row['IS_PK'].ToString() -eq 'PK') { "🔑" } else { "" }
        $col    = $Row['COLUMN_NAME'].ToString()
        $tipo   = $Row['DATA_TYPE_FULL'].ToString()
        $nul    = $Row['IS_NULLABLE'].ToString()
        $desc   = $Row['COLUMN_DESCRIPTION'].ToString().Trim()

        if ([string]::IsNullOrWhiteSpace($desc)) {
            $colUpper = $col.ToUpper()
            if ($DictHosvital.ContainsKey($colUpper)) {
                $desc = $DictHosvital[$colUpper]
            } else {
                $desc = "Campo transaccional de " + $TName
            }
        }

        $rowMd = "| " + $pkIcon + " | **\`" + $col + "\`** | \`" + $tipo + "\` | " + $nul + " | " + $desc + " |"
        $lines.Add($rowMd)
    }

    $outPath = Join-Path $OutputDir ($TName + ".md")
    [System.IO.File]::WriteAllLines($outPath, $lines, [System.Text.Encoding]::UTF8)
}

Write-Host "Completado: $($Tables.Count) fichas tecnicas regeneradas correctamente." -ForegroundColor Green
