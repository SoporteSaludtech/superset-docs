# HCNANDXNO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DIANANCOD`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NOCNANCOD`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOCNANPDI`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOCNANPDO`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOCNANPDD`** | `varchar(50)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOCNANOBS`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOCNANEST`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOCNANFEC`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOCNANUSU`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
