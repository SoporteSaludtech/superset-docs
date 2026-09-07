# HCCCREGRAF

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
| 🔑 | **`HcCCreCod`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HcCCreDet`** | `char(50)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HcCCreIMG`** | `varbinary` | NO | Campo transaccional de Hosvital HIS |
