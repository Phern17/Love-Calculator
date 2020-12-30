# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_name = name1 + name2
lower_name = combine_name.lower()

T = lower_name.count('t')
R = lower_name.count('r')
U = lower_name.count('u')
E = lower_name.count('e')

L = lower_name.count('l')
O = lower_name.count('o')
V = lower_name.count('v')

front_num = T + R + U + E
back_num = L + O + V + E

final_score = int(str(front_num) + str(back_num))

if (final_score >= 40) and (final_score <= 50):
  print(f"Your score is: {final_score}, you are alright together.")

elif (final_score < 10) or (final_score > 90):
  print(f"Your score is: {final_score}, you go together like coke and mentos.")

else:
  print(f"Your score is: {final_score}.")

