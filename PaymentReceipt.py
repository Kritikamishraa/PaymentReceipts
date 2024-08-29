from datetime import datetime #current date and time handle 

def generate_receipt(customer_name, items, prices, quantities, payment_method):
    total_amount = sum(prices[i] * quantities[i] for i in range(len(items)))
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # current date aur time ko format karti hai YYYY-MM-DD HH:MM:SS
    
    receipt = f"""
    ========================= PAYMENT RECEIPT =========================
    Date & Time: {date_time}
    
    Customer Name: {customer_name}
    
    Items Purchased:
    ------------------------------------------------------------------
    Item             Quantity         Price         Total
    ------------------------------------------------------------------"""
    
    for i in range(len(items)):
        item_total = prices[i] * quantities[i]
        receipt += f"\n    {items[i]:<15} {quantities[i]:<15} {prices[i]:<15} {item_total:<15}"
    
    receipt += f"""
    ------------------------------------------------------------------
    Total Amount: {total_amount}
    
    Payment Method: {payment_method}
    ==================================================================
    Thank you for your purchase!
    """
    
    return receipt

# Example usage this
customer_name = "Kritika Mishra"
items = ["Kitkat", "Dairymilk", "Dark Chocolate"]
prices = [0.65, 0.73, 0.98]
quantities = [40, 70, 50]
payment_method = "ATM"

receipt = generate_receipt(customer_name, items, prices, quantities, payment_method)
print(receipt)
