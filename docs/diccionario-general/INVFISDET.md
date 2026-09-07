# INVFISDET

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ID`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IDINVFIS`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LotUbiCtv`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LoteCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LotSalUni`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`LoteFVcto`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ValUnt`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
