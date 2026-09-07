# NINORPOL2

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
|  | **`NINPTDSC`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPTEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPTFC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPTUC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPTFI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPTUI`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`NINPTNV`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NINPTFVI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINPTFVF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
