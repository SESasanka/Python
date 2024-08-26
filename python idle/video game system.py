def video_game_system():
    GPA = float(input("What is your GPA?"))
    if 3.0 < GPA <= 3.5:
        print("Great, You will get a Wii for your good grades!")
    elif 3.5 < GPA <= 3.8:
        print("Great, You will get a Kinect for your good grades!")
    elif GPA > 3.8:
        print("Great, you will get a Playstation 3!")
    else:
        print("Sorry, you do not get a game system.")
        
