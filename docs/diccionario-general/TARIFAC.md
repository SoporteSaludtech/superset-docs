# TARIFAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TarFacCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TarFacDsc`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TarFacTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AgrFacCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TarFacEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TarFacLot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`IMPCOD`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TarFacCC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TarFacRec`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
