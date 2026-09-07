# MEDPAC1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtvMed`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MedCtvMov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MedTipMov`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedFchMov`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedUsuMov`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedCntMov`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedfolMov`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
