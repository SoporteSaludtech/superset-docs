# TMPSAL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TmpSalEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpSalCnt`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpSalAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpSalMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TmpSalNiv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpSalDeb`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpSalCre`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpSalVAn`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpSalVAc`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
