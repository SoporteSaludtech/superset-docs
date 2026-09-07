# MIPRESPRESCRIPCION

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IdPrescripcion`** | `nvarchar(510)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NoPrescripcion`** | `nvarchar(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FPrescripcion`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`TipoIDPaciente`** | `nchar(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NroIDPaciente`** | `nvarchar(40)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FolioPrescrip`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EstPres`** | `nchar(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EstEnvio`** | `nchar(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`JsonPrescripcion`** | `nvarchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EstEnvio2do`** | `nchar(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrescNroReinten`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrescMsgProc`** | `nvarchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrescUsuMod`** | `nchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrescFecMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
