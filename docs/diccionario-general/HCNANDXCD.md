# HCNANDXCD

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
| 🔑 | **`DIANANCOD`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CARNANCOD`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`CARNANFEC`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`CARNANUSU`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
