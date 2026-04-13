from odoo import http
from odoo.http import request

class MyCRMController(http.Controller):

    @http.route('/api/orders', type='json', auth='user', methods=['POST'])
    def get_orders(self):
        # 获取参数
        state = kwargs.get('state')

        # 当前用户
        user_id = request.env.user.id

        # 构造查询条件
        domain = [('user_id', '=', user_id)]

        if state:
            domain.append(('state', '=', state))

        # 查询数据（带条件 + 分页）
        orders = request.env['my.order'].search(
            domain,
            limit=10,
            offset=0
        )

        result = []
        for order in orders:
            result.append({
                'name': order.name,
                'partner': order.partner_id.name,
                'amount_total': order.amount_total,
                'state': order.state,
            })

        return result
    
    @http.route('/api/create_order', type='json', auth='user', methods=['POST'])
    def create_order(self, **kwargs):

        partner_id = kwargs.get('partner_id')

        order = request.env['my.order'].create({
            'partner_id': partner_id,
        })

        return {
            'status': 'success',
            'order_id': order.id,
            'name': order.name
        }