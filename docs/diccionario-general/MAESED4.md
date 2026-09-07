# MAESED4

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDVigDAs`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`MCDUsrRDA`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MCDFchRDA`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`MCDWrkRDA`** | `char(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MCDRepLeg`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDFirRep`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDRESFAC`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDRESDESC`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCDRESFIR`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
