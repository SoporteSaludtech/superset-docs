# BLTAINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BltMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`BltFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltaBod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDpto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltUltCsc`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FecActInv`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EstActInv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BltTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
