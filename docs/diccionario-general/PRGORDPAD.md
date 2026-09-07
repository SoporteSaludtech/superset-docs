# PRGORDPAD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrgSede`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrgDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrgOrdNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HOPNoObl`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrgVlrPag`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgVlrDes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgVlrNet`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgPorDes`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgDocOrP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgPgNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgCodCoF`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrgCodFlC`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
