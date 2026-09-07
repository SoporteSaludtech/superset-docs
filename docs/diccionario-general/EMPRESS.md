# EMPRESS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MEcntr`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`EmpDsc`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MENNid`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MEDire`** | `char(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MeTele`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MESIGLA`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ORGCOD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EmpPrv`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodAse`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MEPubKey`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
