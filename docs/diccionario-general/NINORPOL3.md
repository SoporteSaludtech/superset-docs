# NINORPOL3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NINPTIP`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NINPSEC`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NINPTIT`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NINPPRF`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NINPPDSC`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPPTXT`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPPEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPPFC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPPUC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPPFI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPPUI`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`NINPTNV`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NINPPFVI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPPFVF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
