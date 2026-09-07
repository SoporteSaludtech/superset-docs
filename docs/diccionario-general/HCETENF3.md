# HCETENF3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HCETEMP`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCETDOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCETNRO`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCETCSC`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCETCSCDT`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETSED`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETFOL`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETESTRE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCETPDTD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETPDND`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETCNS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCETOBS2`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCETFCREG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCETCNSIN`** | `decimal(4,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCETFOLEN`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
