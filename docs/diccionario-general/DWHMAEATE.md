# DWHMAEATE

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`No_Factura`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Cedula`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Paciente`** | `char(70)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Fecha_Nac`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`Edad`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`Medida_Eda`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Etareo`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Sexo`** | `char(14)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Departamen`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Municipio`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Barrio`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Regimen`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AFiliado`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Empresa`** | `char(45)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Servicio`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`F_Ingreso`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`F_Egreso`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`Mes_Evalua`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Periodo_An`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`No_Autoriz`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`T_Proced`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`T_Suminis`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`T_Factura`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`T_Subsidio`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`T_Abonos`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`T_Descuent`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`Vlr_CuotaR`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`Vlr_Indige`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`Vlr_Pagado`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`MsUser_Con`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Tipo_Id`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Dias_Estan`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Tipo_Consu`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Diagnostic`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Estado_Sal`** | `char(6)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Primer_Nom`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Segundo_No`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Primer_Ape`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Segundo_Ap`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtroCosto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DescCCosto`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SctrCosto`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`DescSCosto`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
