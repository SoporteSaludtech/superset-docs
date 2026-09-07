# CLIENTE2

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CLICOD`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CliCodMor`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CliDiaMorI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliDiaMorF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CliTasMor`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
