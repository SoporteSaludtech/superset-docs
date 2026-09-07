# CAJMEN

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`MCDpto`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CajMenCod`** | `char(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CajMenNom`** | `char(40)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CajMenUsu`** | `char(10)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CajMenBas`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CajMenEst`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CajMenFecC`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CajMenFecM`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CajBenChq`** | `char(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CajMenCP`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CajMenCD`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
