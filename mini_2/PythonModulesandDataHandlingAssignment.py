
mood = input("How are you feeling today? ")
def mood_responses( mood):
        print("Your mood is", mood,)
        print(mood_responses(mood))
if mood=="Happy":
    print("Remember to smile because smiling helps boost your mood naturally")
elif mood=="Sad":
    print("Please reach out to join a social group going on outings will help you live in the moment.")
elif mood=="Okay":
    print("It's normal to just feel okay, not really happy nor sad. Consider joining our new social groups to learn more about exciting activities in your area....")
else:
    print("Please visit our resource page to find out more about your", mood ,"mood")
try:
     ValueError
except:
     ValueError
finally:
     print("There are many groups available in our social network for people like you that have a", mood, "mood. Please reach out for more information to get linked up right away...")