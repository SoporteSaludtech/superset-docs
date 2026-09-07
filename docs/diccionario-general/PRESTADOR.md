# PRESTADOR

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`PreCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PreCerHab`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreEscCon`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreConTes`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreFConTe`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreCamCom`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreFCamCo`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreCreEnM`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreFCreEn`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreResCiv`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PreFResCi`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TipPreCod`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PreCodRIP`** | `varchar(800)` | SI | Campo transaccional de Hosvital HIS |
|  | **`PRECODENT`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`PREFVIGACR`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`PREACR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
