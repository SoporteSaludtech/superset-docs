# LOG_DOCUMEN_ELECTR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`idCompania`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idDocumento`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`numeroTransaccion`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`sede`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`estado`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaProceso`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaTransaccion`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`usuario`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`solicitud`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`respuesta`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoDocumentoElectronico`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`descripcion`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`reenviar`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idEncabezado`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
