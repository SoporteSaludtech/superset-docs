# TURQUI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TuQCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TuQFchIng`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQFchSal`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQHorIng`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQHorSal`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQPacId`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQTipDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQMedRes`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQUsrRes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQCodCto`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConsCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQNroAut`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQEstTur`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQFchReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProCirCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProEmpCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProMCDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuQTpAnst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuInsCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TuInsXML`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
