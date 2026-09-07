# CORTFAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TFCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmCtvIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CorFacCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`CorFchIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CorFchF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CorNumFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CORPLNCOD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
