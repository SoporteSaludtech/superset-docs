# TMPCAUPRD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TCPEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCPSedCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCPTerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCPCueCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCauPrdCU`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCauPrdSU`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCauPrdCC`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCauPrdSC`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCauFch`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`TCPValor`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
