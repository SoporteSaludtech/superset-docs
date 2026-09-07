# DOCUCON1A

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EmpCodA`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocCodA`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDptoA`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocConA`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocNumInA`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumFiA`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocDscPrFA`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumAcA`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumEsA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumBqA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFchEsA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumReA`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFchReA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocDetArA`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocUsuCrA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFcHCrA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocUsuMoA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFchMoA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFacCrrA`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFacVtaA`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFacNOA`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
