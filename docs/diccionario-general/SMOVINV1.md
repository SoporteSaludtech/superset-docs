# SMOVINV1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SDocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SMvtCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SMvtCscL`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SMvtLote`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtVcto`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtLoteES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvtCntL`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMvUbiCtv`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
