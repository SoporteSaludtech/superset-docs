# BI_MetasRecaudo

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`MetaId`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`Anio`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`Mes`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`Codigo_EPS`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Nombre_Contrato`** | `varchar(200)` | SI | Campo transaccional de Hosvital HIS |
|  | **`Monto_Meta_Mensual`** | `decimal(18,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`Fecha_Creacion`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
