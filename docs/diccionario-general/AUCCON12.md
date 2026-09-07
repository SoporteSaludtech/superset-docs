# AUCCON12

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudForCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AudPreCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AucC12Vre`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AucC12Vr2`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AucC12Vr1`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AucC12Obs`** | `char(240)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AucC12Ob1`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AucC12Fhc`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`AucC12Ucr`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AucC12VI1`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AucC12VI2`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AucC12VD1`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AucC12VD2`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AucC12RV1`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AucC12RV2`** | `money` | SI | Campo transaccional de Hosvital HIS |
