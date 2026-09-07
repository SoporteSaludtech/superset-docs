# MAEATEPLA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MAPFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MAPTipFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MAPNumTra`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPFchTra`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAPFacDif`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
