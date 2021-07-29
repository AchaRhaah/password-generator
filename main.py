import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')',',','*','+']
print("welcome to password generator!")
nr_letters=int(input("how many letters would you like to have in your password\n"))
nr_numbers=int(input("how many numbers would you like to have in your password\n"))
nr_symbols=int(input("how many symbols would you like to have in your password\n"))
password_list=[]
for char in range(1,nr_letters+1):
  random_letter=random.choice(letters)
  password_list+=random_letter
for num in range(1,nr_numbers+1):
  random_number=random.choice(number)
  password_list+=random_number
for char in range(1,nr_symbols+1):
  random_symbols=random.choice(symbols)
  password_list+=random_symbols
random.shuffle(password_list)
password=''
for char in password_list:
  password+=char
print(password)


