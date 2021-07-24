import time
#simple contact file using lists and print function

names = []
phone_numbers = []
num = 3

for val  in range(num):
    name = input("Name: \n")
    phone_number = input("Phone Number: \n")

    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print(f"{names[i]}\t\t\t{phone_numbers[i]}\n")


search = input("\n Enter search name: ")
print(f"searching...{time.sleep(10)}\n"
      f"search result:")

if search in names:
    index = names.index(search)
    phone_number = phone_numbers[index]
    print(f"Name: {search}, Phone Number: {phone_number}")

else:
    print("Name Not Found")