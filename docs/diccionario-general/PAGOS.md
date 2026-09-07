# PAGOS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PAGNUM`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGVLR`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGFCH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGAPL`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGCCJ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGDEL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGUSR`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGFCS`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurCod`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagConta`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagObs`** | `char(240)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipRei`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagUsrRei`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagFchRei`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagHorRei`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagRespDoc`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagRespNom`** | `char(73)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagIdPC`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagNuCsg`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PagAnuCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CJSCod`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0011`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGSEDABO`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGEMPABO`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGABODOC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGFACREC`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PAGDOCNOC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PAGNUMNOC`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NotReConta`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`IDPRC0016`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
