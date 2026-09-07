# HCREGCUCR

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
| 🔑 | **`CurCodCur`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CurSexCur`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCRPerInf`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRPerSup`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRCurUnX`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRCurUnY`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRCurVlX`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRCurVlY`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRFecHr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
