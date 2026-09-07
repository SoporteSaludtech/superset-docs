# VW_FACTURACION_WIP

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`NUMERO_FACTURA`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`TIPO_FACTURA`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
|  | **`FECHA_INGRESO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_EGRESO`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`VALOR_FACTURA`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`SALDO_CARTERA`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
