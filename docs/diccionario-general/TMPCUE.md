# TMPCUE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TmpEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpCueVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmpCueCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TmpCueNom`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCueNat`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpNoDig`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCueNiv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCntTrm`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpAcuTer`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpCodCap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TmpClsCap`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
