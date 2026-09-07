# CUOACUPAG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CuoAPagId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PagAcuId`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PagNumPag`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CuoEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuoMcdPto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuoTipCuo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuoPorCuo`** | `decimal(9,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuoValCuo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuoFecCuo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuoCnsUPa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CuoEstCer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
