# Guía de Despliegue en Nuevos Clientes: IntelliHealth Analytics & Apache Superset

Esta guía detalla el procedimiento estándar para desplegar la plataforma **IntelliHealth Analytics** en la infraestructura de un cliente nuevo desde cero, garantizando persistencia de datos, persistencia visual de marca (co-branding institucional) y conectividad precompilada hacia motores de bases de datos.

---

## 1. Requisitos Previos de Infraestructura

El servidor o equipo anfitrión (Host) debe contar previamente con:

* **Sistema Operativo:** Windows 10/11 Pro/Enterprise o Windows Server (con WSL2 habilitado), o Linux (Ubuntu 22.04 LTS o superior).
* **Virtualización:** Docker Desktop o Docker Engine con Docker Compose v2.x.
* **Recursos mínimos:**
    * 4 vCPUs
    * 8 GB de memoria RAM (recomendado 16 GB para analítica pesada)
    * 40 GB de almacenamiento disponible en disco (SSD preferiblemente)
* **Red:** Puertos de red habilitados (por defecto: `8088` para la interfaz web de Superset y `5432` interno para metadatos).

---

## 2. Estructura de Directorios del Despliegue

Antes de iniciar los servicios, el directorio raíz del proyecto (`superset-docker/`) debe reflejar la siguiente estructura de carpetas y archivos base:

```text
superset-docker/
├── branding/
│   ├── favicon_intellihealth.png
│   ├── logo_intellihealth.png
│   ├── logo_cliente.png
│   └── tail_js_custom_extra.html
├── docker-compose.yml
├── Dockerfile
└── superset_config.py
```
## 3. Configuración de Componentes Clave

### A. Dockerfile (Blindaje de Drivers de Base de Datos)
Para asegurar que los drivers no se pierdan al destruir o recrear contenedores, se empaquetan en la imagen local mediante compilación:

```dockerfile
FROM apache/superset:latest

USER root

# Instalación de dependencias del sistema y drivers nativos (SQL Server, PostgreSQL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    freetds-dev \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalación fija de librerías Python requeridas para conectores clínicos
RUN pip install --no-cache-dir \
    pymssql \
    psycopg2-binary

USER superset
```

### B. tail_js_custom_extra.html (Inyección Dinámica de Marca)
Ubicado en `./branding/tail_js_custom_extra.html`. Implementa la compatibilidad con las directivas de seguridad CSP de Superset mediante `{{ csp_nonce() }}`:

```html
<script nonce="{{ csp_nonce() }}">
document.addEventListener("DOMContentLoaded", function() {
    const checkLogo = setInterval(() => {
        const logoImg = document.querySelector('header img, .ant-menu img, [class*="ant-image"] img, header a[href*="welcome"] img');
        if (logoImg) {
            logoImg.src = '/static/assets/images/logo_intellihealth.png';
            logoImg.style.height = '38px';
            logoImg.style.width = 'auto';
            logoImg.style.maxWidth = '220px';
            logoImg.style.objectFit = 'contain';
            clearInterval(checkLogo);
        }
    }, 150);
});
</script>
```

### C. Mapeo en docker-compose.yml (Volúmenes Externos)
Asegurar que el bloque global `x-superset-volumes` contenga los mapeos de branding y configuración:

```yaml
x-superset-volumes: &superset-volumes
  - ./branding/tail_js_custom_extra.html:/app/superset/templates/tail_js_custom_extra.html:ro
  - ./branding/logo_intellihealth.png:/app/superset/static/assets/images/logo_intellihealth.png:ro
  - ./branding/favicon_intellihealth.png:/app/superset/static/assets/images/favicon_intellihealth.png:ro
  - ./superset_config.py:/app/pythonpath/superset_config.py:ro
  - superset_home:/app/superset_home
  - db_home:/var/lib/postgresql/data
```
## 4. Proceso de Despliegue Paso a Paso

Ejecuta la siguiente secuencia de comandos en la terminal (**PowerShell** o **Bash**) ubicado dentro de la carpeta raíz del despliegue (`superset-docker`):

### Paso 1: Compilar la Imagen Personalizada
Compila la imagen local para empaquetar de forma fija los drivers nativos y dependencias Python:

```bash
docker compose build
```

---

### Paso 2: Inicializar la Base de Datos de Metadatos
Ejecuta las migraciones estructurales del esquema interno de Superset sobre PostgreSQL:

```bash
docker compose run --rm superset superset db upgrade
```

---

### Paso 3: Crear el Usuario Administrador
Genera la cuenta administrativa principal para el entorno del cliente:

```bash
docker compose run --rm superset superset fab create-admin \
    --username admin \
    --firstname Administrador \
    --lastname IntelliHealth \
    --email soporte@saludtech.com \
    --password "TuClaveSegura2026*"
```

---

### Paso 4: Inicializar Roles y Permisos Base
Carga los roles del sistema, permisos de acceso a métricas y sincronización de seguridad:

```bash
docker compose run --rm superset superset init
```

---

### Paso 5: Despliegue de la Suite
Inicia la totalidad de los contenedores (servidor web, workers, Redis, base de metadatos) en segundo plano:

```bash
docker compose up -d
```
## 5. Verificación y Validación

Una vez desplegados los servicios, realiza las siguientes pruebas de aceptación para asegurar la operatividad del entorno:

| Punto de Control | Acción de Verificación | Resultado Esperado |
| :--- | :--- | :--- |
| **Acceso Web** | Abrir `http://<IP-DEL-SERVIDOR>:8088` en el navegador | Pantalla de inicio de sesión de IntelliHealth Analytics |
| **Branding Persistente** | Iniciar sesión y validar la barra superior | Logotipo corporativo de IntelliHealth cargado correctamente y sin distorsión |
| **Conectividad SQL Server** | Probar conexión en *Settings > Data > Databases* usando `mssql+pymssql://...` | Prueba de conexión (*Test Connection*) exitosa sin errores de driver |
| **Conectividad PostgreSQL** | Probar conexión usando `postgresql+psycopg2://...` | Prueba de conexión (*Test Connection*) exitosa |

---

## 6. Mantenimiento y Ciclo de Vida

Procedimientos operativos estándar para la administración del ciclo de vida de los contenedores:

### Detención y Arranque del Servicio
Para detener los contenedores sin pérdida de datos:
```bash
docker compose down
```

> **Advertencia Crítica:** Nunca utilices la bandera `-v` (`docker compose down -v`) en un ambiente productivo. Este modificador elimina los volúmenes físicos persistentes de PostgreSQL (`db_home`), destruyendo todos los metadatos, conexiones y dashboards configurados.

Para reiniciar o levantar la plataforma nuevamente:
```bash
docker compose up -d
```

---

### Adición de Nuevos Conectores de Bases de Datos
Si el cliente requiere un motor relacional o analítico adicional (por ejemplo: MySQL u Oracle):

1. Modifica el archivo `Dockerfile` agregando el paquete correspondiente en la directiva de instalación de Python (por ejemplo, `mysqlclient` o `cx_Oracle`).
2. Recompila la imagen base para empaquetar el nuevo driver:
   ```bash
   docker compose build
   ```
3. Recrea los contenedores con la imagen actualizada:
   ```bash
   docker compose up -d
   ```
*(La configuración, los dashboards y el branding montados mediante volúmenes externos permanecerán intactos durante todo el proceso).*

## 7. Pasos Posteriores a la Instalación de IntelliHealth

Una vez que los contenedores de Docker estén en ejecución y la suite de Superset se encuentre operativa, ejecute en orden los siguientes pasos de aprovisionamiento en la base de datos y la plataforma:

---

### Paso 1: Credenciales Maestras de Acceso
El acceso inicial a la interfaz web (`http://localhost:8088` o IP del servidor) se realiza con la cuenta administradora configurada en el despliegue:

* **Usuario:** `admin`
* **Contraseña:** `AdminSegura2026*`

---

### Paso 2: Aprovisionamiento de Credenciales en SQL Server
Abra SQL Server Management Studio (SSMS) o una terminal con `sqlcmd` en la instancia del cliente y ejecute el siguiente script para crear el login técnico con acceso exclusivo a la base de datos operativa:

```sql
-- 1. Eliminar cualquier residuo del usuario y recrearlo limpio
IF EXISTS (SELECT 1 FROM sys.server_principals WHERE name = 'Superset')
    DROP LOGIN [Superset];
GO

-- 2. Crear con directivas de complejidad deshabilitadas
CREATE LOGIN [Superset] 
WITH PASSWORD = N'AdminSegura2026X', 
     CHECK_POLICY = OFF, 
     CHECK_EXPIRATION = OFF,
     DEFAULT_DATABASE = [Unificacion_QA];
GO

-- 3. Habilitar permisos de servidor
ALTER LOGIN [Superset] ENABLE;
GRANT CONNECT SQL TO [Superset];
GO

-- 4. Asegurar el mapeo en la base de datos Unificacion_QA
USE [Unificacion_QA];
GO

IF EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'Superset')
    DROP USER [Superset];
GO

CREATE USER [Superset] FOR LOGIN [Superset];
ALTER ROLE [db_owner] ADD MEMBER [Superset];
GRANT CONNECT TO [Superset];
GO
```

### Paso 3: Configuración de la Conexión en Superset

En la consola web de Superset, registre la base de datos de la siguiente manera:

1. Ingrese a **Settings** > **Data: Database Connections** (o presione **+** > **Data** > **Connect database**).
2. Defina el nombre de visualización exacto: `HOSVITAL_HIS`.
3. Ingrese la cadena de conexión en **SQLAlchemy URI**:

```text
mssql+pymssql://Superset:AdminSegura2026*@host.docker.internal:1415/Unificacion_QA
```
4. **Configurar los parámetros de seguridad:**
    * Vaya a la pestaña **Advanced** > **Security** (o **Engine Parameters**).
    * En el campo **Connect Arguments**, inserte el siguiente bloque JSON para prevenir conflictos de negociación SSL/TLS:

    ```json
    {
      "ssl": false
    }
    ```

5. Haga clic en **Test Connection**. Al recibir la confirmación de enlace exitoso, guarde la configuración presionando **Connect** o **Finish**.

---

### Paso 4: Creación de Tablas Complementarias

Establezca conexión sobre la base de datos `Unificacion_QA` a través de SQL Server Management Studio (SSMS) o la utilidad `sqlcmd`, y procese el archivo de definiciones:

* **Script:** `Tabla diagnosticos.sql`
* **Propósito:** Genera y estructura el catálogo maestro de diagnósticos necesario para cruzar morbilidad, causas de egreso y análisis de motivos de consulta.

---

### Paso 5: Despliegue de Vistas Analíticas

Con el fin de asegurar la disponibilidad de los datasets en Apache Superset y mitigar excepciones por referencias inexistentes (`Error 208: Invalid object name`), aplique el consolidado DDL en `Unificacion_QA`:

* **Script:** `Vistas_Para_IntelliHealth.sql`
* **Propósito:** Compila las vistas asistenciales, operativas y logísticas que alimentan los tableros (incluyendo `VW_FARMACIA_STOCK_LOTES`, triage, censo hospitalario y oportunidad de atención).
* **Validación:** Acceda al módulo **Dashboards** en Superset, abra las consolas desplegadas y ejecute **Force refresh** desde el menú contextual (`...`) de los componentes para certificar la visualización de la información.