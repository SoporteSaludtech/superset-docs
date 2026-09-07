# LEGCAJMEN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LegCMNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LegCMEst`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegCMFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CajMenCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegCMObs`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegUsuOpe`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegFecREg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegRDocCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegRNroDoc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegUsuReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegUltCons`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegCodSus`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LegForPag`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
