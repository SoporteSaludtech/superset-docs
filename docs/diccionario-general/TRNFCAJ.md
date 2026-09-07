# TRNFCAJ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TraDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TrnCajNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TCUsuOrg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TCUsuDes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrfCajFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrfCajVlr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrfCajEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnCodPag`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnRcCsc`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnAboDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnAboNUm`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnAboCnP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnTurCoO`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnTurCodD`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnNumCoO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnNumCoD`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnTipo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnUlCsCo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnConTot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnAnConO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrnAnConD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
