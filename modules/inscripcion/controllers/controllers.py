from odoo import http
from odoo.http import request

class InscripcionController(http.Controller):
    @http.route('/api/programa/<int:programa_id>/alumnos', type='http', auth='public', methods=['GET'], csrf=False)
    def get_alumnos_inscritos(self, programa_id, **kwargs):

        programa = request.env['programa.programa'].sudo().browse(programa_id)
        if not programa.exists():
            return request.not_found("El programa con ID %s no existe." % programa_id)

        # Obtuve las inxripciones con relacion al programa
        inscripciones = request.env['inscripcion.inscripcion'].sudo().search([
            ('programa_id', '=', programa_id)
        ])

        # mi respuesta
        alumnos_data = []
        for inscripcion in inscripciones:
            alumno = inscripcion.alumno_id
            pais = alumno.pais_id 
            alumno_data = {
                'nombre': alumno.name,
                'apellido': alumno.apellido,
                'legajo': alumno.nro_legajo,
                'fecha_nacimiento': alumno.fecha_nacimiento.strftime('%Y-%m-%d') if alumno.fecha_nacimiento else None,
                'email': alumno.email,
                'telefono': alumno.telefono,
                'pais': {
                    'id': pais.id,
                    'nombre': pais.name
                } if pais else None
            }
            alumnos_data.append(alumno_data)

        # devuelvo la resp en formt JSON
        return request.make_json_response(alumnos_data)