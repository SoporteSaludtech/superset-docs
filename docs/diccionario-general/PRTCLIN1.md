# PRTCLIN1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PClCod`** | `char(30)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PCLCANDIA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PCLDIL`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PCLVIA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PCLDIAAPL`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PCLTIEINF`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
