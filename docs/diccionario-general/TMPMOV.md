# TMPMOV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TVlrCre`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TVlrDeb`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
