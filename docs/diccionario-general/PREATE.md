# PREATE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PACtvo`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PADesc`** | `char(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAFecReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAUsuReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLAESTCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PAESTOBS`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAESTACT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAFECINA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAUSUINA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
