user_age = int(input("age: "))
current_year = int(input("what is the current year?: "))
goback = int(input("by how many years do you want to go back?: "))

print("you are", user_age, "year old,", "the current year is", str(current_year) + ".", "you want to go back in time by", goback, "years.")

decision = input("are you sure you want this? (you may not be able to come back to the present...): ")

if decision == "yes":
    decision = True
    print("you are now in the year of", current_year - goback, "and you are", user_age - goback, "year old")

else:
    decision = False
    print("you are still", user_age, "year old and in the year of", str(current_year) + ".")