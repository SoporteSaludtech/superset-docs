# HISDGEP

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
| 🔑 | **`HisGFchAt`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HiGPCtvP`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`HGPESTRB`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPTSUL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPGLMA105`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPGLME105`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPGLIMA20`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPGLIME20`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPBAMA20`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPBAME20`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPPALU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPCHAGA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPPROTE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPSIFI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPVDRMA20`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPVDRME20`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPFOAPL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPFEAPL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPHBMA11G`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPHBMA20S`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPHBME11G`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPHBME20S`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPVMA20R`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPVMA20S`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPVME20R`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPVME20S`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPTCON`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPTMA20`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPTME20`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPCERCO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPCERP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPCERIV`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPAND2`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPAND1`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPVIANT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPARB`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPVME20T`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPVMA20T`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HECOOBS`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPRUAVI`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HESTBGES`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HINFLUDOS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HINFLU`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOVIDDOS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCOVID`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTDAPDOS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTDAP`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGProGst`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
