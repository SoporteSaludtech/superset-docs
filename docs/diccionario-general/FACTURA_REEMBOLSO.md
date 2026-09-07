# FACTURA_REEMBOLSO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `varchar(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`mcdpto`** | `varchar(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`numeroIdCliente`** | `varchar(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`fechaFactura`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`fechaRegistro`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`usuarioCreacion`** | `varchar(100)` | NO | Campo transaccional de Hosvital HIS |
|  | **`cuenta`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`documentoFactura`** | `varchar(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`numeroFactura`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`codigoContrato`** | `varchar(13)` | SI | Campo transaccional de Hosvital HIS |
|  | **`formaPago`** | `varchar(3)` | NO | Campo transaccional de Hosvital HIS |
