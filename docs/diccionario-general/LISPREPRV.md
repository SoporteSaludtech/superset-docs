# LISPREPRV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`LipCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LipCnsPre`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`LipVigPre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LipPorPre`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
