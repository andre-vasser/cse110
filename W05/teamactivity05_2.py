grade = float(input("Enter the grade 0-10: "))

if grade >= 9.8:
    letter = "A"
    sign = "+"
elif grade >= 9.3:
    letter = "A"
elif grade >= 9:
    letter = "A"
    sign = "-"
elif grade >= 8.8:
    letter = "B"
    sign = "+"
elif grade >= 8.3:
    letter = "B"
elif grade >+ 8:
    letter = "B"
    sign = "-"
elif grade >= 7.8:
    letter = "C"
    sign = "+"
elif grade >= 7.3:
    letter = "C"
elif grade >= 7:
    letter = "C"
    sign = "-"
elif grade >= 6.8:
    letter = "D"
    sign = "+"
elif grade >= 6.3:
    letter = "D"
elif grade >= 6:
    letter = "D"
    sign = "-"
elif grade >= 3.5:
    letter = "F"
    sign ="+"
elif grade >= 1.3: 
    letter = "F"
else:
    letter = "F"
    sign = "-"
    
print (f"Your grade is {letter}{sign}")