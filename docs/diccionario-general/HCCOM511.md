# HCCOM511

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DMCodi`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DgnRslCla`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DgnRslTip`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DgnRslObs`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
