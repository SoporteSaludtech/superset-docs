# TMPCOSMOV

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TCMEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCMDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCMDocNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCMDocCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TCMDocRef`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TCMCntCod`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TCMCUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TCMSUCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TCMCCCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TCMSCCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
