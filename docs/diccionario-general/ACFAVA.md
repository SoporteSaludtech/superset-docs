# ACFAVA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFAvNro`** | `decimal(16,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AcFCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvVlrN`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvVUtN`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvFchC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvCsAj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvDpAj`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvVlrA`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvTer`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvVUt`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvFUD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvCAjT`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvDAjT`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvVlrT`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFavAdep`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvNroA`** | `decimal(16,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvDocA`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvFchA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvUsuA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AcFAvAfeD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
