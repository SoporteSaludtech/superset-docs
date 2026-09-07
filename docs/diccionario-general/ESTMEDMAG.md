# ESTMEDMAG

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CEMMCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CEMMNom`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CEMMNArc`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CEMFrmXML`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CEMMEnv`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CEMMVer`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CEMMCpt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TAGXML`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
