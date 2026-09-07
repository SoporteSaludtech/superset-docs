# HCETENF1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HCETEMP`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCETSED`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCETDOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCETNRO`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETOBS1`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCETUE`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETUR`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETCOPME`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETCOPMR`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETUA`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCETFEC`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETFHIT`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETFHFT`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETFEAN`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCETEST`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCETPBN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCTIPENT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCTIPAC`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
