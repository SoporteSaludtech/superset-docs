# SOLCOTI1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SolNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`SolItm`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`SolProCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolProDsc`** | `char(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolObs`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SolUnMdCod`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
