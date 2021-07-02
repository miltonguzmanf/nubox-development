from odoo import fields, http, _
from odoo.http import request
from odoo.addons.website.controllers.main import QueryURL

class WebsiteSaleForm(http.Controller):


    @http.route('/servicios', type="http", auth="public", website=True, methods=["GET"])
    def propiedades(self, **post):

        product_dictionary = request.env['product.template'].sudo().search([('website_published','=',True)])

        vals = {
            'product_template_ids': product_dictionary, 
        }

        return request.render('nubox_website_developments.services_template', vals)
