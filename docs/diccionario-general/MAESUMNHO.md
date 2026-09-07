# MAESUMNHO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MSCodi`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAc`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSForm`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCd`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSCodiHom`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSPrAcHom`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSFormHom`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CncCdHom`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MSDosEqu`** | `varchar(400)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSVALFOR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSOBSIT`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRECOIT`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSDSCIT`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSRIESIT`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSTIPPRO`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSUSUIT`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MSFECIT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
