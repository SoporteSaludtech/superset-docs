# IFREGTH

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IFFolioH`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IFDocNroH`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IFDocTipH`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IFResolH`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IFCscH`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IFErrCodH`** | `char(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFErrDscH`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnFHH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnUsrH`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnEstH`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnNLH`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnTipH`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnReqH`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnResH`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFCodEmpH`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFCodSedH`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
