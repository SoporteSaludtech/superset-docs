# DEPAVAACT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFAvNro`** | `decimal(16,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DepAvaAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DepAvaMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`DepAvaCto`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DepAvaVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DepAvaBse`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DepAvaDep`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DepAvaTot`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DepAvaCnt`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
