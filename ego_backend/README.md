# Ego Backend Project

## Descripción
El challenge técnico "Ego Backend" consiste en un backend y desarrollo de APIs que integran un sistema de gestión de concesionarios de vehículos, actividades y financiamiento, con un sistema de reseñas incorporado. Este proyecto se divide en tres aplicaciones principales: Vehicles, Extras, y Reviews.
---
---

## Aplicaciones

### Vehicles App
Gestiona todo lo relacionado con vehículos, concesionarios, servicios y accesorios.

#### Modelos
Dealership: Concesionario de vehículos.
Category: Categorías de vehículos.
Vehicle: Detalles de vehículos.
VehicleDetail: Detalles adicionales de vehículos.
Service: Servicios ofrecidos.
Accessory: Accesorios para vehículos.
#### Funcionalidades
CRUD para Dealership, Category, Vehicle, VehicleDetail, Service, y Accessory.
---

### Extras App
Gestiona actividades y opciones de financiamiento.

#### Modelos
Activity: Actividades del concesionario.
Financing: Opciones de financiamiento.
#### Funcionalidades
Listado de Activities y Financing.
---

### Reviews App
Permite a los usuarios dejar reseñas y calificaciones.

#### Modelo
Review: Reseñas y calificaciones de usuarios.
#### Funcionalidades
CRUD para Reviews.
---
---


# Instalación y ejecución
>Asegúrate de tener Python y Django instalados en tu sistema.

1. Clona el repositorio:

**$**git clone [URL del repositorio]

2. Cambia al directorio del proyecto:

**$**cd ego_backend

3. Instala las dependencias:

**$**pip install -r requirements.txt

4. Ejecutar el Proyecto
- Realiza las migraciones:

**$**python manage.py makemigrations
**$**python manage.py migrate

5. Inicia el servidor de desarrollo:

**$** python manage.py runserver