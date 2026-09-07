# INVFISCNTPROD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IDCNTPROD`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IDCNTDET`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NroCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LoteCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LoteFVcto`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LoteSalUnd`** | `money` | NO | Campo transaccional de Hosvital HIS |
