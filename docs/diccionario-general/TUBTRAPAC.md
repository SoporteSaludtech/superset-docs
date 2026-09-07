# TUBTRAPAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TubCedPac`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TubDocPac`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TubFol`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TubPPP`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TubCatTub`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TubFas`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TubFIFas`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
