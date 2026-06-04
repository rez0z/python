def calculate_order_total(order_amount, delivery_zone):
    if not isinstance(order_amount, (int, float)) or order_amount < 0:
        raise ValueError("Сумма заказа должна быть неотрицательным числом.")
    
    if delivery_zone not in ["city", "region", "country"]:
        raise ValueError("Зона доставки должна быть 'city', 'region' или 'country'.")
    
    original_amount = order_amount
    
    if order_amount >= 5000:
        discount = 0.10
    elif order_amount >= 2000:
        discount = 0.05
    else:
        discount = 0.0
    
    amount_after_discount = order_amount * (1 - discount)
    
    if delivery_zone == "city":
        delivery_cost = 0
    elif delivery_zone == "region":
        delivery_cost = 300
    else:
        delivery_cost = 800
    
    total = amount_after_discount + delivery_cost
    
    print("\n" + "=" * 40)
    print("         РАСЧЁТ СТОИМОСТИ ЗАКАЗА")
    print("=" * 40)
    print(f"Сумма заказа (брутто):  {original_amount:>8.2f} ₽")
    print(f"Скидка: {discount * 100:>5.0f}%")
    print(f"Сумма после скидки:     {amount_after_discount:>8.2f} ₽")
    print(f"Доставка ({delivery_zone}):      {delivery_cost:>8.2f} ₽")
    print("-" * 40)
    print(f"ИТОГО К ОПЛАТЕ:        {total:>8.2f} ₽")
    print("=" * 40 + "\n")
    
    return total

if __name__ == "__main__":
    calculate_order_total(1500, "city")
    calculate_order_total(2500, "region")
    calculate_order_total(6000, "country")
