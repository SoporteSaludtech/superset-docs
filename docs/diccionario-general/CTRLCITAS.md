# CTRLCITAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CitEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitNum`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitCed`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CitFchHra`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`CitMtv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitStsCit`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitUsrCit`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitCmbDto`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitDocCan`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNroCan`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitNomRCa`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitParRCa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitVlrMul`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CitSedAbo`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
