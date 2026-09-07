# HCONCO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCONCCSC`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCONCDEST`** | `varchar(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCONCDESN`** | `varchar(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCONCDESM`** | `varchar(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCONESTA`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCONCFIGO`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCONFIVAL`** | `varchar(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCONCOMIT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
