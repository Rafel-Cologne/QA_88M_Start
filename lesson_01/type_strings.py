age = 18  # int
price = 19.99  # float
name = "Rafael" # str
is_name = True # bool

fruits = ["apple", "banana"]  # list
coordinates = [1, 2, 3]   # tuple
student = {"name": "Rafael", "age": 18}  # dict
unique_numbers = {1, 2, 9, 6, 9, 2, 0, 1}

print(unique_numbers)

print(type(age))
print(type(price))
print(type(is_name))

s1 = 'Victor'
s2 = "I want to say \"Hi\" "
print(s1 + s2)
s3 = "First string\nSecond string\nThird string"
print(s3)
first_name = "Rafa"
last_name = "Rafael"
full_name  = first_name + " " +  last_name
print(full_name)

long_string = "Hello World "*5  # repeat string
print(long_string)
city= "New York"
temperature = 27.8
text = f"Today in {city} the temperature is {temperature}"
print(text)


word = "Privet"
print(word[0])
print(word[3])
print(word[1:len(word)])  # 0-P, 1-r, 2-i, 3-v, 4-e, 5-t = rivet
print(word[:2]) # Pr
print(word[::-1]) # tevirP
print(word[-1])  # t


text3 = " I like walking"
text4 = "i like walking"

print(text3)
print(text3.lower()) # today in new york the temperature is 27.8
print(text3.upper()) # TODAY IN NEW YORK THE TEMPERATURE IS 27.8
print(text3.title()) # Today In New York The Temperature Is 27.8
print(text4.capitalize())

print(text3.replace)
print(text3.lstrip())
print(text3.rstrip())

print(text3.strip().replace("walking", "hiking"))

text5 = "i like walking"
parts = text5.split(" ")  # ['i', 'like', 'walking']
print(parts)
print(" ,".join(parts))   # i ,like ,walking
print(text5.find("walking")) # 7  - слово "wakling" начинается с 7 символа от начала строки

print("abracadabra".count("a"))
print("3252".isdigit())  # is - это "boolen" и отвечат true или false
print("wawgfg".isalpha())

# 31.08.2026 "Year: 2026, month: 08, day: 31

date_str = '31.08.2026'

day = int(date_str[0:2])
month = int(date_str[3:5])
year = int(date_str[6:10])

date_str = '31.08.2026'
day, month, year = date_str.split(".")
print(f"Year: {year}, month: {month}, day: {day}")
