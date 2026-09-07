# RESSEV_X

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResTip`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResDoc`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ResNum`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ResFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResRet`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResTexErr`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResRes`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResXmlSol`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResXmlRes`** | `varchar(2000)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResUsr`** | `varchar(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ResEst`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESTIPEMI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCODCON`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCODNUM`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESCLAACC`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`RESTIPPRO`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`RESNUMAUT`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RESSOLBLO`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
