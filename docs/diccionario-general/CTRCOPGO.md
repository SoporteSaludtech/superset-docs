# CTRCOPGO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FctCpg`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FctNomEmp`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FctFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FctVlr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`FctInd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TotSub`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TotAbo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FctCodDxS`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NroFctra`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtvoActe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtvoAten`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FctIndTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
