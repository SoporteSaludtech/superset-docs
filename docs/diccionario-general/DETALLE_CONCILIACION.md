# DETALLE_CONCILIACION

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`bancod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`mesmov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`aniomov`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`cuentaContable`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`documento`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`numero`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaContable`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`referencia`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorContable`** | `decimal(18,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`transaccion`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaTransaccion`** | `date` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorExtracto`** | `decimal(18,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipo`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`observacion`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`referenciaCliente`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
