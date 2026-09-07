# ESTTRA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EstTraCod`** | `char(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EstTraDes`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GruEstCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
