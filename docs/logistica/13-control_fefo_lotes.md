# Consola Gestión de Inventarios: Control FEFO y Trazabilidad de Lotes

---

## 1. Ficha Técnica General

| Parámetro | Definición Institucional |
| :--- | :--- |
| **Identificador Técnico** | `DASH-LOG-013` |
| **Nombre de la Consola** | Consola Gestión de Inventarios (Control FEFO y Trazabilidad de Lotes) |
| **Área Operativa** | Dirección de Logística, Almacén Central y Servicios Farmacéuticos |
| **Sistema Origen** | HOSVITAL HIS (Módulo de Inventarios y Suministros) |
| **Motor de Base de Datos** | Microsoft SQL Server |
| **Capa Semántica** | `dbo.VW_FARMACIA_STOCK_LOTES` |
| **Herramienta de Visualización** | Intelligy Health |
| **Frecuencia de Actualización** | Turno / 8 Horas (Corte programado en cada cambio de turno asistencial) |
| **Marco Normativo Aplicable** | **Resolución 1403 de 2007 (Ministerio de la Protección Social)**: Modelo de Gestión del Servicio Farmacéutico, condiciones esenciales de almacenamiento, semaforización tricolor y política FEFO obligatoria en Colombia. |

---

## 2. Propósito y Alcance

### 2.1 Propósito
Proporcionar una herramienta analítica y operativa en tiempo real para supervisar y auditar las existencias físicas de medicamentos y dispositivos médicos en la institución, garantizando la aplicación estricta de la política **FEFO** (*First Expired, First Out* / Primero en Vencer, Primero en Salir). Su objetivo central es mitigar el riesgo de merma financiera por vencimiento en anaquel y blindar la seguridad del paciente, asegurando que ningún lote caducado o en cuarentena sea dispensado en los servicios asistenciales.

### 2.2 Alcance
* **Cobertura Espacial:** Aplica a todas las bodegas de almacenamiento de la institución (Almacén General de Suministros, Farmacia Central, y Farmacias Satélites en Urgencias, UCI, Salas de Cirugía y Hospitalización).
* **Población de Datos:** Todos los lotes hospitalarios con existencia física viva (`LoteSalUnd > 0`).
* **Exclusiones:** Registros con saldo en cero, bodegas transitorias de migración/traslado técnico y artículos parametrizados para descarte.

---

## 3. Modelo de Datos y Origen de Información

```mermaid
erDiagram
    LOTESUM }|..|| MAESUM1 : "Cruza por MSRESO"
    LOTESUM }|..|| BODEGAS : "Cruza por BODEGA + EMPCOD"
    LOTESUM {
        varchar BODEGA FK
        varchar MSRESO FK
        varchar LoteCod PK
        varchar EMPCOD FK
        date LoteFVcto
        decimal LoteSalUnd
        decimal LoteCstPrm
        varchar LoteEst
        varchar PrvCod
    }
    MAESUM1 {
        varchar MSRESO PK
        varchar MSNomG
        varchar MsCodCUM
        varchar MsRegInv
        varchar MsAltCos
        decimal MSStMin
        decimal MSStMax
    }
    BODEGAS {
        varchar BODEGA PK
        varchar EMPCOD PK
        varchar BODDESC
    }
    LOTESUM ||--|| VW_FARMACIA_STOCK_LOTES : "Materializa vista analítica";
```
	
### 3.1 Tablas Involucradas en HOSVITAL HIS
* **LOTESUM (Tabla Transaccional de Lotes):** Entidad central de existencias vivas por almacén. Almacena el número de lote (LoteCod), fecha de vencimiento (LoteFVcto), existencia física actual (LoteSalUnd), costo promedio del lote (LoteCstPrm), estado operativo (LoteEst) y NIT del proveedor de adquisición (PrvCod).
* **MAESUM1 (Maestro Institucional de Suministros):** Catálogo maestro de productos. Aporta la descripción genérica/comercial (MSNomG), código CUM asignado por INVIMA (MsCodCUM), Registro Sanitario (MsRegInv) y el flag de medicamento de alto costo (MsAltCos).
* **BODEGAS (Catálogo de Almacenes):** Maestro de bodegas y almacenes institucionales. Se enlaza obligatoriamente mediante clave compuesta (BODEGA y EMPCOD) para evitar duplicaciones cartesianas entre razones sociales o sedes.

### 3.2 DDL de la Vista Semántica

```SQL 

SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
GO

CREATE OR ALTER VIEW dbo.VW_FARMACIA_STOCK_LOTES AS
SELECT 
    -- 1. Identificación de Bodega y Empresa
    LTRIM(RTRIM(l.BODEGA))                                                 AS CODIGO_BODEGA,
    ISNULL(LTRIM(RTRIM(b.BODDESC)), 'BODEGA ' + LTRIM(RTRIM(l.BODEGA)))   AS NOMBRE_BODEGA,

    -- 2. Catálogo Maestro de Suministros
    LTRIM(RTRIM(l.MSRESO))                                                 AS CODIGO_SUMINISTRO,
    ISNULL(LTRIM(RTRIM(s.MSNomG)), 'Sin Nombre Registrado')                AS DESCRIPCION_MEDICAMENTO,
    ISNULL(LTRIM(RTRIM(s.MsCodCUM)), 'SIN_CUM')                            AS CODIGO_CUM,
    ISNULL(LTRIM(RTRIM(s.MsRegInv)), 'SIN_REGISTRO')                       AS REGISTRO_INVIMA,
    CASE WHEN s.MsAltCos = 'S' THEN 'Sí' ELSE 'No' END                      AS ES_ALTO_COSTO,

    -- 3. Trazabilidad de Lote y Proveedor
    LTRIM(RTRIM(l.LoteCod))                                                AS NUMERO_LOTE,
    LTRIM(RTRIM(l.PrvCod))                                                 AS NIT_PROVEEDOR,
    CASE 
        WHEN l.LoteEst = 'A' THEN 'Activo / Dispensable'
        WHEN l.LoteEst = 'B' THEN 'Bloqueado / Cuarentena INVIMA'
        WHEN l.LoteEst = 'I' THEN 'Inactivo / Dado de Baja'
        ELSE 'Estado ' + ISNULL(l.LoteEst, 'N/D')
    END                                                                    AS ESTADO_LOTE,

    -- 4. Vencimientos y Control Centinela (Pasado <= 1900 y Futuro >= 2040)
    CASE 
        WHEN l.LoteFVcto <= '1900-01-01' OR l.LoteFVcto >= '2040-01-01' THEN NULL 
        ELSE l.LoteFVcto 
    END                                                                    AS FECHA_VENCIMIENTO,

    CASE 
        WHEN l.LoteFVcto <= '1900-01-01' OR l.LoteFVcto IS NULL OR l.LoteFVcto >= '2040-01-01' THEN NULL
        ELSE DATEDIFF(DAY, GETDATE(), l.LoteFVcto)
    END                                                                    AS DIAS_PARA_VENCER,

    -- 5. Semáforo FEFO Regulatorio (Res. 1403/2007)
    CASE 
        WHEN l.LoteEst <> 'A' THEN '0. BLOQUEADO / CUARENTENA'
        WHEN l.LoteFVcto <= '1900-01-01' OR l.LoteFVcto IS NULL OR l.LoteFVcto >= '2040-01-01' THEN '5. NO PERECEDERO / SIN VCTO'
        WHEN l.LoteFVcto < CAST(GETDATE() AS DATE) THEN '1. VENCIDO'
        WHEN DATEDIFF(DAY, GETDATE(), l.LoteFVcto) <= 90 THEN '2. ROJO (<= 90 Días)'
        WHEN DATEDIFF(DAY, GETDATE(), l.LoteFVcto) <= 180 THEN '3. AMARILLO (91-180 Días)'
        ELSE '4. VERDE (> 180 Días)'
    END                                                                    AS ESTADO_SEMAFORO_FEFO,

    -- 6. Saldos Físicos y Valorización Económica
    CAST(l.LoteSalUnd AS DECIMAL(18,2))                                    AS SALDO_UNIDADES,
    CAST(ISNULL(l.LoteCstPrm, s.MsCstprm) AS DECIMAL(18,4))                AS COSTO_PROMEDIO_UNITARIO,
    CAST(l.LoteSalUnd * ISNULL(l.LoteCstPrm, s.MsCstprm) AS DECIMAL(18,2)) AS VALOR_TOTAL_LOTE,

    -- 7. Niveles de Reposición
    CAST(ISNULL(s.MSStMin, 0) AS DECIMAL(18,2))                            AS STOCK_MINIMO,
    CAST(ISNULL(s.MSStMax, 0) AS DECIMAL(18,2))                            AS STOCK_MAXIMO

FROM dbo.LOTESUM l
INNER JOIN dbo.MAESUM1 s 
    ON LTRIM(RTRIM(l.MSRESO)) = LTRIM(RTRIM(s.MSRESO))
LEFT JOIN dbo.BODEGAS b 
    ON LTRIM(RTRIM(l.BODEGA)) = LTRIM(RTRIM(b.BODEGA))
    AND l.EMPCOD = b.EMPCOD
WHERE l.LoteSalUnd > 0
  -- Controles de Calidad y Depuración de Outliers / Testing:
  AND l.LoteSalUnd <= 25000
  AND (l.LoteSalUnd * ISNULL(l.LoteCstPrm, s.MsCstprm)) <= 500000000
  AND UPPER(LTRIM(RTRIM(l.LoteCod))) NOT IN ('ANDRES', 'PRUEBA', 'TEST', 'DEMO', '123456')
  AND UPPER(LTRIM(RTRIM(l.LoteCod))) NOT LIKE 'ASDASD%'
  AND UPPER(s.MSNomG) NOT LIKE '%PRUEBA%'
  AND UPPER(s.MSNomG) NOT LIKE '%NO USAR%'
  AND UPPER(ISNULL(b.BODDESC,'')) NOT LIKE '%SOLO PARA TRASLADOS%';
GO;
```

## 4. Reglas y Lógica de Negocio

### Jerarquía Normativa del Semáforo FEFO

| Nivel Semáforo | Condición Técnica | Impacto Asistencial y Operativo |
| :--- | :--- | :--- |
| **`0. BLOQUEADO / CUARENTENA`** | `LoteEst <> 'A'` | Todo lote cuyo estado no sea `'A'` (Activo). Se aísla preventivamente de la dispensación asistencial sin importar su fecha de caducidad. |
| **`1. VENCIDO`** | $\text{FechaVcto} < \text{Hoy}$ | Lote con caducidad rebasada. Genera valores negativos en `DIAS_PARA_VENCER`. Exige acta de baja técnica y traslado físico a estiba de descarte. |
| **`2. ROJO (<= 90 Días)`** | $0 \le \text{Días} \le 90$ | Lote en ventana crítica ($\le 3$ meses). Prioridad número uno de consumo asistencial o activación urgente de canje con el proveedor. |
| **`3. AMARILLO (91-180 Días)`** | $91 \le \text{Días} \le 180$ | Alerta preventiva (ventana de 3 a 6 meses). Se prioriza su traslado hacia servicios de alto flujo (Urgencias u Hospitalización). |
| **`4. VERDE (> 180 Días)`** | $\text{Días} > 180$ | Existencia óptima y segura con vigencia mayor a 6 meses de margen. |
| **`5. NO PERECEDERO / SIN VCTO`** | $\text{Fecha} \le 1900 \lor \ge 2040$ | Dispositivos médicos o insumos sin fecha de caducidad. Devuelven `NULL` en días para no distorsionar promedios. |

### Homologación Multi-Empresa

El cruce entre `LOTESUM` y `BODEGAS` se enlaza estrictamente por la tupla `(BODEGA, EMPCOD)`. Esto previene multiplicaciones cartesianas cuando existen almacenes con el mismo código en diferentes sedes o razones sociales dentro de la misma base de datos.

### Depuración de Registros Atípicos (Data Cleansing)

Para asegurar la confiabilidad financiera en entornos de pruebas y producción, la vista filtra de forma automática:

* Lotes comodín o de pruebas de usuario (`ANDRES`, `PRUEBA`, `TEST`, `ASDASD%`).
* Saldos individuales físicamente irreales ($\gt 25.000$ unidades en un único lote).
* Lotes con valorización desproporcionada ($\gt \$500.000.000$ COP).
* Registros con descripciones maestras marcadas como `"NO USAR"` o bodegas de migración `"SOLO PARA TRASLADOS"`.

---

## 5. Métricas y Lógica Aritmética

### 5.1 Fórmulas Matemáticas

**Días para Vencer ($D_v$):**

$$D_v = \text{DATEDIFF}(\text{DAY}, \text{GETDATE}(), \text{LoteFVcto})$$

**Valorización Económica del Lote ($V_L$):**

$$V_L = \text{SaldoUnidades} \times \text{CostoPromedioUnitario}$$

**Capital Total en Inventario ($K_{total}$):**

$$K_{total} = \sum_{i=1}^{n} V_{L_i}$$

**Capital Crítico en Riesgo de Caducidad ($K_{riesgo}$):**

$$K_{riesgo} = \sum V_L \quad \forall \quad \text{ESTADO\_SEMAFORO\_FEFO} \in \{'1.\text{ VENCIDO}', '2.\text{ ROJO (<= 90 Días)}'\}$$

**Porcentaje de Exposición a Merma ($\% Exp$):**

$$\% Exp = \left( \frac{K_{riesgo}}{K_{total}} \right) \times 100$$

---

## 6. Consultas SQL por cada Chart

### KPI 1: Capital Total en Inventario

```sql
SELECT 
    SUM(VALOR_TOTAL_LOTE) AS VALOR_INVENTARIO_TOTAL
FROM dbo.VW_FARMACIA_STOCK_LOTES;
```
### KPI 2: Saldo Físico Total de Unidades
```SQL 
SELECT 
    	SUM(SALDO_UNIDADES) AS TOTAL_UNIDADES_FISICAS
FROM dbo.VW_FARMACIA_STOCK_LOTES;
```
### KPI 3: Lotes en Riesgo Crítico (Vencidos y $\le 90$ Días)
```SQL
SELECT 
    COUNT(DISTINCT NUMERO_LOTE) AS TOTAL_LOTES_CRITICOS
FROM dbo.VW_FARMACIA_STOCK_LOTES
WHERE ESTADO_SEMAFORO_FEFO IN ('1. VENCIDO', '2. ROJO (<= 90 Días)');
```
### KPI 4: Capital Financiero en Riesgo Crítico
```SQL
SELECT 
    SUM(VALOR_TOTAL_LOTE) AS CAPITAL_EN_RIESGO_COP
FROM dbo.VW_FARMACIA_STOCK_LOTES
WHERE ESTADO_SEMAFORO_FEFO IN ('1. VENCIDO', '2. ROJO (<= 90 Días)');
```
### Chart 5: Gráfico de Barras Apiladas (Composición FEFO por Bodega)
```SQL
SELECT 
    NOMBRE_BODEGA,
    ESTADO_SEMAFORO_FEFO,
    SUM(VALOR_TOTAL_LOTE) AS VALOR_TOTAL
FROM dbo.VW_FARMACIA_STOCK_LOTES
GROUP BY NOMBRE_BODEGA, ESTADO_SEMAFORO_FEFO
ORDER BY SUM(VALOR_TOTAL_LOTE) DESC;
```
### Chart 6: Gráfico de Dona (Distribución del Portafolio de Lotes)
```SQL
SELECT 
    ESTADO_SEMAFORO_FEFO,
    SUM(VALOR_TOTAL_LOTE) AS VALOR_TOTAL
FROM dbo.VW_FARMACIA_STOCK_LOTES
GROUP BY ESTADO_SEMAFORO_FEFO;
```
### Chart 7: Matriz de Control FEFO y Trazabilidad de Lotes (Tabla Operativa)
```SQL
SELECT 
    CODIGO_SUMINISTRO,
    DESCRIPCION_MEDICAMENTO,
    CODIGO_CUM,
    NUMERO_LOTE,
    NOMBRE_BODEGA,
    FECHA_VENCIMIENTO,
    DIAS_PARA_VENCER,
    ESTADO_SEMAFORO_FEFO,
    NIT_PROVEEDOR,
    SUM(SALDO_UNIDADES)   AS SALDO_UNIDADES,
    SUM(VALOR_TOTAL_LOTE) AS VALOR_TOTAL_LOTE
FROM dbo.VW_FARMACIA_STOCK_LOTES
GROUP BY 
    CODIGO_SUMINISTRO,
    DESCRIPCION_MEDICAMENTO,
    CODIGO_CUM,
    NUMERO_LOTE,
    NOMBRE_BODEGA,
    FECHA_VENCIMIENTO,
    DIAS_PARA_VENCER,
    ESTADO_SEMAFORO_FEFO,
    NIT_PROVEEDOR
ORDER BY MIN(DIAS_PARA_VENCER) ASC;
```

### 7.1 Esquema de Distribución en Grilla

El tablero organiza el flujo visual desde indicadores directivos macro hasta la auditoría granular de lotes, distribuido sobre el estándar de 12 columnas:

```text
+---------------------------------------------------------------------------------------------------+
| FILTROS NATIVOS (Panel Lateral Izquierdo)                                                         |
| [Bodega / Almacén]  |  [Semáforo FEFO]  |  [Medicamento / Principio Activo]  |  [Es Alto Costo]   |
+---------------------------------------------------------------------------------------------------+
| FILA 1: TARJETAS DE IMPACTO ECONÓMICO Y VOLUMEN (KPIS)                                            |
| +--------------------+ +--------------------+ +--------------------+ +--------------------+       |
| | KPI 1: Valor Total | | KPI 2: Unidades   | | KPI 3: Lotes Crít. | | KPI 4: Cap. Riesgo |       |
| | 3 Columnas (25%)   | | 3 Columnas (25%)   | | 3 Columnas (25%)   | | 3 Columnas (25%)   |       |
| +--------------------+ +--------------------+ +--------------------+ +--------------------+       |
+---------------------------------------------------------------------------------------------------+
| FILA 2: ANÁLISIS TÁCTICO Y DISTRIBUCIÓN POR SERVICIO                                              |
| +---------------------------------------------------+ +-----------------------------------------+ |
| | Chart 5: Barras Apiladas por Bodega               | | Chart 6: Proporción Global Portafolio   | |
| | 7 Columnas (58% del ancho)                        | | 5 Columnas (42% del ancho)              | |
| +---------------------------------------------------+ +-----------------------------------------+ |
+---------------------------------------------------------------------------------------------------+
| FILA 3: MATRIZ DE CONTROL OPERATIVO Y AUDITORÍA SANITARIA                                         |
| +-----------------------------------------------------------------------------------------------+ |
| | Chart 7: Matriz de Control FEFO y Trazabilidad de Lotes (Tabla Granular)                      | |
| | 12 Columnas (Ancho Completo - 100%)                                                           | |
| +-----------------------------------------------------------------------------------------------+ |
+---------------------------------------------------------------------------------------------------+
```

| Nivel / Sección | Componente | Visualización | Ancho Superset | Propósito Operativo |
| :--- | :--- | :--- | :---: | :--- |
| **Lateral** | Filtros de Control | Filtros nativos | Barra lateral | Segmentación rápida por almacén, medicamento o nivel de riesgo. |
| **Fila 1** | KPI 1: Valor Total | `Big Number` | 3 cols (25%) | Capital total inventariado en moneda local. |
| **Fila 1** | KPI 2: Total Unidades | `Big Number` | 3 cols (25%) | Conteo físico global de unidades en existencia. |
| **Fila 1** | KPI 3: Lotes Críticos | `Big Number` | 3 cols (25%) | Cantidad de lotes vencidos o con vigencia ≤ 90 días. |
| **Fila 1** | KPI 4: Capital en Riesgo | `Big Number` | 3 cols (25%) | Exposición económica sujeta a posible merma asistencial. |
| **Fila 2** | Chart 5: FEFO por Bodega | `Bar Chart` (Stacked) | 7 cols (58%) | Concentración del semáforo normativo por centro de costo. |
| **Fila 2** | Chart 6: Proporción Global | `Donut Chart` | 5 cols (42%) | Distribución porcentual según Resolución 1403 de 2007. |
| **Fila 3** | Chart 7: Matriz de Control | `Table` | 12 cols (100%) | Trazabilidad granular: CUM, Lote, Vencimiento y Proveedor. |

---

### 7.2 Detalle de Configuración por Componente

#### Componentes Tipo KPI (Fila 1)

* **Visualización:** `Big Number` (ECharts).
* **Formato Numérico Monetario (KPI 1 y KPI 4):** `$,.2f` (ej. `$ 1,250,450.00`).
* **Formato Numérico de Conteo (KPI 2 y KPI 3):** `,d` (ej. `45,210`).

#### Chart 5: Composición FEFO por Bodega (Fila 2)

* **Visualización:** `Bar Chart` (ECharts).
* **Eje X:** `NOMBRE_BODEGA`.
* **Dimensión de Agrupación (Series):** `ESTADO_SEMAFORO_FEFO`.
* **Métrica:** `SUM(VALOR_TOTAL_LOTE)`.
* **Configuración Customize:** Stacked: `YES`, Orientación: `Vertical`, Formato Eje Y: `$,.3s`.

#### Chart 6: Proporción Global de Exposición FEFO (Fila 2)

* **Visualización:** `Pie Chart / Donut` (ECharts).
* **Dimensión:** `ESTADO_SEMAFORO_FEFO`.
* **Métrica:** `SUM(VALOR_TOTAL_LOTE)`.
* **Configuración Customize:** Donut: `YES` (Radio interior 50%), Label Type: `Category Name + Percentage`.

#### Chart 7: Matriz de Control FEFO y Trazabilidad (Fila 3)

* **Visualización:** `Table`.
* **Ordenamiento Inicial:** `DIAS_PARA_VENCER` con agregación `MIN` en sentido **Ascendente** (lotes críticos y vencidos al tope).
* **Búsqueda Dinámica:** Activada (`Search box: YES`).
* **Paginación:** 25 registros por página.
* **Formato Condicional Sólido (Pestaña Customize):**

| Orden en Lista | Operador | Valor Objetivo | Esquema de Color | Use gradient | Interpretación en Pantalla |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1ª** | `≤` | `180` | `warning` (Amarillo) | **Desmarcado** | Identifica preventivamente existencias dentro del semestre. |
| **2ª** | `≤` | `90` | `error` o `alert` (Rojo) | **Desmarcado** | Sobreescribe a Rojo sólido los días críticos (≤ 90) y vencidos. |
| **3ª** | `>` | `180` | `success` (Verde) | **Desmarcado** | Pinta de Verde uniforme el inventario con vigencia superior a 180 días. |

#### Paleta Institucional Homologada (JSON Metadata)

Inyectar en las propiedades generales del tablero (*Dashboard Properties -> JSON Metadata*):

```json
{
  "label_colors": {
    "0. BLOQUEADO / CUARENTENA": "#2C3E50",
    "1. VENCIDO": "#78281F",
    "2. ROJO (<= 90 Días)": "#C0392B",
    "3. AMARILLO (91-180 Días)": "#F39C12",
    "4. VERDE (> 180 Días)": "#27AE60",
    "5. NO PERECEDERO / SIN VCTO": "#2980B9"
  }
}
```


