# TMPFAC4

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TFCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmCtvIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFCsAb`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`ABONUM`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFnitA`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFFchA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFValA`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFRcIm`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUAbo`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFAboEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFAboSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFAboDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
