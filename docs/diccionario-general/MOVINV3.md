# MOVINV3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvtoFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovTerCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoUltCsc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtoFchCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtObs`** | `char(350)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtTipBlt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0005`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0006`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovUsuRec`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovDepId`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
