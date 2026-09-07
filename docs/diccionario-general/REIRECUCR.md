# REIRECUCR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICurCod`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICurSex`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIPerInf`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIPerSup`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICurUnX`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICurUnY`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICurVlX`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICurVlY`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIFecHr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
