# INVFISCNT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IDCNT`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvFechIni`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvTip`** | `char(7)` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvEst`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`InvUsrCier`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`InvFechCier`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`docum`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`numDocEnt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`numDocSal`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idInvFis`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
