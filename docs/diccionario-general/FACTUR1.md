# FACTUR1

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
| 🔑 | **`FacturNro`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FacConCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FacConCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`FacTotAnI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacTotDes`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacValImp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacTotDsI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IMPCOD`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacCantid`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FacValUni`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
