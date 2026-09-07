# IFREGTRN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IFCsc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IFFolio`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IFDocNro`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IFDocTip`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IFResol`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IFErrCod`** | `char(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFErrDsc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnFH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnEst`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnNL`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnTip`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnReq`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFTrnRes`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFCodEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IFCodSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
