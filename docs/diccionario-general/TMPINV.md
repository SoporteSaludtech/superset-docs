# TMPINV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpInvDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmInvMsR`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpInvTrn`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpInvApl`** | `char(16)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpInvCC`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpInvBog`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpInvES`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TmpInvVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpInvSC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
