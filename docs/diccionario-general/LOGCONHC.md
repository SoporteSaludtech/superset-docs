# LOGCONHC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FECHORCON`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`LOGMOTCON`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSUser`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LOGESTTRA`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LOGNOMREP`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
