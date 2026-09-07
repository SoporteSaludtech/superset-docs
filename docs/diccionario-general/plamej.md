# plamej

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`mejempcod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`mejprecod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`mejpresed`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`mejindcod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`mejpro`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`mejaccion`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`mejfchini`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`mejfchfin`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`mejres`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MejEmpNom`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MejPreNom`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MejIndDsc`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
