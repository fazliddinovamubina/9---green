""" tashqi kutubxonalar """
""" datetime """
# 
# 
import datetime 
# 
# print(datetime.datetime.now())
# # hozir = datetime.datetime.now()
# print(hozir.year)
# print(hozir.month)
# print(hozir.weekday())
# print(hozir.day)
# print(hozir)
# print(hozir.hour)
# print(hozir.minute)
# print(hozir.second)
# print(hozir.microsecond)
# """
# 
# link -> https://docs.python.org/3/library/datetime.html
# link -> https://www.w3schools.com/python/python_datetime.asp
# 
# """
# 
# print(hozir.strftime("%A"))
# print(hozir.strftime("%B"))
# print(hozir.strftime("%w"))
# print(hozir.strftime("%b"))
# print(hozir.strftime("%y"))
# print(f"sana: {hozir.strftime(" %A  %d %B  %Y year  ")}")
# print(f"bugun sana: {hozir.strftime(" %d-%m-%Y   ")}")
# """ """
# sanadan sanani ayirish
# bugun = datetime.date.today()
# ramazon = datetime.date(2025, 3, 1)
# print(ramazon-bugun)
# vaqtdan vaqtni ayirish 
# bugun1 = datetime.datetime.now()
# ramazon1 = datetime.datetime(2025,3,1,00,00,1)
# print(bugun1)
# print(ramazon1)
# farq = ramazon1-bugun1
# print(farq)
# print(farq.days)
# """   """
# t_sana = datetime.datetime(2021,  1,  18,  3,  0,  0)
# print(t_sana )
# print(t_sana + datetime.timedelta(days=20, hours=8))
# SIZ TUGILGANINGIZGA 15 YIL UU 20 KUN BOLDI 

# yil=int(input("tugilgan yilingizni kiriting: "))
# kun=int(input("tugilgan kuningizni kiriting: "))













# import datetime 

# def otgan_kunlar(yil:int,oy:int,kun:int)->str:
#     """ yashab otgan vaqtingizni yil va kun hisobida hisoblab beruvchi funksiya. 
    
#     year - tugilgan yil
#     moth - tugilgan oy
#     day  - kun 

#     9 Green sinfi bilan yasalgan fuksiya(06-02-2025)

#     """

#     t_yil  = yil # tugilgan yil
#     t_oy   = oy  # tugilgan oy 
#     t_kun  = kun # tugilgan kun 
#     t_sana = datetime.date( yil, oy, kun ) # tugilgan sana
#     bugun  = datetime.date.today()         # bugungi sana 

#     if (bugun-t_sana).days <= 365:         # hali bir yoshga tolmagan chaqaloq uchun
#         return f" siz tugilganingizga {(bugun-t_sana).days} kun boldi"
#     elif bugun.month > t_oy:
#         yil = bugun.year - t_yil
#         kun = bugun-datetime.date(bugun.year, t_oy, t_kun)
#         return f" siz tugilganingizga {yil}-yilu, {kun.days} kun boldi"

#     elif bugun.month == t_oy:
#         if bugun.day < t_kun:
#             yil = bugun.year - t_yil - 1
#             kun = bugun-datetime.date(bugun.year - 1, t_oy, t_kun)
#             return f" siz tugilganingizga {yil}-yilu, {kun.days} kun boldi"
        
#         elif bugun.day == t_kun:
#             yil =bugun.year = t_yil
#             return f" siz bugun {yil} yoshga toldingiz. tabriklaymiz ! "
        
#         else:
#             yil = bugun.year - t_yil
#             kun = bugun-datetime.date(bugun.year, t_oy, t_kun)
#             return f" siz tugilganingizga {yil}-yilu, {kun.days} kun boldi"
#     else:
#         yil = bugun.year - t_yil - 1
#         kun = bugun-datetime.date(bugun.year - 1, t_oy, t_kun)
#         return f" siz tugilganingizga {yil}-yilu, {kun.days} kun boldi"



# yil = int(input("tugilgan yilingizni kiriting:  "))
# oy  = int(input("tugilgan oyingizni  kiriting:  "))
# kun = int(input("tugilgan kuningizni kiriting:  "))


# foydalanuvchi = otgan_kunlar( yil, oy, kun )
# print( foydalanuvchi)


# import datetime 
# 
# print(datetime.datetime.now())
# hozir = datetime.datetime.now()
# print(hozir.year)
# print(hozir.month)
# print(hozir.weekday())
# print(hozir.day)
# print(hozir)
# print(hozir.hour)
# print(hozir.minute)
# print(hozir.second)
# print(hozir.microsecond)

# import datetime

 
# bugun = datetime.date.today()

# oy = int(input("Oy kiriting: "))

# sana1 = datetime.date(bugun.year, oy, kun)
# sana2 = datetime.date(bugun.year+1, oy, kun)
# 
# if sana1 > bugun:
    # print(f"Sizning tug'ilgan kuningizga {(sana1-bugun).days} kun qoldi.")
# elif sana1 < bugun:
    # print(f"Sizning tug'ilgan kuningizga {(sana2-bugun).days} kun qoldi.")
# 
# else:
    # print(f"Siz bugun tug'ilgan kuningizni nishonlamoqdasiz")  
    


# kun= int(input("necha kundan keyingi sanani bilmorchisiz  kunni kiriting:  "))
# sana = bugun + datetime.timedelta(days=kun)
# print((sana))


# link -> https://www.w3schools.com/python/module_math.asp
# link -> https://docs.python.org/3/library/math.html

# """homework"""
 
# import math
# print(math.tan(60))  # raqamning tangensini qaytaradi 
# print(math.sinh(20)) # sonning giperborlik sinusini qaytaradi
# print(math.cosh(33)) # sonning giperbor
# print(math.radians(68)) # daraja qiymatini radianga aylantiradi 
# print(math.atan(22)) #X ning tanjans yoyini qaytarish. Ikkita filial kesilishi mavjud: Biri tasavvur o'qi bo'ylab 1j dan ∞j gacha cho'ziladi. Ikkinchisi tasavvur o'qi bo'ylab -1j dan -∞j gacha cho'ziladi.









"""  RegEx - regular expression"""
import re 


word1= "phyton"
word2= "hello"
word3= "noutbook"

print(re.match("^p....n", word1))
print(re.match("^h...o", word2))
print(re.search("b.ook", word3))

ism= input("ismingizni kiriting:  ")
if re.match("^n",ism):
    print(f" salom{ism} sizning ismingiz n harfi bilan boshlanadi  ")
else:
    print(f"salom {ism}")









# """REGEX SHABLON  ""
# link -> https://docs.python.org/3/howto/regex.html
# link -> https://docs.python.org/3/library/re.html
# link -> https://www.w3schools.com/python/python_regex.asp



shablon="^[+]998[\s]?[0-9]{2}[\s]?[0-9]{3}[\s]?[0-9]{2}[\s]?[0-9]{2}"
tel=  input(" tel kiriting: ")

if re.match(shablon,tel):
    print("telefon  nomeringizni togri kiritdingiz ")
else:
    print("telefon nomerini qayta kiriting!")


matn="""
    nimadur nimadur okokok@gmail.com
    efhierwbgbvbeivuvjbh lalala@gmail.com
    ifhnviuoerhfr4h dsbhvuf@gmail.com

"""

email_andoza= '[^@\t\r\n]+@[^@\t\r\n]+\.[^@\t\r\n]+'
email=re.findall(email_andoza,matn)
print(email)




"""
findall()-- barcha mosliklarni oz ichiga olgan royxatni qaytaradi 
search()--- agar satrning istalgan joyida moslik mavjud bolsa  match obyektini qaytaradi 
"""




































