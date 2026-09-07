# HCENTREST

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCTOKEN`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCFINI`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCFFIN`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCTOKES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
