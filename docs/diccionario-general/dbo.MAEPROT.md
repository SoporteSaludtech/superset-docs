# dbo.MAEPROT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PRTCOD`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`PRTTIP`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PRTNOM`** | `varchar(50)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PRTDES`** | `varchar(200)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PRTRIE`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PRTDOC`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRTOBS`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRTUSUCRE`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRTFECCRE`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRTUSUMOD`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRTFECMOD`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
