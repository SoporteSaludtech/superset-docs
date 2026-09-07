# CTRCNSFAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CNSFACTU`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CNSFACFCH`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNSFACTIP`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNSFACPC`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNSFACUSU`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
