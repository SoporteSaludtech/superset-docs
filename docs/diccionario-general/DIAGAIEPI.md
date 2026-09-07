# DIAGAIEPI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`DiaCodIgo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DiaAgnDes`** | `char(80)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DiaCodRed`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DiaCodGre`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DiaCodBlu`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DiaFecHor`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`DiaUsuCre`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DMCODI`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaAyuRap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DiaApliEnf`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
