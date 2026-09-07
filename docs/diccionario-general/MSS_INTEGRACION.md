# MSS_INTEGRACION

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`msin_id`** | `varchar(36)` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_tipo_proceso`** | `varchar(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_id_proceso`** | `varchar(36)` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_estado`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_solicitud`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_respuesta`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_estacion`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_usuario`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_fecha`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_id_destino`** | `varchar(36)` | NO | Campo transaccional de Hosvital HIS |
|  | **`msin_fecha_envio`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
