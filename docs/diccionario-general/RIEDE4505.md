# RIEDE4505

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`RieEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RieCod`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RieCnsDet`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RieCodDet`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`RieCodReD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieCodRDD`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieCodDxP`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieValAdi`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieEmb`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieTieFUR`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieTenSis`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieIMC`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieCauExt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieApDeDx`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieRanTSi`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieApFuRa`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieRanTDi`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieTenDia`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RiePrcOrd`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieFchTrt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RieVisRes`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
