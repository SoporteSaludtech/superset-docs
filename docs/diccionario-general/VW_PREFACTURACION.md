# VW_PREFACTURACION

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`EMPRESA`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SEDE`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DOCUMENTO`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NUMERO_ORDEN`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FECHA_ORDEN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PROVEEDOR`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
