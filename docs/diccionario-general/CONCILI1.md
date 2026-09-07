# CONCILI1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConciCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConCodOpe`** | `char(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConDscOpe`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTipOpe`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcuCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
