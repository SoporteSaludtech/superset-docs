# MODINCPAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`IncEmpPac`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IncSedPad`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IncDocCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IncConPac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`IncConMod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`IncCamMod`** | `varchar(100)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IncValAnt`** | `varchar(300)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IncValNue`** | `varchar(300)` | NO | Campo transaccional de Hosvital HIS |
|  | **`IncFecMod`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`IncUsuMod`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
