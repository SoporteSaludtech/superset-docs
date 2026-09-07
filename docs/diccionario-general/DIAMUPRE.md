# DIAMUPRE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`DimCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DimDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DimAgr`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DimSub`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DimIndUrg`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DimVlr`** | `money` | SI | Campo transaccional de Hosvital HIS |
