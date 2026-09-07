# SMOVINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SDocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SMvtFolio`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtClpr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtPab`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtCtvIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtDocEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtUltCsc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtTerCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtBdSol`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtBdEnt`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtCCSol`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtCscSum`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtDocRq`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtNoReq`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMVtObs`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvDocMVI`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvNroMVI`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtSedRq`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
