# ADMUSRFCH

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AUsrId`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AUsrFch`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`AUsrDes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrHorIni`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrHorFin`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
