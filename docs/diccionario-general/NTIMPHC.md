# NTIMPHC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NImFch`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`NImDsc`** | `char(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MMCODM`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NtImpTip`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NtImpFol`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NtImpIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
