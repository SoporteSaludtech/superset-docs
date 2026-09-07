# ENVHSTCLN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EnvNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EnHsClCn`** | `decimal(18,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EnHsClNm`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EnHsClFl`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
