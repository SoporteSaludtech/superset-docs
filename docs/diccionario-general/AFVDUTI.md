# AFVDUTI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFVUCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AcFVUNue`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFVUUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFVUFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFFchMod`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFVUTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFVUNroD`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFVUCtoH`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
