# PAQUETE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PaqMsreso`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PaqNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PaqNom`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PaqFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PaqMsUser`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PaqEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
