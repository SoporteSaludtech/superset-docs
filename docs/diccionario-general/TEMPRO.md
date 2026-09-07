# TEMPRO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NitNum`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmCtvIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ProAgCod`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CodiPr`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TemSoatP`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodiCC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipPro`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ProcCl`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CanPro`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`VaUnPr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`VaToPr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TempMed`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`vTFHoMe`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`vTFHoAn`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`vTFDeSa`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`vTFMate`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`vTFHoAy`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`vTFHoPe`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`vTFinte`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`vTFintu`** | `money` | SI | Campo transaccional de Hosvital HIS |
