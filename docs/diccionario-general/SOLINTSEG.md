# SOLINTSEG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocInt`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipInt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedSol`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EspSol`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EspCon`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipAte`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaPri`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaRelUno`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaRelDos`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaRelTre`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ObsInt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PriInt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EstInt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FecHorCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SubInt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ObjInt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AnaInt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PlaInt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TraInt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImaSol`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
