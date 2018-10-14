# Schreibe eine while Schleife
# sie bricht nur dann ab, wenn der User "yes" oder "no" eingegeben hat
while True:
    answer = raw_input("yes or no")
    if answer not in ["yes", "no"]:

else:
    print("You typed {}".format(answer))



