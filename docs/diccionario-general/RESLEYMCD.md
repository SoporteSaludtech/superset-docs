# RESLEYMCD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResLeyDet`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResLeyCas`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResLVar`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResLVarVlr`** | `varchar(5000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLVarObs`** | `varchar(6000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLVarFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLVarHor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLVarRes`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLVarImp`** | `varchar(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLVarEsp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLVarMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyCau`** | `varchar(256)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyFecA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResLeyDecC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
