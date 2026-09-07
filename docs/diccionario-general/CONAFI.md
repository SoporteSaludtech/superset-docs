# CONAFI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ConCodAfi`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConDesAfi`** | `char(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConEstAfi`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConFij`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConMaxDia`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConSex`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ConAplEdG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CONMINDIA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConAplPat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConPreOri`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
