# CMPPRE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AgCCdg`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AgCTranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCDes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCCon`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCVlrBse`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCFchVal`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MetCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgCUltCns`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGCNI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
