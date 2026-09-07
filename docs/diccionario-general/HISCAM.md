# HISCAM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCodP`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPNumC`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`FecCam`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EstCam`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`UsuCamEst`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
