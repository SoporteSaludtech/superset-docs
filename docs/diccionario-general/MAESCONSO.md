# MAESCONSO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MaeConAni`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MaeConCnC`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MaeConCnD`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeConTip`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeConCNv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeCoCDNa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeConCTr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TpCCodCap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeNatCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
