# ADGLORA1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GlorCtv`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GlsRaCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloRItem`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GlorCtvIt`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`GlorVlrMo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorVlIva`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorVlNet`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorVlrCa`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GlorConCn`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloDetObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
