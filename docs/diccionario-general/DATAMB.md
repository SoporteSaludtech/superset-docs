# DATAMB

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DatCscIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DatTipIE`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DatTipAmb`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatPlaAmb`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatDirIni`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatDirFin`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatUR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatCodDep`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatCodMun`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatCedEnt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatNomEnt`** | `char(73)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatRMEnt`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatAmbPro`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatNitEmp`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatNomEmp`** | `char(35)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatCedCon`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatTipCed`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatPriNom`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatSegNom`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatPriApe`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatSegApe`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatPerNat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatCodHab`** | `char(12)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatDirRec`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatTelRec`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DatOtrVeh`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
