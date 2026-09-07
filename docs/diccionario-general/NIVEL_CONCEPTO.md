# NIVEL_CONCEPTO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`nivel`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`operacion`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`descripcion`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ultimoNivel`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`nivelPadre`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoReporte`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`cuentaDesde`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`cuentaHasta`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`cantidadFirmas`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`nombreArchivo`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`orden`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorAcumulado`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
