# INGODOPRI1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`OdoPcCed`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`OdoTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`OdoNuDie`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`OdoCarDi`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`OdoCnDie`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`OdoFoli`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoFec`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoCodTr`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoObse`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoPrVez`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoEmpTra`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoSedTra`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoDocTra`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoCnsTra`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoCoCOPE`** | `char(2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`OdoTtoReal`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
