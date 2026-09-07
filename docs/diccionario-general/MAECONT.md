# MAECONT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MacCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MacDscCon`** | `char(60)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TipConCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`MacObser`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacFrmPag`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipPCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CODBAN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacTipCue`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacNoCue`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacCodIAC`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacCodMat`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacUltCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacCupCre`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacCodPrP`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacEmpPrP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacTipPrP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacDirRad`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacConRad`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`MacAleRad`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
