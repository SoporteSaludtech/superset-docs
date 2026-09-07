# EVEADVADJ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EVEADVSEC`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EVEADJSEC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CodIma`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEADJDES`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEADJRUT`** | `varchar(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEADJOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EVEADJEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
