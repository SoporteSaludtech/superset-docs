SET NOCOUNT ON;
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
