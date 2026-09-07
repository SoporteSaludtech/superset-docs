# INGRESOMP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IngCtvMoP`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IngCodPab`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngCodCam`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFecMoP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngUsuMoP`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngFecMoE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngUrgObs`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
