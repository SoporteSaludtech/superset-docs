# KARDEX1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocTip`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MovFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovVlU`** | `decimal(16,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovVlT`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovBod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovSld`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovNrAut`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReqN`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCodPac`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovSolN`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCnsRq`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovTipDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovNumFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovTipFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovCtvIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovFolPac`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReqEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReqSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReqDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
