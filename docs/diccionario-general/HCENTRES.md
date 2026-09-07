# HCENTRES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCtvEnt`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCTOKEN`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCFchEnt`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCMailEnt`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HcNumEst`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDocRec`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCNomRec`** | `varchar(80)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCDirRec`** | `varchar(150)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCTelRec`** | `varchar(40)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCUsrEnt`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCTPENT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCTipEnt`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
