# RADCUEN2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadCueDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadCueCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadRegCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadConCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CocGenCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RadConCan`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadConObs`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCoVAnI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCoVIVa`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCoVNet`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNCCOD`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadSedCCo`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadConCli`** | `char(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadPorIva`** | `decimal(12,9)` | SI | Campo transaccional de Hosvital HIS |
