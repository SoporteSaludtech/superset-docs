# MEDPAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtvMed`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`MmeCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedSed`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedCtvIng`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedFchReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedUsuReg`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedNomEnt`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedSld`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedNumLot`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedFchVen`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedRegInv`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MedUCtMov`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
