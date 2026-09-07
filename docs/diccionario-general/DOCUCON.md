# DOCUCON

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocSig`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocTranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocCodTri`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocFacObl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocRadi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocCscEmp`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocCscL`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocApl`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocNI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCDSREDI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCATSNOC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCATSCOM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DOCATSRTV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
