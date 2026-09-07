# ANUCAUPRD

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ACPNroFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ACPMaTip`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ACPMaCls`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ACPCodEmp`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ACPCodSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ACPDocCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ACPNroDoc`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
