# DonOrganos

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
| 🔑 | **`DonCod`** | `numeric(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DonCodMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DonEsp`** | `numeric(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DonMoOpPre`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DonFecSus`** | `date` | SI | Campo transaccional de Hosvital HIS |
|  | **`DonEntSus`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DonObse`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DonFec`** | `datetime2` | SI | Campo transaccional de Hosvital HIS |
