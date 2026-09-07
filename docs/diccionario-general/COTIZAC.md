# COTIZAC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CotNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CotFch`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`TranApl`** | `char(16)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotDiaVld`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotSolNro`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPrvPlz`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPrvCod`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotPrvRaz`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotCupCre`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotUltCns`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotVlrNet`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CotMsUser`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
