# MORTAL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MorNit`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MorCed`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MorNom`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorDS1`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorDeD`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorEst`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorHIn`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorHEg`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorFIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorFEg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorSex`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorFNa`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorEda`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorSum`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorClP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
