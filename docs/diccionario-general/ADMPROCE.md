# ADMPROCE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ProcesId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IdModulo`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MaeProPc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ProcesNm`** | `varchar(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ProAgrupa`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProNivel`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`APgmId`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ASysId`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ProOrden`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ProImage`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProTipo`** | `varchar(4)` | NO | Campo transaccional de Hosvital HIS |
