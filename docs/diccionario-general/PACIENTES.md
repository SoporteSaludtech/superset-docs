# PACIENTES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`cns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`cedulaMSP`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`nombre`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`paterno`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`materno`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`sexoMSP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`direccion`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`telefono`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoOperac`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idHospital`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
