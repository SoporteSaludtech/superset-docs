# LOGEMAIL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`mcdpto`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`tipo`** | `varchar(50)` | NO | Campo transaccional de Hosvital HIS |
|  | **`estado`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`solicitud`** | `varchar(MAX)` | NO | Campo transaccional de Hosvital HIS |
|  | **`destinoEmail`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`codigoTercero`** | `varchar(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`fechaProceso`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`mensajeError`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`documento`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`numeroDocumento`** | `int` | SI | Campo transaccional de Hosvital HIS |
