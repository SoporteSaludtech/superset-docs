# TEMNIT

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`NitNum`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TFTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TmCtvIng`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NitNomb`** | `char(45)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFFecha`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFNumFac`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTotPro`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTotSum`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTotFac`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVlrSub`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFAbono`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVlrAxUsu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVlrDto`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVLRIVA`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVlrPxUsu`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVlrNPxUs`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFUsuario`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCoPAgo`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFCoMOde`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFormalq`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFVALBAS`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTotSuSI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`TFTotPrSI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
