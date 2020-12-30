# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_T = name1.count('t') + name2.count('t')
num_R = name1.count('r') + name2.count('r')
num_U = name1.count('u') + name2.count('u')
num_E = name1.count('e') + name2.count('e')

num_L = name1.count('l') + name2.count('l')
num_O = name1.count('o') + name2.count('o')
num_V = name1.count('v') + name2.count('v')
num_E = name1.count('e') + name2.count('e')

print(f"T occurs {num_T} times.")
print(f"R occurs {num_R} times.")
print(f"U occurs {num_U} times.")
print(f"E occurs {num_E} times.\n")

print(f"L occurs {num_L} times.")
print(f"O occurs {num_O} times.")
print(f"V occurs {num_V} times.")
print(f"E occurs {num_E} times.")

front_num = num_T + num_R + num_U + num_E
back_num = num_L + num_O + num_V + num_E

string_num = str(front_num) + str(back_num)
final_score = int(string_num)

if (final_score > 40 and final_score < 50):
  print(f"Your score is: {final_score}, you are alright together.")

elif (final_score < 10 or final_score > 90):
  print(f"Your score is: {final_score}, you go together like coke and mentos.")

else:
  print(f"Your score is: {final_score}.")

