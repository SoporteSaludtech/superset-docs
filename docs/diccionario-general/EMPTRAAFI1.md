# EMPTRAAFI1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EmpDocAfi`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EmpTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EmpNitAfi`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EmpDesEmp`** | `char(150)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpSuc`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpMora`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpDirEmp`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpDepCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpCiuCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpCodBar`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpTel`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EMPTRATIP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
