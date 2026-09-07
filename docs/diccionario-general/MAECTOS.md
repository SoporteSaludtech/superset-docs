# MAECTOS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MeCnsCnt`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MECTope`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MESalMi`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtoFchIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeCfcha1`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeVlrReg`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeVlrFact`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeVlrNoC`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeVlrAlar`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeMenVig`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeResCon`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeEmpUbi`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeSedUbi`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeAreUbi`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeEstUbi`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeNivUbi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeNumPol`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeTipPol`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeObsPol`** | `char(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeValPol`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaeFvePol`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
