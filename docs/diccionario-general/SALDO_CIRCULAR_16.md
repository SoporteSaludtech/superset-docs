# SALDO_CIRCULAR_16

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `varchar(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`cuenta`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`tercero`** | `varchar(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`fechaCausacion`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`saldoInicial`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`debitos`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`creditos`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`saldoFinal`** | `decimal(17,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`anio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`mes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`tipo`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`fechaGeneracion`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`usuario`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`formato`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
