# EMPCLACON

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EMCSTRCON`** | `varchar(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMCFCHCAR`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMCUSUCAR`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMCWKSCAR`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EMCESTUSO`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMCFCHUSO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EMCUSUUSO`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EMCWKSUSO`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
