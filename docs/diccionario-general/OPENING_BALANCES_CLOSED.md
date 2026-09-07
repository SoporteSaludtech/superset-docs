# OPENING_BALANCES_CLOSED

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ID`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`ID_COMPANY`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ID_OFFICE`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ID_STORE`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DATE_CLOSED`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`USER_CLOSED`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
