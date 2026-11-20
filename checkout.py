def calculate_total(cart, discount_limit=10):
    total = 0
    for name, (price, qty) in cart.items():
        total += price * qty
    if total >= discount_limit:
        discounted = total * 0.9
    else:
        discounted = total
    return round(total, 2), round(discounted, 2)