# FORMATO_BANCO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `varchar(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`bancod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`formato`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`descripcion`** | `varchar(255)` | NO | Campo transaccional de Hosvital HIS |
|  | **`tipoFormato`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`fechaCreacion`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`separadorDecimales`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`separadorColumnas`** | `varchar(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoArchivo`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
