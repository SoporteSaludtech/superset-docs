# CUENTASN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EMPCODNI`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CntCodNI`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CntPrcNI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CntEstNI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
