# FCTAG03

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AFCscS`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AFCnsAgr`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AFCntS`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFVaTS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFBodEn`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFBodSal`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFCenCos`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFNumOrsS`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFTipOrsS`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFCscOrsS`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFDatSum`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
