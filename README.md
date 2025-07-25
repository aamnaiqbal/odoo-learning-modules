# 🎓 Odoo Learning Journey - Custom Modules Development

> **A hands-on learning repository for Odoo development** featuring custom modules, Docker setup, and comprehensive documentation.

This repository documents my journey learning Odoo development by building real-world modules from scratch. Perfect for beginners who want to understand Odoo's architecture and development patterns.

## 🎯 Learning Objectives

- ✅ Understanding Odoo module structure 
- ✅ Creating models with fields and relationships  
- ✅ Building modern views (forms, lists) with proper syntax
- ✅ Setting up security and access controls
- ✅ Docker-based development environment
- ✅ Module installation and testing


## 🐳 Docker Development Environment

Easy setup with Docker Compose including:
- Odoo 17.0
- PostgreSQL database
- Volume mounting for live development
- Secrets management for database passwords

## 🛠️ Development Setup

### Prerequisites
- Docker Desktop
- Git
- Basic Python knowledge

### Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/aamnaiqbal/odoo-learning-modules.git
   cd odoo-learning-modules
   ```

2. **Setup database password**
   ```bash
   echo "your_password_here" > odoo_pg_pass
   ```

3. **Start development environment**
   ```bash
   docker-compose up
   ```

4. **Access Odoo**
   - URL: http://localhost:8069
   - Create database and install custom modules

---

## 📚 Learning Resources Included

## __init__.py
In Odoo, the __init__.py file is used to initialize Python packages and import your module's Python files so that Odoo knows which models, wizards, controllers, or other Python components to load.

---

## __manifest__.py
the metadata file that describes the module.

```bash
{
    'name': 'Hospital Management', #required field
    'version': '1.0.0', #required field
    'category': 'Healthcare',
    'summary': 'Hospital Management System',
    'description': 'A basic hospital management module',
    'author': 'Aamna Iqbal',
    'depends': ['base'], #required field.    The depends field lists the Odoo modules that your module depends on. These must be installed for your module to work correctly.
    'license': 'LGPL-3',
    'data': [],   #required field.  The data field is a list of XML/CSV files that should be loaded when the module is installed.
    'installable': True,
    'application': True,
}
```

---

## 📁 1. models/ Folder
This is where you define the business logic and data structure of your module. Each file here typically contains a Python class inheriting from models.Model.

#### ✅ You define:
New models (tables)

Fields (columns)

Methods (business logic)

Constraints and computed fields

#### 📄 Example Files:
patient.py – defines the patient model

appointment.py – defines appointment logic

doctor.py – defines doctor model

---

## 📁 2. views/ Folder
This folder defines how your data appears in the Odoo UI: form views, list (tree) views, search views, menus, actions, dashboards, etc.

#### ✅ You define:
Form views

List views

Search views

Kanban/calendar views (if needed)

Menus and actions

#### 📄 Example Files:
patient_view.xml

appointment_view.xml

doctor_view.xml

menu.xml

---

## 📁 3. controllers/ Folder
This folder is used if you're building web pages, JSON APIs, or custom endpoints. You’ll only need this if you're:

Building a website

Exposing APIs

Handling custom frontend logic

#### ✅ You define:
HTTP routes

REST API endpoints

Website pages (optional)

Custom JSON responses

---

