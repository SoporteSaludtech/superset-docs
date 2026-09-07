# INTINGRES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IINId`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ClaPro`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SisTerId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IINTip`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IINIT`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IINFecCre`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`IngAteEgr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Intentos`** | `int` | SI | Campo transaccional de Hosvital HIS |
