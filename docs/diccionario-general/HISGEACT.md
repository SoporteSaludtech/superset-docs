# HISGEACT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HisGeCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HisGFoli`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGFchRg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGFUM`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGFPP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISAUNFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISESTGES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISOBSANU`** | `varchar(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISMEDANU`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTIPTOM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISEGECO`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISFECECO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISINDEGM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCSCGES`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGeRie`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisGeNroBB`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDATPAD`** | `varchar(2500)` | SI | Campo transaccional de Hosvital HIS |
