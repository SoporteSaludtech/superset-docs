# HEMMETDXN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HEMMETCOD`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HEMMETPRC`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HEMMETSEG`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMMETDSC`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMMETVAL`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMMETRAN`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMMETBASV`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMMETINT`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEMMETDMAX`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
