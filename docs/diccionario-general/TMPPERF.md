# TMPPERF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TmpApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpPrg`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpEve`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TmpGrup`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCrit`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
