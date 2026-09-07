# NOTANUFAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NOTANFEMP`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NOTANFSED`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NOTANFDOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NOTANFCNS`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOTANFFCH`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOTANFPRF`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NOTANFNUF`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NOTANFTIF`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
