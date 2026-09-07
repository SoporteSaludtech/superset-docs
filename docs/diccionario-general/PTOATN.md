# PTOATN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PtoAtnCdg`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PtoAtnDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PtoAtnPor`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PtoAtnMed`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PtoAtnTer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PtoAtnTC`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PtoIndCap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
