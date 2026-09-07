# INVFISCNTDET

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IDCNTDET`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IDCNT`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NroCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UbiCnt`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvUsrCnt`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InvEstCnt`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`LotUbiCtv`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
