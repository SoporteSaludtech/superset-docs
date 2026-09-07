# PrefeVi

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PreDoc`** | `numeric(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PreDocVa`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreForDo`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreFecDoc`** | `date` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreCodPre`** | `numeric(5,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreObser`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreCodMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreEsp`** | `numeric(3,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Prefec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
