# HCCOM1DES

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
| 🔑 | **`HISDesAtr`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HISDesDet`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDESIMA`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisDesTpo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisDesRep`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
