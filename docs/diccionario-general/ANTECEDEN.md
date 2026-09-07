# ANTECEDEN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AntCtvo`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`HISCKEY`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTipDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntConc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntDesc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AntTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
