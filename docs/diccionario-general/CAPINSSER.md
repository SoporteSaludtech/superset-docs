# CAPINSSER

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PreCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PreSedCod`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SERCOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TIPSERCOD`** | `varchar(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MECodE`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SERDISOCU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SerOcuPer`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SerOcuHor`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SERDISDIS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SerDisPer`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`SerDisHor`** | `int` | SI | Campo transaccional de Hosvital HIS |
