# MAEATEOTS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MAOtSMPNF`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MAOtSTipD`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MAOtSDoR`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAOtSObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAOtSVal`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAOtSUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAOtSFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
