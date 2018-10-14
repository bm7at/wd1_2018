# Schreibe eine Schleife, die nach einem Input fragt,
# bis man eines der Grundrechenarten eingegeben hat.

# tipp:
# "+" in "+-/*"
# "+" in ["*", "+", "-", "/"]


answer = None
while answer not in ["*", "+", "-", "/"]:
    answer = raw_input("Give me an operator")
    if answer=="yes":
        print "Thank you"

#print ("+" in "+-/*")

#print ("+" in ["*", "+", "-", "/"])

