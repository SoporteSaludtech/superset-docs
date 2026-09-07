# LOTESUM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LoteCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LoteFVcto`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LoteCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`LoteSalUnd`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`LoteCstPrm`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LoteEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LoteFeEnA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LOTECSTPN`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
