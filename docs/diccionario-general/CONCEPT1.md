# CONCEPT1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConTip`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConCod`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConMnjCXP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCodAgr`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCamSum`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CONNI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConMoCan`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
