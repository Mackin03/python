import random

file = open("academe_word_list.txt" , "r" , encoding="utf-8")
list = file.read().split()
file.close()

list.sort()
print("raw word count: "+ str(len(list)))

word_list = []
for word in list:
    if word in word_list: continue
    else:
        word_list.append(word)

print("word count: " + str(len(word_list)))

#for word in word_list:
#    print(word)
#word_pick = random.choice(word_list)

print("Random word Generator")
print("<press any to continue>")
print("<type quit() to exit>")
    
while True:
    quitting = input()
    if quitting == "quit()":
        print("beep . . . boop . . .")
        break
    else:
        print(random.choice(word_list))
        