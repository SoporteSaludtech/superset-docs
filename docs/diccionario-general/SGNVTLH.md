# SGNVTLH

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
| 🔑 | **`HISCHOR`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HISDPRES`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDPRED`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SgVVlrPVC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDTMP`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDFRR`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDFRC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDPUL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDGLA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDPES`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDTAL`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISHIDR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPERS`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPIEL`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISSATO`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISNEUR`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISRESP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVPPulSis`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVPPulMed`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVPPulDia`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVPPulCun`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVPValPCf`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVPValPTr`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVPValPAb`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVPPsoIde`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVGstCar`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNrPupODr`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNrPupOIz`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNrFrMMSD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNrFrMMSI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNrFrMMID`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CNrFrMMII`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVtObs`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisFrCaFe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDPVC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISViaTem`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisTipSV`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISRams`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISRichRa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISEscDoA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTipEsD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPERCEF`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPERABD`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVEstReCo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVEstRRes`** | `char(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPunRC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISResRC`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTFG`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPunSlv`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCadSlv`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPRIC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPRPC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPRIA`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTAPUP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTAPUPI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPATRE`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISAPEOC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISACTMOT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISACTVER`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISREALU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISREALUI`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPAACSI`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPAACDI`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPASESI`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPASEDI`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPERCIN`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPERPAN`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPERCAD`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqTur`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqFcT`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM1`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM2`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM3`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM4`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM5`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM6`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM7`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM8`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM9`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM10`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM11`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM12`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM13`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM14`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM15`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM16`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM17`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM18`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM19`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqAdM20`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqSNTE`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqSNTP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqNVO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqNVOQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqDiu`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqDiQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqDep`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqDeQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqEORQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqVOMQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqTTDe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqTTIz`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqHmDe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqHmIz`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqTMTD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqTMTI`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqULTQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqPeIQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqGaUr`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqEOtr`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqEOtQ`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqPeAb`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqPeCe`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqReGa`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqASCo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`AdLqGLUC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISSOVAL`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISSOAM`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCLAASA`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HESCMAL`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISGLIS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTIPPRO`** | `char(5)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISFECREG`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISPERBRA`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNINDALR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNOSBSGV`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNCODESC`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNPESGR`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDTOF`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDBIS`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDPCP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDEKG`** | `varchar(4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISDCO2`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HGVTIPTOM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVoXD`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SVoXDFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISESCTOT`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISESCVSG`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISESCSG`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISESCAD`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISESCAT`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNVTRNE`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNVTCAP`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNVTODPP`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNGLUCAP`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNHEMCAP`** | `smallmoney` | SI | Campo transaccional de Hosvital HIS |
|  | **`SGNINDPRO`** | `varchar(3000)` | SI | Campo transaccional de Hosvital HIS |
