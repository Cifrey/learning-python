# Format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :<(number) = left justify
# :>(number) = right justify
# :^(number) = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator # Si hay números grandes (mil, millón, etc), añade la coma (ex: 1,000)
# Se pueden poner todas las que queramos pero hay que tener cuidado con el orden
# Ejemplo orden: f"{price1:>+10.2f}"

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:+.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")