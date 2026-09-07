# HISDATUSU

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HisFecHor`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HisEdoCiv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisInsAca`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisOcu`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisOcuPri`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisTipAfi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisDir`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisBar`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisMun`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisDep`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisTel`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTIPEMP`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDIRREf`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDIRSEC`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDIRCOM`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTIPCNT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
