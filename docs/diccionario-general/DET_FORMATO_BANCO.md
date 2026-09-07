# DET_FORMATO_BANCO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`idFormatoBanco`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`tipoRegistro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`columnaDesde`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`columnaHasta`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoVariable`** | `varchar(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`valorVariable`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`equivalencia`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`longitud`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`completarCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoDeDato`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
