# RADCUERIP

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadCueDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadCueCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RaCuCnRi`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RadCueUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
