# CTCMENPDE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTCtvo`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTCDesAtr`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CTCDesDet`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
