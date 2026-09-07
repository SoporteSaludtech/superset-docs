# CIECAJA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CCjCod`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CCjFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSUser`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCjVlrTtl`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCCong`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CJSCod`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CCConta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
