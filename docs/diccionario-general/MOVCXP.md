# MOVCXP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvCxPNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvCxPCsc`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvCxPFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCxPMB`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCxPTC`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCxPNuOb`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCxPNat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCxPVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCxPVEx`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CnUSub`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntSub`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCxPCnc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvCxPAct`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MVCXPTer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FljCajCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FljCajCon`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
