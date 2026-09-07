# REITRIAGE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REICSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DiaCodDia`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`REITriPas`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REITrFoHC`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
