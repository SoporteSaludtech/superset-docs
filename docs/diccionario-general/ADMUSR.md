# ADMUSR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`AUsrId`** | `char(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AUsrDsc`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrPsw`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AGrpId`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuFecReg`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuFecAct`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`UsuFecVen`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrFecIni`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrDiaExp`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrTip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrBase`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrVlTope`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrIndCj`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrFot`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsPswDel`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AusUsuUni`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrFotB`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrMod`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AusFirUBD`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUSFECINA`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUSDIAINA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUsrImgFi`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`AUSRRED`** | `varchar(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PERFIL`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdmUsrInc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
