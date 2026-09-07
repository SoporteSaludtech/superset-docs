# PROVEEDOR3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCodMor`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvVigMor`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`PrvMorCre`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvMorDeb`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvDiaMorI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvDiaMorF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvTasMor`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvEstMor`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
