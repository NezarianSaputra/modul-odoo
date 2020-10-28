from odoo.addons.website_sale.controllers.main import WebsiteSale


class Shop(http.Controllers):
		
	@http.route('/sale/support', type='http', website=True)
		def sale_support(self, **kwargs):
		return "Heloo, World"
    	# controller ini hanya untuk merender form
    	# return request.render('tutorial_controller.sale_support')