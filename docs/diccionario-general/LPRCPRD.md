# LPRCPRD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`LPrCod`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`LPrDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`LPrFchIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LprFchFin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`LPrPorPrm`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
