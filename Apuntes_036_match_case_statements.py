# Match-case statements (switch): an alternative to using many 'elif' statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

# Insted of this:
def day_of_week(day):
    if day == 1:
        return "It's Sunday"
    elif day == 2:
        return "It's Monday"
    elif day == 3:
        return "It's Tuesday"
    elif day == 4:
        return "It's Wednesday"
    elif day == 5:
        return "It's Thursday"
    elif day == 6:
        return "It's Friday"
    elif day == 7:
        return "It's Saturday"
    else:
        return "Not a valid day"
    
print(day_of_week(7))

# Do this:
def day_of_week(day):
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return "It's Friday"
        case 7:
            return "It's Saturday"
        case _:
            return "Not a valid day"
    
print(day_of_week(5))

# Shorter version
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
    
print(is_weekend("Monday"))