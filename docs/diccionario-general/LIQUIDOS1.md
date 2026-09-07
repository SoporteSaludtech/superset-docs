# LIQUIDOS1

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
| 🔑 | **`LiqCstvo`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LiqHorReg`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LiqFecReg`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`LiqCntFor`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqHorInD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqFecMasH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqFecHorR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqCntApl`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqUsuReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqEstFo1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqFolReg`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqRegObs`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqFecApl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqHorApl`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqNroBol`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqSllCal`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqFchVnc`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LiqDscG`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
