from odoo import models, fields

class Inscripcion(models.Model):
    _name = 'inscripcion.inscripcion' 
    _description = 'Modelo para gestionar inscripciones'

    alumno_id = fields.Many2one('alumnos.alumnos', string='Alumno', required=True)  
    programa_id = fields.Many2one('programa.programa', string='Programa', required=True)  