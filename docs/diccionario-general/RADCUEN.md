# RADCUEN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadCueDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`RadCueCns`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TrcCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadDocCod`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadVatAnI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadVatIva`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadVatNet`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadUltCns`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadRipPro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadRutRip`** | `char(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadTipPro`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCanDoc`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadEsta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadEstRip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadTipDoc`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadUltRip`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueCT`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueAF`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueUS`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueAD`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueAC`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueAP`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueAH`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueAU`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueAN`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueAM`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadCueAT`** | `varbinary` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmCT`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmAF`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmUS`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmAD`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmAC`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmAP`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmAH`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmAU`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmAN`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmAM`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuNmAT`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExCT`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExAF`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExUS`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExAD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExAC`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExAP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExAH`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExAU`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExAN`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExAM`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaCuExAT`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadPrcRip`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadConReg`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElCT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElAF`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElUS`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElAD`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElAC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElAP`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElAH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElAU`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElAN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElAM`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RaRiElAT`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadObsAnu`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadUsuAnu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadEstAnu`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadFchAnu`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`RadTipPro1`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
