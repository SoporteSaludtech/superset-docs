# FORAIEPI2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ForMatCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ForAieCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`GPACOD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreCodIgo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ForAieOrd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForAieEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
