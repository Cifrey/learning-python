# keyword arguments = an argument preceded by an identifier
# helps with readability
# order of arguments doesn't matter
# 1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, last, first, honorific):
    print(f"{greeting}, {last} {first}-{honorific}")

hello(honorific="san", greeting="Hello", last="Ushiromiya", first="Battler")

# for x in range(1, 11):
#     print(x, end=" ")

print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=34, area=968, first=122, last=343)

print(phone_num)