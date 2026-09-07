# DOCUCONA

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EmpCodA`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DocCodA`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`DocDscA`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocSigA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocTranApA`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocCscEmA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocCscLA`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DocAplA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
