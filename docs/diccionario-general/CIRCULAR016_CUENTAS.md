# CIRCULAR016_CUENTAS

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `int` | NO | Campo transaccional de Hosvital HIS |
|  | **`formato`** | `varchar(10)` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`tipoDeuda`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`medicionPosterior`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`conceptoDeudor`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`conceptoAcreencia`** | `decimal(18,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipIdDeudrAcreedr`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`idDeudorAcreedor`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`nomDeudorAcreedor`** | `varchar(150)` | SI | Campo transaccional de Hosvital HIS |
|  | **`deterioro`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`abonosRecibidos`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`cuentaInicial`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`cuentaFinal`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
