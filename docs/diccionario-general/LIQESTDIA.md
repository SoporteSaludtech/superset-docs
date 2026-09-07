# LIQESTDIA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MENNIT`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LIQEVICNS`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LIQESTCNS`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LIQESTATE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LIQESTPAB`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`LIQESTPRO`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LIQESTDII`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`LIQESTDIF`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
