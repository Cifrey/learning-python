# 2D Collections

# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print(groceries[0][2])
# Si sólo ponemos [0], imprime toda la posición 0 de groceries (fruits) entera.
# Si ponemos dos corchetes, por ejemplo: [0][2], imprime de la posición 0 de groceries
# que es fruits, la posición 2 de dentro, banana.

# Se puede escribir también de esta manera: 

# groceries = [["apple", "orange", "banana", "coconut"],
#             ["celery", "carrots", "potatoes"],
#             ["chicken", "fish", "turkey"]]

# # print(groceries[0][0])

# for collection in groceries:
#     for food in collection:
#       print(food, end=" ")
#     print()

##############################################

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for rows in num_pad:
    for number in rows:
        print(number, end=" ")
    print()