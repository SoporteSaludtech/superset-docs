# RESCON

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`RESCONEMP`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESCONSED`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESCONCOD`** | `varchar(70)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESCONTDC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESCONDOC`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESCTVGA`** | `varchar(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RESCONDET`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCONOBS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCONFEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCONFIP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCONFFP`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCTVITEM`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCONTRE`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCOTPDE`** | `varchar(5)` | SI | Campo transaccional de Hosvital HIS |
