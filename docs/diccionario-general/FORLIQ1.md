# FORLIQ1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ForLiqCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HnrCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ForLiqVlHn`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForLiqcar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FctoCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForCodQx`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForInIm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FOREXCBAS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FORINDREC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
