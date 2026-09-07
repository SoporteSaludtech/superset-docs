# AJSCSTPRO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AjsCstCon`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MSRESO`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AjsVlrSug`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AjsVlrDef`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AjsCstFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AjsCstUsr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
