# PROVEEDOR1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TipPCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCupCre`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCon`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCrgCon`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvNoCue`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvTipCue`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvFchUlC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvFrmPag`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CODBAN`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCodIAC`** | `char(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvNoAutF`** | `char(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvFchVnF`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvCodMat`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRVCLC2`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRVCLC1`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRVCOMUN`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRVTRNSIS`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRVCODCLA`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvNumCoE`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PrvIndCoE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRVTRNSID`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TrcCodTit`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
