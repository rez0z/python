def calculate_order_total(order_amount, delivery_zone):
    if not isinstance(order_amount, (int, float)) or order_amount < 0:
        raise ValueError("Сумма заказа должна быть неотрицательным числом.")
    
    if delivery_zone == "city":
        delivery_cost = 200
    elif delivery_zone == "region":
        delivery_cost = 500
    elif delivery_zone == "country":
        delivery_cost = 1200
    else:
        print("Неверная зона доставки")
        return None
    
    if order_amount >= 20000:
        discount = 0.15
    elif order_amount >= 10000:
        discount = 0.10
    elif order_amount >= 5000:
        discount = 0.05
    else:
        discount = 0.0
    
    amount_after_discount = order_amount * (1 - discount)
    
    if amount_after_discount >= 15000:
        delivery_cost = 0
    
    total = amount_after_discount + delivery_cost
    
    print("\n" + "=" * 40)
    print("         РАСЧЁТ СТОИМОСТИ ЗАКАЗА")
    print("=" * 40)
    print(f"Сумма заказа:           {order_amount:>8.2f} ₽")
    print(f"Скидка:                 {discount * 100:>5.0f}%")
    print(f"Сумма после скидки:     {amount_after_discount:>8.2f} ₽")
    print(f"Доставка ({delivery_zone}):      {delivery_cost:>8.2f} ₽")
    print("-" * 40)
    print(f"ИТОГО К ОПЛАТЕ:        {total:>8.2f} ₽")
    print("=" * 40 + "\n")
    
    return total

if __name__ == "__main__":
    calculate_order_total(1500, "city")
    calculate_order_total(7500, "region")
    calculate_order_total(12000, "country")
    calculate_order_total(25000, "city")
    calculate_order_total(16000, "region")
    calculate_order_total(1000, "mars")
