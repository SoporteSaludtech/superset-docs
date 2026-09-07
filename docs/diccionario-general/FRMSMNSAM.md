# FRMSMNSAM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FrADocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FrACtvDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FraFecFor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrANroFor`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FraFecReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrAMENNIT`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrABodega`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrAMMCODM`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrAMECodE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrAMMNomM`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrAFolio`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrAEstado`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrAMpCodP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`FrATipAte`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FraIngCtv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
