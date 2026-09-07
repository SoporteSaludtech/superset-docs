# HCNANDX

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
|  | **`PACNANPPL`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PACNANANA`** | `varchar(4000)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PACNANFEC`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`PACNANUSU`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
