# MOVREU1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BodReuCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovReuDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovReuNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MovReuCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MPCedu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MPTDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReuLot`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReuCan`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReuTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReuNo`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MorReuFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReuEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReuFol`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReuUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReuND`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MovReuCU`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConTip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConCod`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
