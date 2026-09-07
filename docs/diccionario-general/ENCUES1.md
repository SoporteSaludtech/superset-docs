# ENCUES1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncCod`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncVer`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EncAgrPr`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EncAgrDsc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncAgrOrd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncAgrTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncUlCPr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncIsMen`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncGriCol`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EncTipAgr`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
