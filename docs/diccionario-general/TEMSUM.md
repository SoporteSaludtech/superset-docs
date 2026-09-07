# TEMSUM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NitNum`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmCtvIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SumAgCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResoNu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CanSum`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`VaUnSu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VaToSu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TemSumAnu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
