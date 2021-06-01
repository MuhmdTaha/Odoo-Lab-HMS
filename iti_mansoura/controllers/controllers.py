# -*- coding: utf-8 -*-
# from odoo import http


# class ItiMansoura(http.Controller):
#     @http.route('/iti_mansoura/iti_mansoura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iti_mansoura/iti_mansoura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iti_mansoura.listing', {
#             'root': '/iti_mansoura/iti_mansoura',
#             'objects': http.request.env['iti_mansoura.iti_mansoura'].search([]),
#         })

#     @http.route('/iti_mansoura/iti_mansoura/objects/<model("iti_mansoura.iti_mansoura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iti_mansoura.object', {
#             'object': obj
#         })
