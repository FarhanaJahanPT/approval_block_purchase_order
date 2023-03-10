from odoo import models, fields, api


class ApprovalBlock(models.Model):
    _name = 'approval.block'
    _description = 'Approval Blocks'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    amount_limit = fields.Float(string='Minimum Amount')


class PurchaseApproval(models.Model):

    _inherit = 'purchase.order'

    approval_block_id = fields.Many2one('approval.block',
                                        string='Approval Block',
                                        compute='_compute_amount_total',inverse='_inverse_approval_block_id')

    @api.depends('amount_total')
    def _compute_amount_total(self):
        print(self)
        search = self.env['approval.block'].search([('amount_limit', '<=', self.amount_total)],order='amount_limit desc')
        print(search,'dd')
        self.approval_block_id = False
        if self.amount_total:
            self.approval_block_id = max(search)
            print( max(search),'jjj')
            return self.approval_block_id

    def _inverse_approval_block_id(self):
        search = self.env['approval.block'].search([('amount_limit', '<=', self.amount_total)],
                                                   order='amount_limit desc')
        if self.approval_block_id:
            self.amount_total = max(search)
            return self.amount_total



