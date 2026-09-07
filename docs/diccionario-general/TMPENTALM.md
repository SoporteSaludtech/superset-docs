# TMPENTALM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TEEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TEMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TEDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TEDocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TECsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`TEMsReso`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEMsNomG`** | `char(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEMsCtrLt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEMsUnd`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TECant`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEVlrUni`** | `decimal(17,6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEPrcDsto`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`TETotDsto`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEPrcIVA`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TETotIVA`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TETotal`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEFctCnv`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEBodega`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEMsInvN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEVlrAfe`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEValor`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEMvtoCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEVlrSIVA`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TELotCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEFchVto`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TEBodUbiC`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
