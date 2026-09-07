# MAEPAB11

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCodP`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNumC`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HisCamCtv`** | `decimal(10,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HisCamEdo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisCamFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisCamHor`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisCamUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisCnsIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
