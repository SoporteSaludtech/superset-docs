# MAECOTI2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotConse`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotConSum`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MSRESO`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCanSum`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotValUnS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotValToS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotTpoTrS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPaqCod`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
