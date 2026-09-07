# PRPCRNL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRnCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MMCODM`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TRnCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRnFchIng`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRnEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
