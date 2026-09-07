# PABPUNRUT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PunRutCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PunRutPab`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PunRutPabN`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PunRutPEs`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
