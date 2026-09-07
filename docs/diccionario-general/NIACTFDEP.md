# NIACTFDEP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDEPANO`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIDEPPER`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIDEPCHI`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDHAANT`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDEPMES`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDHAACT`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIDEPCONT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
