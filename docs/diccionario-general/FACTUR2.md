# FACTUR2

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
| 🔑 | **`FacturNro`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FacCodImp`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FacPrcImp`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacVlrImp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
