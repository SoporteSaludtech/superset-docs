# DESCIRMED

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CodEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodMcdpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodMed`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodCir`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`CedPac`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HorIniCir`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HorFinCir`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaEnt`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaSal`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipHer`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CanSan`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TiePer`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TieClamp`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ViaIng`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EstCir`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipAne`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CscIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DQxCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesCir`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesCom`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesDatMUn`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesInNNIS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesIndCom`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesHalEnc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesObsDxE`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesObsDxS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DesIndTej`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECFINCIR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECINICIR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DESESTSAL`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DESMATOST`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DESDISMED`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
