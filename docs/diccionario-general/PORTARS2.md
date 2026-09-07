# PORTARS2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PSCodi`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtvPS`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`PSVigIn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PSVALU1`** | `money` | SI | Campo transaccional de Hosvital HIS |
