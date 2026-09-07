# ABONOS1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABODOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ABONUM`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AboCnsPgo`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`AboCtaCte`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboNomAut`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CodPago`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboNroAut`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboCodBan`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABONumPgo`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOValPgo`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOValPgoF`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABoNroCon`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboNrRCmp`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboUsTra`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboTurCod`** | `decimal(12,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboConTot`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboUCscCo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AboAnCon`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ABOFORPAG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
