from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    new_offered_product_ids = fields.Many2many('product.product', 'company_product_rel', 'company_id', 'product_id',
                                               string="New Offered Products")


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    new_offered_product_ids = fields.Many2many('product.product',
                                               'company_product_rel',
                                               'company_id',
                                               'product_id',
                                               string="New Offered Products",
                                               related='company_id.new_offered_product_ids',
                                               readonly=False)
