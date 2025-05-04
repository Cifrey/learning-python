# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

for x in range(1, 11):
    print(x)

# ######################################

for x in reversed(range(1, 11)):
    print(x)

print("HAPPY NEW YEAR")

########################################

for x in range(1, 11, 3):
    print(x)

########################################

credit_card = "1234-5678-9012-3456"

for x in credit_card:                   
    print(x)

# # Esto hace que ponga los números de la variable 1 a 1

########################################

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# 'continue' lo que hace es omitir la anterior línea en el output y continuar hacia la siguiente//

########################################

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

########################################

# Ejemplo anon para entender usos de 'continue':
# for element in elements:
# 	if element == unusable_edge_case:
# 		continue  # skip this element
	
# 	if element == problematic:
# 		if element == fixable:
# 			do-fix-here  # apply fix, element is now compatible with the 30-lines-of-code below
# 		else:
# 			continue  # skip this element
	
# 	do 30-lines-of-code here