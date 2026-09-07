# AUTRIZ

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
| 🔑 | **`AutNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AutFchF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutMsUser`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutConc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutEstF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutDocMvt`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutNrMvt`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AutTraCod`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
