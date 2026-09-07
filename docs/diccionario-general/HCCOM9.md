# HCCOM9

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
| 🔑 | **`HCFCCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCFCCSC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCFCFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFCTipC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFCCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPrCodi`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFCResul`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
