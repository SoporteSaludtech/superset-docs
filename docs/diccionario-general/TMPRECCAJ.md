# TMPRECCAJ

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NoDocto`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FchApl`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`NoDist`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
