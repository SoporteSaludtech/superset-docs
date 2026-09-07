# CTCMENP1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTCtvo`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTCtvPOS`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CTCMsCo`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCanPOS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTDosDia`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTPoso`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTPriAct`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTTieDur`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTPreMed`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCncCd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CTCodPro`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
