# HCANTE1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTIPDOC`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISCSEC`** | `decimal(11,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ANTTIPCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ANTAYUCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ANTCODHC1`** | `varchar(40)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ANTNIEGO`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTESTCLI`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTESTVE`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTCOM`** | `varchar(120)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ANTH1FEC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
| 🔑 | **`AntVncFm1`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`AntObser`** | `varchar(4000)` | SI | Campo transaccional de Hosvital HIS |
