import pandas as pd

# load original file
df = pd.read_csv("data/orders_fixed.csv")

success_orders = (df['status'] == 'success').sum()
refunded_orders = (df['status'] == 'refunded').sum()

total_relevant_orders = success_orders + refunded_orders

print(f"success_orders: {success_orders}")
print(f"refunded_orders: {refunded_orders}")
print(f"total_relevant_orders: {total_relevant_orders}")

refund_rate = (
    refunded_orders / total_relevant_orders * 100
    if total_relevant_orders > 0
    else 0
)

print(f"Refund rate: {refund_rate:.2f}%")