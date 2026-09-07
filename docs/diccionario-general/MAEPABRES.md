# MAEPABRES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCodP`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNumC`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNCReCtv`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCReFeH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCReUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCReEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCIngCs`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCAnReU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCAnReF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPNCReObs`** | `char(240)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCNSSOLC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
