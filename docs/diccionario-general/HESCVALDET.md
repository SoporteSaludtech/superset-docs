# HESCVALDET

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EscValCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EscVDItem`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`EscVDTipo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscVDResp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EscVDRanEdad`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
