# ENTTURN1

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
| 🔑 | **`TurCod`** | `decimal(12,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodPago`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EntVlrPag`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TurNoCnsg`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EntVlrRmp`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
