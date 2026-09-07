# PPTOOPECP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`POCCod`** | `varchar(100)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocCodOPe`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocConOpe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SalPreVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SalPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RcuId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`UniNegId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`POCCPCCod`** | `varchar(40)` | NO | Campo transaccional de Hosvital HIS |
|  | **`POCVlrMov`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`POCVlrEje`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`POCEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`POCVlrAnu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
