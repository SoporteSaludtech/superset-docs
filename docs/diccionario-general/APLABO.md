# APLABO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AplAboNC`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AplAboCli`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAboDoc`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAboNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAboSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAboVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAboUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAboFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAboEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAbCAnu`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAbFAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AplAbUAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
