# PAGACU

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PagAcuId`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PagNumPag`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PagPorCIn`** | `decimal(9,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagFecCIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FecFecCOr`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`PagCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagNumCIn`** | `decimal(2,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagNumCOr`** | `numeric(2,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagValCIn`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagCotValC`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EMPCOD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagAcuEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ID_USER_PAY`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OBSERVATION_PAY`** | `varchar(501)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UPDATE_PAY`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
