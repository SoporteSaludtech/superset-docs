# HCCOMOFT

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
| 🔑 | **`HCOFTCNS`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCOFTTPO`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HCOFTBS`** | `char(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOFTINCA`** | `char(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FTFecha`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FTAgVOjIzq`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FTAgVOjDer`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
