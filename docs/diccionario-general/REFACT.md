# REFACT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ReFatNum`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ReFatMat`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MotAnCod`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReFacFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RefacUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ReFacObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
