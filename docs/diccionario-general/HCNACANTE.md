# HCNACANTE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NacPacAnt`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NacPacDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NacFolAnt`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NacTpoAnt`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NacCnsAnt`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NacDscAnt`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NacTpoPrt`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NacCnpAnt`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NacEdAnt`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
