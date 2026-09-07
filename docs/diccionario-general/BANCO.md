# BANCO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BANCOD`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`BanNom`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanSuc`** | `char(30)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanDir`** | `char(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanTel`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanFax`** | `char(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanEmail`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanCnt`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanFormChq`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtBCodTrc`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtBNro`** | `char(25)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CtBTipCue`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanCaj`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ConciCod`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`ForTraEle`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanCodNac`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanUsuUni`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`BanIndCIC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
