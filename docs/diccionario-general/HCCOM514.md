# HCCOM514

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
| 🔑 | **`HCONVALME`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`HNOMBACOM`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HMOTIVCON`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HANTEFAMI`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HQUIRURG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HENFSOSTE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTRANSHEM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HUSCROAN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTRANSFU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTRASPLRE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HENFADRE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALTNEUR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEVECERE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEPILEPS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTRASMEN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HENFENDO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HENFPARA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HENFAUTO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HENFONCO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCONSPSIC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTRASSUE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALTCOAGU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HNEFROPAT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTRANSHE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOBSERVAC`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGESTACIO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGPARTOS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGABORTO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGCESAREA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HORGASNT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HORGASNTO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCARDPUL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCARDPULO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HABDOMEN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HABDOMEO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOSTEMUS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOSTEMUSO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRENAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRENALO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPSIQUIA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPSIQUIAO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HNEUROL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HNEUROLO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HMETABOL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HMETABOLO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTASISTO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTADIAST`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HFC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HFR`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTALLA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPESO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HESTCON`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPOSINOR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCONDUCC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPOSISED`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HFISPRO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALFIMOM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALMOFIGR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALFIMOMI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALMARCH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HMOVREPE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPROMIE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOBLOCO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HFMOSECO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HMOVCTR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALTEQU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTRDEMO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HSECNEUR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HSISNEROB`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HICC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALTERIT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HREPORZ`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALTFRCA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCIFTEN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HALTCLAFU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXIMARPA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAPAUM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAPAUMO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPALIMUC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXICIA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HLLECAP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXISFAT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXIEQUPE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXIRUFA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXISPAON`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXQUIMIO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HHEMATOBS`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HREPESLE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXISFATI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXISSIBI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXISTOTO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXISSUPL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXISFRERE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRESPIOBS`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HANACAR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPIESEC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXFATI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HAPASUE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXPRURI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXISAMONI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTRANSRE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRENOBS`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HSECAQUE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPISECA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HMANPIE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXIBRADI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HSOMNOL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HPIFRIA`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTAQARR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HANSIRR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HVERBORR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTEMANO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXOFTAL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HEXMUSIMP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HDESHIDR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCICAPIEL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HVAOBSER`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HSISNEEMO`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HIDEDELI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HTRASCOG`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HIRRIANSI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HESPSOLI`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HMOTREMI`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HRESPUES`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HIMPDIAG`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCANDID`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCATEGO`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCANDIDA`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCATEGOR`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HVAOBSERVA`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HDIAMEL`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HENFCORO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HVALVULOP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HANEURISM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HHIPERART`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
