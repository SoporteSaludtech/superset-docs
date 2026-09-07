# IMAREQING

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ImaDocPac`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ImaTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ImaTipAte`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ImaConIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ImaCodReq`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ImaNitR`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ImaRutIma`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImaCmpRqs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
