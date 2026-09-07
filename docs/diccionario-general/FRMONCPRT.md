# FRMONCPRT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `nchar(30)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `nchar(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRTCOD`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCPRTFCH`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRCODI`** | `nchar(18)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PRONESQC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCPRTOBS`** | `nvarchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTEST`** | `nchar(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTUSU`** | `nchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTCLPR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTFOTE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTUSSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTFHSU`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPRTRIE`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCPPRFINT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
