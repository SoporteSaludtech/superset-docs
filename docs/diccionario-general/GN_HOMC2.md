# GN_HOMC2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HOM_CODI`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOM_CODD`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOM_CODC`** | `numeric(8,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HOM_VALH`** | `varchar(40)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HOM_DESH`** | `varchar(1024)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HOM_VALO`** | `varchar(40)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HOM_DESO`** | `varchar(1024)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HOM_CCEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
