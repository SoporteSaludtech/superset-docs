# LISPREPRS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`LipCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LipCnsPre`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LipCodSuH`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LipPreSum`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
