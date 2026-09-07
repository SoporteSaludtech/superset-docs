# MEDCABPAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCabMMCODM`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCabMECodE`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MCabMeEste`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCabFecVi`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MCabEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
