# HCCOM515

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCod`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCPrcCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HCONSIC`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`SDEMANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SDEMSIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SDESOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SESQANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SESQSIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SESQOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRAAANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRAASIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRAOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRADANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRADSIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRADOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRASANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRASSIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRSOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SIMPANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SIMPSIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SIMPOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRAPANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRAPSIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`STRAPOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SNIVESC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCOEINT`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SATEANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SATESIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SATEOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SHABANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SHABSIN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SHABOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SESPSOL`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMOTREM`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SRES`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCANUNO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCANDOS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCATUNO`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SCATDOS`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOBSRES`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SOTRPAT`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SALTCOINT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMEMGENO`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMEMGENH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SMEMGENA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SRETMENO`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SRETMENH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SRETMENA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
