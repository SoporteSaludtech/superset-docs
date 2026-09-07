# CLIENTE1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLICOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CliDepCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliMunCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliTrcTlf`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliTrcDir`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliTrcFax`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliTrcAAe`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliEmail`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliCon`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliCrgCon`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliCupCre`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipPCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLIDCPLCC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLICIR30`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLICLC2`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLICLC1`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CLICLC3`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliTipAse`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
