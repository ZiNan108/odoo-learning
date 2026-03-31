from odoo import models, fields, api

# 1. 扩展Odoo原生客户模型（res.partner），添加一对多订单关联
class ResPartner(models.Model):
    _inherit = 'res.partner'

    order_ids = fields.One2many(
        'my.order',  # 关联的订单模型
        'partner_id',  # 订单模型中关联客户的字段
        string='关联订单'
    )

# 2. 自定义订单模型（必须包含order_line_ids）
class MyOrder(models.Model):
    _name = 'my.order'
    _description = '客户订单'
    _order = 'date_order desc'

    name = fields.Char(string='订单号', required=True, copy=False, readonly=True, default='新建')
    date_order = fields.Datetime(string='订单日期', required=True, default=fields.Datetime.now)
    state = fields.Selection(
        [('draft', '草稿'), ('confirmed', '已确认'), ('done', '已完成')],
        string='状态', default='draft', tracking=True
    )
    amount_total = fields.Float(string='订单总金额', compute='_compute_amount_total', store=True)

    # 关联客户（Many2one）
    partner_id = fields.Many2one(
        'res.partner',
        string='客户',
        required=True,
        ondelete='cascade'
    )
    # 订单明细（One2many，必须有！）
    order_line_ids = fields.One2many(
        'my.order.line',
        'order_id',
        string='订单明细'
    )

    # 自动生成订单号（解决全是"新建"的问题）
    @api.model
    def create(self, vals):
        if vals.get('name', '新建') == '新建':
            vals['name'] = self.env['ir.sequence'].next_by_code('my.order') or '新建'
        return super().create(vals)

    # 计算总金额
    @api.depends('order_line_ids.price_subtotal')
    def _compute_amount_total(self):
        for order in self:
            order.amount_total = sum(line.price_subtotal for line in order.order_line_ids)
    
    # 订单状态按钮
    def action_confirm(self):
        for order in self:
            order.state = 'confirmed'

    def action_done(self):
        for order in self:
            order.state = 'done'

    def action_draft(self):
        for order in self:
            order.state = 'draft'

# 3. 订单明细模型
class MyOrderLine(models.Model):
    _name = 'my.order.line'
    _description = '订单明细'

    product_name = fields.Char(string='产品名称', required=True)
    quantity = fields.Float(string='数量', required=True, default=1.0)
    price_unit = fields.Float(string='单价', required=True)
    price_subtotal = fields.Float(string='小计', compute='_compute_price_subtotal', store=True)

    order_id = fields.Many2one(
        'my.order',
        string='所属订单',
        required=True,
        ondelete='cascade'
    )

    @api.depends('quantity', 'price_unit')
    def _compute_price_subtotal(self):
        for line in self:
            line.price_subtotal = line.quantity * line.price_unit