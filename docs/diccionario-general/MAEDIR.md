# MAEDIR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MDTipo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MDCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MDRuta`** | `char(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDObs`** | `char(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDPue`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDUsr`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDUsrPsw`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDIP`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDTOut`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDTipEnv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDTipDis`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDXSDASO`** | `char(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDAsunt`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDCueCor`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDNomUsu`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDNUMPRC`** | `numeric(5,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MDNUMREG`** | `numeric(5,0)` | SI | Campo transaccional de Hosvital HIS |
