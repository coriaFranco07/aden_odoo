# -*- coding: utf-8 -*-
# from odoo import http


# class Programa(http.Controller):
#     @http.route('/programa/programa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/programa/programa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('programa.listing', {
#             'root': '/programa/programa',
#             'objects': http.request.env['programa.programa'].search([]),
#         })

#     @http.route('/programa/programa/objects/<model("programa.programa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('programa.object', {
#             'object': obj
#         })

