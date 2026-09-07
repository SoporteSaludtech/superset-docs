# REICOM6

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PntCodi`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`REIREIPa6`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
