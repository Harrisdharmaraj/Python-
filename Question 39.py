regular_price = 185
discount_percentage = 0.60
num_fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
num_day_old_loaves = int(input("Enter the number of day-old loaves purchased: "))
amount_fresh_loaves = num_fresh_loaves * regular_price
amount_day_old_loaves = num_day_old_loaves * (regular_price - (regular_price * discount_percentage))
total_amount = amount_fresh_loaves + amount_day_old_loaves
print(f"Regular price: Rs.{regular_price:,.2f}")
print(f"Amount of new loaves: Rs.{amount_fresh_loaves:,.2f}")
print(f"Amount of day-old loaves: Rs.{amount_day_old_loaves:,.2f}")
print(f"Total amount: Rs.{total_amount:,.2f}")









































































