# GRPBODEN1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GrpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GrpTipBod`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GrpCntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`GrpCntInv`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GrpCntCon`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRPCNTDDN`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRPCNTCDN`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRPCNTCRN`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GRPCNTDRN`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
