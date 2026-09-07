# OPENING_BALANCES_DETAIL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
|  | **`cod_product`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`description`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`quantity`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`value_unitary`** | `decimal(17,4)` | NO | Campo transaccional de Hosvital HIS |
|  | **`provider`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`lote`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`date_lote`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`id_opening_balance`** | `varchar(75)` | NO | Campo transaccional de Hosvital HIS |
