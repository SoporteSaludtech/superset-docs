# MAETAR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MACODTAR`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MAEDESTAR`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEESTTAR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEOBSTAR`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEFECCRE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MAEFECINA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
