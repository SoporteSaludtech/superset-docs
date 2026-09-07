# ADGLOSAS2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPNFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MATipDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloCtvo`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GlsCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloItem`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloHrioTip`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloItCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloCtNDe`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`GloTipNDe`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEmpNDe`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloSedNDe`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloVlrNDe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsrNDe`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloFHrNDe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloEstCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
