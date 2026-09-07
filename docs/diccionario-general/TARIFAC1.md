# TARIFAC1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TarFacCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TarFacIni`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TarFacFin`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`TarFacVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
