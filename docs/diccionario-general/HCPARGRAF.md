# HCPARGRAF

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HcParGCtv`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HcParGraCo`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HcParGraDe`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HcParGraIm`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`HcParBB`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
