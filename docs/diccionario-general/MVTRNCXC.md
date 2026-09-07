# MVTRNCXC

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
| 🔑 | **`MvTrnNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvTrnFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrnCnp`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrnMBse`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrnTCmb`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvTrnEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
