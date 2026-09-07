# RSMAUXT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`RsmEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RsmCtnCon`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RsmAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RsmMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`RsmNivX`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsAxDebX`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsAxCreX`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsAxSAntX`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RsAxSActX`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
