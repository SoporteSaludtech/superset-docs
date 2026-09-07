# HCNANDXFR

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
| 🔑 | **`FACNANCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`FACNANFEC`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`FACNANUSU`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
