# AGRASIS1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AgrAsCd`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AgrTerCod`** | `char(11)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AgrTRazS`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgrAsFcIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ArgAsEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgrAsFcRt`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
