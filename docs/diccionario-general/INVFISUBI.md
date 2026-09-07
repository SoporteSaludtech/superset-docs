# INVFISUBI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CodEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NumBol`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AnioBol`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MesBol`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ConBol`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodProBol`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NumConBol`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`UbiCtvInB`** | `decimal(12,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CanBolInB`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuBolInB`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FchBolInB`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
