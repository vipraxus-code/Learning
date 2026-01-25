user_input = int(input("Enter number so the program can analyze it: "))

def analyze_number(number):
    return {
        "positive": number > 0,
        "even": number % 2 == 0,
        "digits": len(str(abs(number)))
    }

print(analyze_number(user_input))