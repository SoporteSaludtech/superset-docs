# HCCOM516

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
| 🔑 | **`HCONPRVI`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HEVALENCO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEVALENCS`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAGVSLJOD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAGVSLJOI`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAGVSLJVB`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAGVSCEOD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAGVSCEOI`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAGVSCEVB`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPCRRFDAF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTIVISMON`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAPPLHOR`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAPPLVER`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HESRESGSR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HESABPCAO`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCMCNESAB`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HFNSECNNO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPORVISPRO`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPOLICNOR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALTVISMES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HASCREDES`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRENTM5SG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPRAFEVIS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HLAGAFVIS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HDIPLOPIA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPHORIAP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HNISTAGMU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOFTALMOD`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOFTALMOI`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOFTALMOB`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAFACPSEU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAFACOBSE`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HFECULCVS`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGAFAS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGAFTIPUS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HLENCONT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HLENTTUSO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTIEMPO`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCIRREFRA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCIRREFOB`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HNISFTVDC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOTDFVSBI`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HENFPRNFJ`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HESPSOLIC`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HMOTRMI`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRESPUEST`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HASPIRAN1`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCATEGO1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HASPIRAN2`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCATEGO2`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCATOBRS`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAGUVISC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPREFUS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALTCOI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALTCOD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAFECTRA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HMOBEXT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HORBITA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCRISTAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRETINA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCORNEA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
