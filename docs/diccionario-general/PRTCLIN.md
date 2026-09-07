# PRTCLIN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PClCod`** | `char(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PClDsc`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PClTpo`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PClArc`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PCLARCBLO`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
