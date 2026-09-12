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