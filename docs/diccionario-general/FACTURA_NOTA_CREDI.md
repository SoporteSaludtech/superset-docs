# FACTURA_NOTA_CREDI

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`tipoDocumento`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`numeroFactura`** | `varchar(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`matipdoc`** | `int` | SI | Campo transaccional de Hosvital HIS |
|  | **`sedeFactura`** | `varchar(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`puntoEmision`** | `varchar(7)` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaFactura`** | `datetime` | NO | Campo transaccional de Hosvital HIS |
|  | **`numeroIdPaciente`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoIdPaciente`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`nombrePaciente`** | `varchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`numIdResponsable`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoIdResponsable`** | `varchar(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`nombreResponsable`** | `varchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorObligaRespons`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`saldoResponsable`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`nombreAsegurador`** | `varchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`numeroIdAsegurador`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorObligaAsegura`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`saldoAsegurador`** | `decimal(19,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoNota`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`valorNotaAplica`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`codigoDocumento`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`codigoContrato`** | `char(13)` | NO | Campo transaccional de Hosvital HIS |
|  | **`estado`** | `char(1)` | NO | Campo transaccional de Hosvital HIS |
|  | **`docContable`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`numeroNota`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `varchar(15)` | SI | Campo transaccional de Hosvital HIS |
|  | **`mcdpto`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaNota`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaRegistro`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`usuarioCreacion`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`docAnulacion`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`numeroDocAnulacion`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`sedeAnulacion`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaAnulacion`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`usuarioAnulacion`** | `varchar(100)` | SI | Campo transaccional de Hosvital HIS |
|  | **`puntoEmisionAnulac`** | `varchar(17)` | SI | Campo transaccional de Hosvital HIS |
|  | **`observacion`** | `varchar(300)` | SI | Campo transaccional de Hosvital HIS |
|  | **`cuentaCxC`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
