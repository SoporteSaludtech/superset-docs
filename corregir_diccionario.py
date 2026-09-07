import pyodbc
import os

output_dir = r"C:\Users\sopor\Documents\ProyectosBI\superset-docs\docs\diccionario-general"
os.makedirs(output_dir, exist_ok=True)

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=HVT_HOSVITAL;"
    "UID=Superset;"
    "PWD=Superset;"
    "TrustServerCertificate=yes;"
)

# Diccionario semantico de campos comunes en Hosvital HIS
DICCIONARIO_HOSVITAL = {
    'MPNFAC': 'Número consecutivo de factura / cuenta de cobro',
    'MATIPDOC': 'Tipo de documento de identificación del paciente',
    'MPTDOC': 'Número de documento / identificación del paciente',
    'HISTORIAPAC': 'Número de historia clínica del paciente',
    'GLONUM': 'Número consecutivo de radicación de glosa',
    'GLOITEM': 'Ítem o renglón glosado dentro de la factura',
    'GLOEDO': 'Estado normativo / ciclo de vida de la glosa',
    'GLOVLR': 'Valor económico objetado / glosado por la entidad pagadora',
    'GLOVLRLEV': 'Valor económico levantado / ratificado a favor de la IPS',
    'GLOVLRACE': 'Valor económico aceptado por la IPS (pérdida asumida)',
    'GLSCOD': 'Código normativo de motivo de glosa (MinSalud / EPS)',
    'PRNCON': 'Código interno de procedimiento o producto en MAEPRO',
    'PRNCON1': 'Código de homologación CUPS o CUM',
    'PRNOMB': 'Nombre o descripción del producto / procedimiento',
    'MAECOD': 'Código de la empresa administradora / EPS / EAPB',
    'MAENOM': 'Razón social de la aseguradora / pagador',
    'FECING': 'Fecha y hora de ingreso de la atención hospitalaria',
    'FECEGR': 'Fecha y hora de egreso o alta médica',
    'CODSER': 'Código del servicio o unidad funcional asistencial',
    'NOMSER': 'Nombre del servicio hospitalario',
    'CODCAM': 'Código o identificación física de la cama',
    'ESTCAM': 'Estado operativo de la cama (Ocupada, Libre, Desinfección)',
    'USUREG': 'Usuario del sistema que registró la transacción',
    'FECREG': 'Fecha y hora del registro transaccional en el sistema'
}

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
except Exception as e:
    print(f"Error conectando por ODBC: {e}")
    exit(1)

# 1. Consulta maestra de columnas
query_cols = """
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
"""

cursor.execute(query_cols)
rows = cursor.fetchall()

# 2. Foreign Keys
query_fks = """
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
"""
cursor.execute(query_fks)
fk_rows = cursor.fetchall()

fks_by_table = {}
for r in fk_rows:
    p = r[0]
    if p not in fks_by_table:
        fks_by_table[p] = []
    fks_by_table[p].append(r)

tables = {}
for r in rows:
    t_name = r[0]
    if t_name not in tables:
        tables[t_name] = {'type': r[1], 'cols': []}
    tables[t_name]['cols'].append(r)

for tbl_name, info in tables.items():
    obj_desc = "Tabla Transaccional" if info['type'] == "USER_TABLE" else "Vista SQL"
    lines = [
        f"# {tbl_name}\n",
        f"**Tipo de Objeto:** {obj_desc}  ",
        "**Base de Datos:** `HVT_HOSVITAL`  ",
        "**Esquema:** `dbo`\n",
        "---",
        "\n## Estructura de Campos\n",
        "| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |",
        "| :-: | :--- | :--- | :-: | :--- |"
    ]
    
    for c in info['cols']:
        pk_icon = "🔑" if c[5] == "PK" else ""
        col_name = c[2]
        data_type = c[3]
        nullable = c[4]
        desc = c[6].strip()
        
        if not desc:
            desc = DICCIONARIO_HOSVITAL.get(col_name.upper(), "Campo técnico del modelo transaccional Hosvital")

        lines.append(f"| {pk_icon} | **`{col_name}`** | `{data_type}` | {nullable} | {desc} |")

    if tbl_name in fks_by_table:
        lines.extend([
            "\n---",
            "\n## Relaciones con Otras Tablas (Foreign Keys)\n",
            "| Columna Origen | Tabla Destino | Columna Destino | Nombre Constraint |",
            "| :--- | :--- | :--- | :--- |"
        ])
        for fk in fks_by_table[tbl_name]:
            lines.append(f"| **`{fk[1]}`** | [`{fk[2]}`]({fk[2]}.md) | `{fk[3]}` | `{fk[4]}` |")

    file_path = os.path.join(output_dir, f"{tbl_name}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

cursor.close()
conn.close()
print(f"Diccionario regenerado con exito total para {len(tables)} tablas/vistas.")
