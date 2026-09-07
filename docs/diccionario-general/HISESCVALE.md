# HISESCVALE

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
| 🔑 | **`EscValCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`EscValFol`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValNom`** | `char(73)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValFcNa`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValSex`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValEdCorr`** | `char(150)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValAcuNom`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValParen`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValMCod`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValMNom`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValME`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValMENom`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValFcAp`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValCal`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`EsValObs`** | `varchar(1024)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscValReal`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
