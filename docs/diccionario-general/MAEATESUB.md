# MAEATESUB

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPNFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MATipDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MaTSubCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MaTCodImp`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaTPorIva`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MaTBasImp`** | `decimal(17,4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MaTValImp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
