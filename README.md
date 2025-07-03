#  Comandos para levantar el proyecto

1. `py -3.10 -m venv venv`
2. `venv\Scripts\activate`
3. `pip install setuptools wheel`
4. `pip install -r requirements.txt`
5. `python odoo-bin -r odoo -w odoo --addons-path=addons,modules -d odoo17`

---

#  Credenciales para iniciar sesión en Odoo

- **Usuario:** `admin`  
- **Contraseña:** `admin`

---

#  Base de datos

- **Nombre:** `odoo17`

##  Roles de base de datos

- **Usuario:** `odoo`  
- **Contraseña:** `odoo`

---

#  Navegación en el panel

En el panel lateral izquierdo se encuentran los módulos:

- **Alumnos**
- **Programa**
- **Inscripción**

![Captura de pantalla](images/modulos.png)

---

##  Módulo: Alumnos

###  Listado de alumnos  
Se pueden ver y eliminar alumnos existentes.

![Captura de pantalla](images/alumnos/list_alumnos.png)

###  Agregar alumno

![Captura de pantalla](images/alumnos/add_alumnos.png)

###  Editar alumno

![Captura de pantalla](images/alumnos/edit_alumnos.png)

---

##  Módulo: Programas

###  Listado de programas  
Permite ver y eliminar programas existentes.

![Captura de pantalla](images/programas/list_programas.png)

###  Agregar programa

![Captura de pantalla](images/programas/add_programas.png)

###  Editar programa

![Captura de pantalla](images/programas/edit_programas.png)

---

##  Módulo: Inscripciones

###  Listado de inscripciones  
Permite ver y eliminar inscripciones.

![Captura de pantalla](images/inscripciones/list_inscripciones.png)

###  Agregar inscripción

![Captura de pantalla](images/inscripciones/add_inscripciones.png)

###  Editar inscripción

![Captura de pantalla](images/inscripciones/edit_inscripciones.png)

---

##  Endpoint API - Método GET

Se puede consultar la lista de alumnos inscritos a un programa específico usando su `id`.

###  Ejemplo: Programa ID = 1 (Programa Odoo)

**URL:**  
`http://localhost:8069/api/programa/1/alumnos`

**Resultado JSON:**

![Captura de pantalla](images/postman/postmanId1.png)

---

###  Ejemplo: Programa ID = 2 (Programa Python)

**URL:**  
`http://localhost:8069/api/programa/2/alumnos`

**Resultado JSON:**

![Captura de pantalla](images/postman/postmanId2.png)
