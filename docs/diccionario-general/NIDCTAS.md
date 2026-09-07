# NIDCTAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDCANIO`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDCMES`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDCCSC`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDCDI`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDCDF`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIDCPRC`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCUC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCFC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCUI`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCFI`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCUSO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDCTIP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
