from odoo import models, fields

class Programa(models.Model):
    _name = 'programa.programa' 
    _description = 'Modelo para gestionar programas'

    name = fields.Char(string='Nombre', required=True) 
    descripcion = fields.Text(string='Descripción') 