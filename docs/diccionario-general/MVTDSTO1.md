# MVTDSTO1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtDCn`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MvtDstCt`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`MvtDstT`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDstN`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDstFA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDstUC`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDstUA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MvtDstVa`** | `money` | SI | Campo transaccional de Hosvital HIS |
