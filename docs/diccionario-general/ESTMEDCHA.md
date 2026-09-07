# ESTMEDCHA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EstCodMed`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`EstFecIni`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`EstMed`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EstIPEqu`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`EstSes`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
