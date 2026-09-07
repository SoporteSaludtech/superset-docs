# ADNCAMO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcDCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ADNcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ADNCVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADNCFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADNUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADNCFReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADNcDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADNcNroD`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADNNueVU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADNAntVU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ADNcAEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
