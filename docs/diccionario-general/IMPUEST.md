# IMPUEST

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IMPCOD`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ImpCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ImpFchIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImpFchFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImpPcj`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImpTopMin`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImpDstFM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ImpCodPcj`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
