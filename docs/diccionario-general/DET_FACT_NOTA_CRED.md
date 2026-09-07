# DET_FACT_NOTA_CRED

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`factNotaCrediId`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`codProducto`** | `varchar(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`descripcion`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`cantidad`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`centroCosto`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorUnitario`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`subtotalFactura`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ivaFactura`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorTotal`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorAfectar`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorNotaCredito`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorSoportado`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`subtotalNota`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ivaNota`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`porcentajeIva`** | `decimal(5,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`codigoImpuesto`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`motivoGlosa`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`consecutivoFactura`** | `int` | SI | Campo transaccional de Hosvital HIS |
