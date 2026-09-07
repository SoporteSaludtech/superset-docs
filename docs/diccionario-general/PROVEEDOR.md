# PROVEEDOR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvDiaIni`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrvDiaFin`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvPorDes`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
