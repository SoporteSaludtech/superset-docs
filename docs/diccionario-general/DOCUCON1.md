# DOCUCON1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocCon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocNumIn`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumFi`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocDscPrf`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumAc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumEs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumBq`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFchEs`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNumRe`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFchRe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocDetAr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocUsuCr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFcHCr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocUsuMo`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFcHMo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFacCrr`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFacVta`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFacNOpe`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocTOCrr`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocTOVta`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocTONOpe`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCTORC`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCTOREI`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCFFR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCFIR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCCLATEC`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCNOTDB`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCNOTCR`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCTIPOP`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocUniOrg`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
