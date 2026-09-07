# TERASIS4

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TerHorCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TerHorDia`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerHorIni`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerHorFin`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TerHorEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
