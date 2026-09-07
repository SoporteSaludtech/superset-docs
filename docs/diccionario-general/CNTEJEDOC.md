# CNTEJEDOC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`Doc1Tpo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`Doc1Nro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`Doc2Tpo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`Doc2Nro`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`Doc1Vlr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`Doc1Eje`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`Doc2Vlr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`Doc2Eje`** | `money` | SI | Campo transaccional de Hosvital HIS |
