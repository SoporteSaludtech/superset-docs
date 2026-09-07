# MDPTRAFIS

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
| 🔑 | **`MdpFisNum`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MdpFisCal`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisCam`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisTro`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisSal`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisEsa`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisAbd`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisAlt`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisMed`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisBaj`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisEae`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDpFisBic`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisBan`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisTrt`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisSbe`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisEnf`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisEsd`** | `decimal(11,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisRec`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MdpFisCon`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
