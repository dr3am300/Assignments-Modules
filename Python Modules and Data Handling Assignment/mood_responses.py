def mood_response(mood):
    if mood == "HAPPY":
        return "It's great to see you happy!"   
    elif mood == "SAD":
        return "I'm sorry to hear that you are sad."
    elif mood == "ANGRY":
        return "Take a deep breath 3 times."
    elif mood == "RELAXED":
        return "I'm glad you are relaxed."
    else:
        print("Invalid input. Please choose from the following options - [ HAPPY, SAD, ANGRY, RELAXED ]")
        return mood_response(input("How are you feeling today? Choose from the following options - [ HAPPY, SAD, ANGRY, RELAXED ]: ").upper())
    

    
    
    
    
    

