# Get element using list comprehension
# numbers=[int(input(f"Enter number {i+1}: ")) for i in range(5)]
# print(*numbers)

# Program to read five real numbers and find the average and standard deviation:

# import math
# numbers=[]

# for i in range(5):
#     n=int(input("Enter element: "))
#     numbers.append(n)

# avg=sum(numbers)/len(numbers)
# v=sum((x-avg)**2 for x in numbers)/len(numbers)

# sd=math.sqrt(v)

# print(f"The avf is {avg}")
# print(f"The variance is {v}")
# print(f"The sd is {sd}")

# Program to compute the value of an algebraic expression:

# x = float(input("Enter the value of x: "))
# y = float(input("Enter the value of y: "))

# result = 1 + (x/y) + (x*y) + 2 + (y/x) + (y*x)
# print(f"Result: {result}")

# Program to multiply an integer by 2 using the bitwise operator:

# n=int(input("Enter a number: "))

# r=n<<1
# print(f"Result: {r}")


# Program to divide an integer by 4 using the bitwise operator:

# n=int(input("Enter a number: "))

# r=n>>2
# print(f"Result: {r}")


# Program to exchange values of two variables using bitwise XOR operator:

# a=int(input("Enter first number: "))
# b=int(input("Enter first number: "))

# print(f"before reversing a and b  {a}  {b}")

# a=a^b
# b=a^b
# a=a^b

# print(f"after reversing a and b  {a}  {b}")


# Program to exchange values of two variables using addition and subtraction:

# a=int(input("Enter first number: "))
# b=int(input("Enter first number: "))

# print(f"before reversing a and b  {a}  {b}")

# a=a+b
# b=a-b
# a=a-b

# print(f"after reversing a and b  {a}  {b}")

# Program to check if an integer is even or odd using bitwise operator:

# n=int(input("Enter a number: "))
# if n&1:
#     print("odd")
# else:
#     print("even") 

# Program to find the maximum of three numbers:

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# max_num = max(a, b, c)
# print(f"The maximum number is: {max_num}")


# Program to find the distance between two points on an x-y plane:

# import math

# x1,y1=map(int,input("Enter first coordinates: ").split(","))
# x2,y2=map(int,input("Enter second coordinates: ").split(","))

# distance=math.sqrt((x2-x1)**2+(y2-y1)**2)

# print(f"result {distance}")


# Program to compute the factorial of an integer:

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# n=int(input("Enter a number : "))
# f=fact(n)
# print(f"result:  {f}")


# Program to check whether an integer is prime:

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
    


# x=int(input("Enter a number : "))

# if is_prime(x):
#     print("Prime ")
# else:
#     print("Not prime")


# Program to find prime numbers between two numbers:

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# start=int(input("Enter starting number: "))
# end=int(input("Enter starting number: "))

# for i in range(start,end):
#     if is_prime(i):
#         print(i)
    

# Python function to calculate the sum of digits of a given integer:

# def sum_digit(n):
#     return sum(int(digit) for digit in str(n))

# n=int(input("Enter a number: "))
# print(f"result : {sum_digit(n)}")


# Function to add arbitrary integers:

# def add(*arg):
#     return sum(arg)

# n=int(input("how many numbers: "))
# # list=[]
# # for i in range(n):
# #     x=int(input("Enter numner: "))
# #     list.append(x)

# list=[int(input(f"Enter number {i+1}")) for i in range(n)]
# print(f"result : {add(*list)}")

# Program to check whether a string is a palindrome or not:

# def is_palindrome(str):
#     return str==str[::-1]

# s=input("enter str: ")

# if is_palindrome(s):
#     print("plaindrome")

# Program to delete 'e' from the end of a string and add 'en':


# def modify_string(s):
#     if len(s)<3:
#         return s
#     if s.endswith('e'):
#         s=s[:-1]
#     return s+'en'

# s=input("enter a str: ")
# print(f"result: {modify_string(s)}")


# Program to create two separate lists for strings and integers from a mixed list:

# def sep_list(list):
#     interges=[x for x in list if isinstance(x,int)]
#     strings=[x for x in list if isinstance(x,str)]
#     return strings,interges

# list=["shuja",10,"shadab",20]

# s,i=sep_list(list)

# print(s)
# print(i)


# Program to sort words in alphabetical order:

# def sort_Word(s):
#     words=s.split()
#     words.sort()
#     return ' '.join(words)

# string=input("Enter a sentence: ")
# print(sort_Word(string))

# Program to transfer even and odd integers into two different lists:


# def sep_list(list):
#     even=[x for x in list if x%2==0]
#     odd=[x for x in list if x%2!=0]
#     return even,odd

# list=[2,3,4,5,6,70]

# print(sep_list(list))

# Program to find the second largest number in a list and its index:

# def second_largest(lst):
#     l=list(set(lst))
#     l.sort()
#     sl=l[-2]
#     indices=[i for i,x in enumerate(lst) if x==sl]
#     return sl,indices

# numbers=[int(input(f"Enter number: {i+1} ")) for i in range(5)]
# print(second_largest(numbers))

# Create a list of tuples with the first element as the number and second as its square:

# def tupleslist(n):
#     return [(i,i**2) for i in range(1,n+1)]

# n=int(input("enter range: "))

# print(tupleslist(n))


# Program to find the element occurring an odd number of times in a list:

# def odd_times(lst):
#     for i in lst:
#         if lst.count(i)%2!=0:
#             return i
        
# l=[1,2,2,2,1]

# print(odd_times(l))


# def max_term(lst):
#     return max(len(i) for i in lst)

# l=["shuja","yusuf","shadab"]
# print(max_term(l))

# Program to find the repeated items of a tuple:

# def repeated_tpl(l):
#     ri=set([x for x in l if l.count(x)>1])
#     return ri

# l=(1,12,2,1,2,3,3,)

# print(repeated_tpl(l))

# index postion

# l=[1,2,1,3,4]
# print(l.index(3),l.count(1))

# Program to count the words in a line of text:
# def count_words(line):
#     words=line.split()
#     return len(words)

# s=input("Enter a line: ")
# print(count_words(s))

# Program to count the number of sentences, words, and the word with maximum occurrence:

# import re

# def analyse_text(text):
#     sentences=re.split(r'[!.?]',text)
#     num_sen=len([s for s in sentences if s.strip()])

#     words=re.findall(r'\w+',text.lower())
#     num_words=len(words)

#     word_counts={}
#     for word in words:
#         word_counts[word]=word_counts.get(word,0)+1

#     most_common_word=max(word_counts,key=word_counts.get)
#     max_occurence=word_counts[most_common_word]

#     return num_sen,num_words,max_occurence

# string=input("Enter text to analyse= ")
# s,w,o=analyse_text(string)

# print(f"result: {s,w,o}")


# Program to count frequency of each character in a line of text:


# def freq_char(text):
#     cf={}

#     for char in text:
        
#         if char in cf:
#             cf[char]+=1
#         elif char==' ':
#             continue
#         else:
#             cf[char]=1
    

#     return cf

# t=input("Enter the text: ")

# d=freq_char(t)

# print("Freq is ",d)


# Program to find the character with the maximum count in a line of text:

# def freq_char(text):
#     cf={}

#     for char in text:
        
#         if char in cf:
#             cf[char]+=1
#         elif char==' ':
#             continue
#         else:
#             cf[char]=1
        
#         max_freq=max(cf,key=cf.get)
    

#     return max_freq

# t=input("Enter the text: ")

# d=freq_char(t)

# print("the character that occurs most is  ",d)

# from collections import Counter

# def cf(text):
#     chf={}

#     frq=Counter(text)
#     max_frq=max(frq,frq.get)
    
#     return chf,max_frq

# import string 

# def is_pangram(sentence):

#     sentence=sentence.lower().replace(" ","")

#     aplhabet_in_sentence=set(sentence)

#     all_alphabet=set(string.ascii_lowercase)

#     return all_alphabet.issubset(aplhabet_in_sentence)

# t=input("Enter the sentence: ")

# if is_pangram(t):
#     print("Is pangram ")



# def count_digi_alphabet(text):
#     digit=sum(x.isdigit() for x in text)
#     alph=sum(x.isalpha() for x in text)

#     return digit,alph



# s=input("enter a string: ")
# print(count_digi_alphabet(s))


# Program to count the number of lines, words, characters, alphabets, and digits in a file:

# import re

# def count_all(file):
#     with open(file,'r') as f:
#         text=f.read()

#     lines=re.split(r'[.!?]',text)

#     words=text.split()
#     char=len(text)
#     a=sum(x.isalpha() for x in text)
#     d=sum(x.isdigit() for x in text)

#     return len(lines),len(words),char,a,d


# filep=input("Enter file path: ")

# print(count_all(filep))


# 1. Program to count each character in a text and find the character with the maximum occurrences:


# def char_count(text):
#     cf={}
#     for char in text:
#         if char in cf:
#             cf[char]+=1
#         else:
#             cf[char]=1

#     max_occ=max(cf,key=cf.get)

#     return cf,max_occ

# s=input("Enter a stirng: ")

# d,c=char_count(s)

# print("Char counts: ")
# for char,count in d.items():
#     print(f"{char} : {count} ")

# print(f"The max char count char is : {c}")

# def create_subset(uset):
#     sorted_list=sorted(uset)
#     hf=len(sorted_list)//2

#     s1=set(sorted_list[:hf])
#     s2=set(sorted_list[hf:])

#     return s1,s2


# ui=input("Enter the elements: ")

# us={x for x in ui.split()}

# if len(ui)%2==0:
#     print("Not even entry ")
# else:
#     s1,s2=create_subset(us)
#     print(s1,s2)

# def read_and_merge(f1,f2,final):
#     with open(f1,'r') as f1:
#         content=f1.read()

#     with open(f2,'r') as f2:
#         content2=f2.read()

#     hf1=len(content)//2
#     hf2=len(content2)//2
#     with open(final,'w') as f:
#         f.write(content[:hf1])
#         f.write(content[hf2:])


# def sp_list(list):
#     strng=[x for x in list if isinstance(x,str)]
#     intr=[x for x in list if isinstance(x,int)]
#     return strng,intr

# mixed=["shuja",43,"ashif",89]
# s,i=sp_list(mixed)

# print(s,i)


# def snd_l(lstt):
#     lst=list(set(lstt))
#     lst.sort()
#     sle=lst[-2]
#     i=[i for i, x in enumerate(lst) if x==sle]
#     return sle,i
# x=[2,5,6,9,20,10,3,3,4,5]
# s,i=snd_l(x)
# print(s,i)

# sort acording to length 

# def sort_len(lst):
#     return sorted(lst,key=len)

# x=["shuja","aqsa","ammi"]

# print(sort_len(x))


# repeared items

# def repeated(lst):
#     r=set([x for x in lst if lst.count(x)>1])
#     return r

# x=[1,1,1,2,2,2,4,5,5,6]

# print(repeated(x))


# len of words

# def count_words(stng):
#     words=stng.split()
#     return len(words)

# x="shuja ia a good bou"

# print(count_words(x))

# from collections import Counter

# def count_words(line):
#     words=line.split()
#     f=Counter(words)
#     return max(f,key=f.get)

# x="shuja shuja is a good boy"
# print(count_words(x))

