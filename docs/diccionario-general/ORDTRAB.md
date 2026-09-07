# ORDTRAB

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
| 🔑 | **`OrdTrbNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbCPz`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbDPz`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbDsc`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbNFa`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbFcF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrUsuC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrUsuA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbRec`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbUlt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbObs`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbAnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbCC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbCDP`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrbEPr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTipDis`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdTrFchA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
