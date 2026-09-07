# LOGS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`LogId`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LogProceso`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogUsuario`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogFecha`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogHora`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogOperaci`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipLId`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogPgmName`** | `char(31)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogFchHor`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogUsrAppI`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LogDesc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
