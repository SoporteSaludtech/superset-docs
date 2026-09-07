# ORDTRNS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`OTrCod`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`OTrFchSol`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OTrEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
