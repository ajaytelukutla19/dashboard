def paginate(query, page, limit):
    items = query.paginate(page=page, per_page=limit, error_out=False)
    return {
        'items': items.items,
        'total': items.total
    }
