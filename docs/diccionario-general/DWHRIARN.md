# DWHRIARN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`P_Factura`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`P_Consec`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`P_Cedula`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Paciente`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_FNacMadr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Edad`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Medida_E`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Etareo`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Departam`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Municipi`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Barrio`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Zona`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Regimen`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_AFiliado`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Empresa`** | `char(45)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Servicio`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_FIngreso`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_FEgreso`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Mes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Anual`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_SemGest`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_ContPren`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_TipoPart`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Anestesi`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_FMteMadr`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_CMteMadr`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_QuienAte`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_FNacBebe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_HNacBebe`** | `char(8)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_SexoBebe`** | `char(14)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_PesoBebe`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_TallaBeb`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Cefalico`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Toraxico`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Apgar1mi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_Apgar5mi`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_CMteBebe`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_FMteBebe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_DxRecNac`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_CtroCost`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_DescCCos`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_SctrCost`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`P_DescSCos`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
