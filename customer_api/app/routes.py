from flask import Blueprint, request, jsonify
from app.models import db, Customer, Order
from app.utils import paginate

bp = Blueprint('api', __name__)

@bp.route('/customers', methods=['GET'])
def get_customers():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    customers_query = Customer.query
    paginated = paginate(customers_query, page, limit)

    result = [
        {'id': c.id, 'name': c.name, 'email': c.email}
        for c in paginated['items']
    ]

    return jsonify({
        'page': page,
        'limit': limit,
        'total': paginated['total'],
        'customers': result
    })

@bp.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    return jsonify({
        'id': customer.id,
        'name': customer.name,
        'email': customer.email,
        'order_count': len(customer.orders)
    })
