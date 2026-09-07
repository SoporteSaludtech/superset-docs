# NINOTREV1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NINRNRO`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NINRANIO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINRMES`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINRFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINRUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINRTIT`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINRNOT`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINRVIS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NINRTIP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
