text="Elsa is a good girl"
text1='captain'
text2='         avengers       '

#basic string function
print(text+text1)
print(text1*5)
print("length of string:",len(text))


print()

#string method
print('----string method----')
text="Elsa is a good girl"
print("uppercase:",text.upper())
print("lowercase:",text.lower())
print("casefold:",text.casefold())
print("capitalized:",text.capitalize())
print("title case:",text.title())

print()

#strip method

print('-----strip method----')
text='       avengers    '
print("stripped:",text.strip())
print("left stripped:",text.lstrip())
print("right stripped:",text.rstrip())

#remove the leading characters "abc"from the string

string="abchello, world!"
stripped_string =string.lstrip("abc")
print(stripped_string)

#output: hello, world!


string="abchello, world!"
stripped_string =string.rstrip("ld!")
print(stripped_string)

#output: hello, wor

print()

print('-----starting and ending and replace string-------')

text="Elsa is a good girl"
print("start with 'Elsa': ",text.startswith("Elsa"))
print("End with 'girl': ",text.endswith("girl"))
print("replaced 'Elsa' with 'anna':",text.replace("Elsa","anna"))

print()

#string slicing
print('----silcing of string-----')
print("First 5 characters:",text[:3])
print("last 6 characters:",text[-3:-1])

print()

#count method
print('----count method----')

print('-----counting string----')
text= "HELLO, HELLO, WORLD"
count= text.count("Hello")
print(count)
print(text.count("o"))

print('----Counting List-----')
number=[1,2,3,2,4,2,5]
count=number.count(2)
print(count)

print('-----Counting Tuple-----')
fruits=("apple","banana","apple","cherry","apple")
count=fruits.count("apple")
print(count)

#find method
print('---find and index method----')
text="hello, world! This is a sample text."
#using the find and index method
fnd = text.find('l')
ind = text.index('l')
print("find method:",fnd)
print("index method:",ind)


#fnd=text.find('e')
#ind=text.index('e')
#print("find method:",fnd)
#print("index method:",ind)

# Using the find and index not available method
print('------- find and index not available -------')
text = "Hello, World! This is a sample text."
fn = text.find('z')
# nd = text.index('z')
print("find method:",fn)
# print("index method:",nd)


print()

# rfind Method
print('-------- rfind And rindex Method ---------')
text = "Hello, World!"
# Using the find and index method
rfnd = text.rfind('l')
rind = text.rindex('l')
print("find method:",rfnd)
print("index method:",rind)

# Using the find and index not available method
print('------- rfind and rindex not available -------')
rfnd = text.find('z')
# rind = text.index('z')
print("find method:",rfnd)
print("index method:",rind)

print()

# String Splitting
print('---------- String Spliting Method----------')
print('----- Splitting using default delimeter----')
text = "Hello, World! This - is a sample text." 
words = text.split()
print(words)
words = text.split("-")
print("Spliting using space:", words)

print()

print('------ Spliting using ","------')
data = "apple,banana,orange,grape"
fruits = data.split(',')
print(fruits)

print()

print('----- Specifying a maximum number of split ------')
sentence = "This is a sample sentence with many words."
words = sentence.split(" ",3)
print(words)

print()

# String Join method
print('----------String Join Method---------')
words = ["Hello", "World", "Python"]
# separator = " "
# result = separator.join(words)
result = " 420 ".join(words)
print(result)

print()

text = "Hello how are you"
separator = "*"
result = separator.join(text)
# result = "+".join(text)
print(result)


# String Checks
print('---------String Check Methods-------------')
text='123456'
text1='Avengers'
text3='Avengers123'
text4='avenger'
text5='AVENGERS'
text6='١٢٣१२३⅒½'
print("Is it isdigit?", text.isdigit())
print("Is it alphabetic?", text1.isalpha())
print("Is it alphanumeric?", text3.isalnum())
print("Is it in lowercase?", text4.islower())
print("Is it in uppercase?", text5.isupper())
print("Is it numeric?", text6.isnumeric())
print("Is it digit?", text6.isdigit())


print()

print('----- Swapcase ------')
text = "Hello, World!"
swapped_text = text.swapcase()
print(swapped_text)
