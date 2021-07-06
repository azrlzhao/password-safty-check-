
#Password security check code
#
# Low-level password requirements:
# 1. The password is composed of simple numbers or letters
# 2. The password length is less than or equal to 8 digits
#
# Intermediate password requirements:
# 1. The password must consist of numbers, letters or special characters (only: ~!@#$%^&*()_=-/,.?<>;:[]{}|\) any two combinations
# 2. The password length cannot be less than 8 digits
#
# Advanced password requirements:
# 1. The password must consist of three combinations of numbers, letters and special characters (only: ~!@#$%^&*()_=-/,.?<>;:[]{}|\)
# 2. The password can only start with a letter
# 3. The password length cannot be less than 16 digits

# apply all the possible letter symbol letters in the array and use for compare
word=r'''~!@#$%^&*()_=-/,.?<>;:[]{}\|'''
number='0123456789'
letter='abcdefghijklmnopqrstuvwxyz'

passward =input("please input your password:")
safty=0
count=0
#check the password should not be zero
while passward.isspace() or len(passward)==0:
    passward =input("passward should not be empty")
#meet the low requirment and set a flag
if len(passward) <=7:
    safty=1
#second set flag
elif 7<=len(passward)<=15:
    safty=2
elif len(passward)>15:
    safty=3
#check if the password has multple combination
for each in passward:
    if each in number:
        count+=1

        break
for each in passward:
    if each in word:
        count+=1

        break

for each in passward:
    if each in letter:
        count+=1
        break


# print  state

if safty==1 and count==1:
    print('low safty ')
elif safty ==3 and count == 3:
    print('high safty')
else:
    print('median safty')



