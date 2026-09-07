# NOTADMMED

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
| 🔑 | **`NOTAMCSC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOTAMOBS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOTAMFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOTAMTIP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOTAMCOES`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOTAMCOME`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOTAMUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOTCLAPRC`** | `nchar(4)` | SI | Campo transaccional de Hosvital HIS |
