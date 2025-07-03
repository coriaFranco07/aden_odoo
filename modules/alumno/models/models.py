from odoo import models, fields

class Alumnos(models.Model):
    _name = 'alumnos.alumnos'  
    _description = 'Modelo para gestionar alumnos'

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    nro_legajo = fields.Char(string='Nro. de Legajo', required=True)
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    pais_id = fields.Many2one('res.country', string='País') 


  