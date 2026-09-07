# NOREAB

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NReaNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`NReaBdOrg`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NReaBdDes`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NReaFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NReaCUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
