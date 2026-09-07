# DESCIRTEJ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`CodEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodMcdpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodMed`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodCir`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodCnsTej`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CodDesTej`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
