# ABONOS2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABODOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABONUM`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AboCnsPgo`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AboCnsCon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AboVlrCon`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboNroCo2`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboAnuCo2`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
