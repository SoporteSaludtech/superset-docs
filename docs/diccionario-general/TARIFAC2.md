# TARIFAC2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TarFacCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TarFCntVi`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`TarFCntCo`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TarFCntDe`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
