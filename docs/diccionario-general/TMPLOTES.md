# TMPLOTES

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`TLEmpCod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TLMSReso`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TLBodega`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TLCodLot`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TLPrvCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TLBltNro`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TLBltAno`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TLBltMes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TLLotCns`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`TLLotCan`** | `money` | SI | Campo transaccional de Hosvital HIS |
