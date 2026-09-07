# PEDPAQQX

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ProEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProMCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProCirCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PaqCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PQCantPaq`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQEdoDes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PqEdoGas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQCodEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQUsuDes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQSpsErr`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQSpsCnf`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQSpsEC`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PQConCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
