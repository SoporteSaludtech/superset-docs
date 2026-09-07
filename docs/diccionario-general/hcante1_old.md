# hcante1_old

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `nchar(30)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `nchar(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AntTipCod`** | `nchar(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AntAyuCod`** | `nchar(6)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PriActCod`** | `nchar(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ANTH1FEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
