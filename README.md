Te lo voy a mejorar, pero no solo “bonito”: más claro, profesional y con estructura real de proyecto (lo que se espera en GitHub en equipos serios).

---

# 📌 Sistema de Gestión Colaborativa de Tareas (SGCT)

## 🧠 Descripción

SGCT es una aplicación web diseñada para la gestión de tareas en entornos colaborativos. Permite a múltiples usuarios organizar su trabajo dentro de grupos, facilitando la asignación de tareas, el seguimiento de progreso y la comunicación entre miembros.

El sistema sigue una arquitectura cliente-servidor desacoplada, donde el frontend y el backend operan de forma independiente a través de una API REST.

---

## 🎯 Objetivo

Centralizar la organización del trabajo en equipo mediante:

* Creación de grupos de trabajo
* Gestión de miembros mediante invitaciones
* Administración de tareas
* Organización por categorías
* Asignación de responsabilidades
* Seguimiento de actividad

---

## 🏗️ Stack Tecnológico

### 🔙 Backend

* Django
* Django REST Framework
* PostgreSQL
* Gunicorn
* Whitenoise

### 🎨 Frontend

* React

---

## 📦 Dependencias principales

### Backend

```txt
asgiref==3.11.1
dj-database-url==3.1.2
Django==6.0.3
gunicorn==25.3.0
packaging==26.0
psycopg2-binary==2.9.11
sqlparse==0.5.5
tzdata==2025.3
whitenoise==6.12.0
```

---

## ⚙️ Funcionalidades principales

* 🔐 Registro e inicio de sesión de usuarios
* 👥 Creación y gestión de grupos
* ✉️ Invitación de usuarios por correo electrónico
* 🛡️ Sistema de roles (Administrador / Miembro)
* 📝 CRUD completo de tareas
* 📌 Asignación de tareas a usuarios
* 🗂️ Organización por categorías
* 💬 Comentarios en tareas
* 📊 Registro de actividad (auditoría básica)

---

## 🔐 Control de acceso

El sistema implementa control de acceso basado en:

### 📍 Pertenencia

Un usuario solo puede interactuar con los grupos a los que pertenece.

### 🎭 Roles

**Administrador**

* Invitar usuarios
* Gestionar miembros
* Administrar el grupo

**Miembro**

* Crear y gestionar tareas
* Comentar en tareas

---

## 🔗 Modelo de datos (visión general)

El sistema utiliza un modelo relacional con las siguientes entidades:

* Usuarios
* Grupos
* Usuario-Grupo (relación muchos a muchos con roles)
* Tareas
* Categorías
* Invitaciones
* Comentarios
* Registro de actividad

---

## 🔄 Flujos principales

### 1. Registro

El usuario crea una cuenta en la plataforma.

### 2. Creación de grupo

Un usuario crea un grupo y automáticamente se convierte en administrador.

### 3. Invitación

El administrador invita usuarios mediante correo electrónico.

### 4. Gestión de tareas

Los usuarios crean, asignan y actualizan tareas dentro del grupo.

### 5. Colaboración

Los usuarios interactúan mediante comentarios en tareas.

---

## 🌐 Arquitectura

El sistema está dividido en dos repositorios independientes:

### 🔙 Backend

Responsable de:

* Lógica de negocio
* Autenticación
* Validaciones
* Acceso a datos
* API REST

### 🎨 Frontend

Responsable de:

* Interfaz de usuario
* Consumo de la API
* Experiencia de usuario

---

## 🚀 Instalación y ejecución

### 🔙 Backend

```bash
# Clonar repositorio
git clone <URL_BACKEND>
cd backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

---

### 🎨 Frontend

```bash
# Clonar repositorio
git clone <URL_FRONTEND>
cd frontend

# Instalar dependencias
npm install

# Configurar variables
cp .env.example .env

# Ejecutar aplicación
npm run dev
```

---

## 🛡️ Seguridad

* Autenticación basada en tokens
* Validación de permisos en backend
* Restricción de acceso por grupo
* Protección contra accesos no autorizados

---

## 📊 Escalabilidad

El sistema está preparado para:

* Múltiples usuarios concurrentes
* Múltiples grupos independientes
* Separación clara de responsabilidades (frontend/backend)
* Posible despliegue en entornos cloud

---

## 🧠 Decisiones de diseño

* Uso de relación muchos a muchos con roles → flexibilidad en permisos
* Arquitectura desacoplada → escalabilidad y mantenibilidad
* Control de acceso por pertenencia → seguridad lógica
* Sistema de invitaciones → control de usuarios
* Organización por categorías → mejor estructura de tareas

---

## 👤 Autor

**Diego Alejandro Rodríguez**

---

## 📌 Estado del proyecto

🚧 En desarrollo / Funcional (MVP)

---

