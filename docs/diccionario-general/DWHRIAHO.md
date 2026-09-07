# DWHRIAHO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`H_Factura`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`H_Cedula`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_FchNa`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_GrpoE`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Edad`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_MedidaEd`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Sexo`** | `char(14)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Nombre`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_FIngreso`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_FEgreso`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_MedIng`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_MedEgr`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_ViaIngr`** | `char(24)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Pabellon`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Cama`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Procedie`** | `char(240)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_CausaExt`** | `char(23)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Empresa`** | `char(45)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_DxIngr1`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_DxIngr2`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_DxIngr3`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_DxEgre1`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_DxEgre2`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_DxEgre3`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_CausaMte`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Complica`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_MotSalid`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Incapaci`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Reingres`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_CondUsua`** | `char(23)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_EnfSobre`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_DiasEsta`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Departam`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Municipi`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Barrio`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Regimen`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Afiliado`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_Mes`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_PerAnual`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_CntrCost`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_SubCntrC`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_DescCCos`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`H_DescSCos`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
