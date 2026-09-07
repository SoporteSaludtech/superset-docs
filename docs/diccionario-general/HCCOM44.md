# HCCOM44

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCDIETCD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCDIEEST`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDieDsc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EvCodEnf`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EvOdsEf`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EvFeHrEf`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDUNDMED`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDTMSMAX`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDVOLMAX`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOBSVREV`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCUSUAREV`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCFECHREV`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCDESTREV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
