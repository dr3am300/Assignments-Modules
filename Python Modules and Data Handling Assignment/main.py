import mood_responses
welcome_message = "Welcome to the mood response program!"
print(welcome_message)
do_you_want_to_continue = input("Do you want to continue? (YES/NO) ").upper()
if do_you_want_to_continue == "YES":
    mood = input("How are you feeling today? Choose from the following options - [ HAPPY, SAD, ANGRY, RELAXED ]: ").upper()
    print(mood_responses.mood_response(mood))
else:
    print("SHUTTING DOWN PROGRAM")
    count = 0
    while count < 3:
        print("...")
        count += 1
    print("PROGRAM SHUT DOWN")
do_you_want_to_continue = input("Do you want to continue? (YES/NO) ").upper()
if do_you_want_to_continue == "YES":
    mood = input("How are you feeling today? ").upper()
    print(mood_responses.mood_response(mood))
else:
    print("SHUTTING DOWN PROGRAM")
    count = 0
    while count < 3:
        print("...")
        count += 1
    print("PROGRAM SHUT DOWN")
    
    

