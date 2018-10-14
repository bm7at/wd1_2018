small_number = 2
big_number = 50

is_great = 2>50

text = "The number was great" if is_great else "the number was tiny"
text_2 = "The number was {}".format("great" if is_great else "tiny")
print(text)
print(text_2)

