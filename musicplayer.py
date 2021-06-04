from playsound import playsound
print("\t\t\t\t\tWelcome to Python Music Player")
_music = input("""Select your music from the given Number of List below:
Water
Eye
Exercise\n""")
if _music == "water":
    playsound('C:\\Users\\aarya\\PycharmProjects\\PythonTut\\water.mp3')
elif _music == "eye":
    playsound('C:\\Users\\aarya\\PycharmProjects\\PythonTut\\eye.mp3')
elif _music == "exercise":
    playsound('C:\\Users\\aarya\\PycharmProjects\\PythonTut\\exercise.mp3')
else:
    print("Sorry This Song is not Exist try again!!")