# VW_Hosvital_CAC

**Tipo de Objeto:** Vista SQL  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
|  | **`Servicio`** | `char(30)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Total_CAC`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Casos_Cancer`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Casos_VIH`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Casos_Renal`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Casos_Huerfanas`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`Porc_Cancer`** | `decimal(10,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Porc_VIH`** | `decimal(10,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Porc_Renal`** | `decimal(10,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Porc_Huerfanas`** | `decimal(10,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`FECHA_ATENCION`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
