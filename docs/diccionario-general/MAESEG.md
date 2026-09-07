# MAESEG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MSUser`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MSNomb`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSPass`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSCopy`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MStatus`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DepCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSValBas`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsVlrTop`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
