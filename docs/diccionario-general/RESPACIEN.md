# RESPACIEN

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
| 🔑 | **`MotConCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PreCodIgo`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResPacRes`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResPacObs`** | `char(240)` | NO | Campo transaccional de Hosvital HIS |
