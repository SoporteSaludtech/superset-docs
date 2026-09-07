# ENTRALM

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
| 🔑 | **`EntANro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`OrdeDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeNum`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntAFact`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntARemi`** | `char(12)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntAEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntAFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntAUltCs`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntRcp`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntPlaSO`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntPlzSO`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntObs`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OrdeSede`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntUsuCre`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntFchCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntUsuMod`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntIndUso`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntUsuUso`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0013`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
