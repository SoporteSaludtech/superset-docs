# ADGLOSAS3

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MPNFac`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MATipDoc`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloCtvo`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloAnuEmp`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloAnuSed`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloAnuDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`GloAnuNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`GloAnuTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloAnuUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloAnuFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloPrfRel`** | `char(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`GloUsuRel`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
