# Python quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's athmosphere?: ",
             "How many bones are in the human body? ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

#################################################

# Versión para Andrés <3
# Python quiz game

questions = ("¿Qué día nos conocimos? ",
             "¿Qué día nos vimos en persona por primera vez? ",
             "¿Cuánto te quiero? ",
             "¿Qué tengo ganas de hacer contigo? ",
             "¿Cómo eres? ")

options = (("A. 9 junio", "B. 28 agosto", "C. 9 julio", "D. 28 julio"),
           ("A. 29 octubre", "B. 28 septiembre", "C. 9 septiembre", "D. 28 octubre"),
           ("A. Mucho", "B. Muchísimo", "C. Infinito y más allá", "D. Un montón"),
           ("A. Besarte", "B. Olerte", "C. Abrazarte", "D. Todas son correctas"),
           ("A. Precioso", "B. Maravilloso", "C. Increíble", "D. Todas son correctas"))

answers = ("C", "B", "C", "D", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Escribe (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("¡CORRECTO! :3")
    else:
        print("Te has equivocado :(")
        print(f"{answers[question_num]} es la respuesta correcta")
    question_num += 1

print("-------------------------")
print("       RESULTADOS        ")
print("-------------------------")

print("Opciones correctas: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Tus opciones:       ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Tu puntuación es:   {score}%")