# SINCATMVC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`DiaCodIgo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CatCodIgo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SinSigCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SinCatReq`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SinCatFho`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`SinCatUcr`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`SinCatOrd`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SinCatUcs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
