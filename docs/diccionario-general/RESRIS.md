# RESRIS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ResEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResDocPR`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResTDPR`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResFolPR`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResPro`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResCon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResFecEnv`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResProLla`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResMsgHL7`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResRISHL7`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResEstTra`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResResRIS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResNumCit`** | `int` | SI | Campo transaccional de Hosvital HIS |
