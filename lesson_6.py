"""if-else"""
# a= 4
# b= 5


# if a > b: # 1- usul 
#     print(a)
# else:
#     print(b)


# son1 = int(input("1-sonni kiriting:"))
# son2 = int(input("2-sonni kiriting:"))


# if son1 > son2 :
#     print(f"{son1} > {son2}")
# elif son1 <son2:
#     print(f"{son1} > {son2}")
# else: 
#     print(f"{son1} = {son2}")


# ism = input("ismingizni kiriting :").lower()

# if ism == "oydina":
#         print("oydina darsda uhlamay otir")
# elif ism == "mubina":
#     print*("mubina tezroq yoz ")
# else:
#      print(f"salom{ism }")





# sonlar= list(range(102,2020))
# for son in sonlar:
#     if 1000 > son :
#         print(son**7)
#     elif 1500< son :
#         print(son-4)


# ismlar = ["ali", "olim", "kamron", "abdulloh", "karim","usmon"]

# for ism in ismlar:
#     if ism == "kamron" :
#         print(f"salom ahvollaring qanday {ism}")
#     elif ism == "karim" :   
#         print(f"salom ahvollaring qanday {ism}" )
#     else:
#         print(f"assalomu aleykum {ism} ")


#3-mashq

# sonlar = [2, 6, -9, 0, 8.5, 21, 65, -34, 43.6, -44, 847, 0, 32, -4]
# print(len(sonlar))
# print(max(sonlar))
# print(min(sonlar))
# print(sonlar[0]+ sonlar[13])
# #4-maqshq
# numbers = list(range(-2024, 2024))
# print(numbers)
# print(max(numbers))
# numbers1 = list(range(123, 87384))
# print(min(numbers1))
# numbers1 = list(range(352, 20010118))





# son = int(input("son kiriting:  0 kiritmang   "))
# if son %2 == 0:
#     print(f"{son} juft ")
# else:
#     print(f"{son} toq ")






# from math import sqrt 


# son = int(input("son kiriting: " ))
# if son > 0: 
#     print(sqrt(son))
# if son < 0:
#     print("musbat son kiriting ")






# son1 = int(input("1-son kiriting: " ))
# son2 = int(input("2-son kiriting: " ))
# son3 = int(input("3-son kiriting: " ))

# sonlar= [son1,son2,son3]

# for s in range  (sonlar):   
#     if s > 0:
#         print(s**2)
#     elif s < 0:
#         print("musbat son kiriting! ")




# son = int(input("son kiriting:  0 kiritmang   "))
# from math import sqrt
# if son > 0: 
#     print(sqrt(son))
# if son < 0:
#     print(son**2)



# kod=int(input("parol kiriting")) 
# parol = "1234"
# if parol == "kod":
#     print(f"{parol} dasturga hush kelibsiz ")

 
"""
maktab baholar sistemasi"""

# ism = input("ismingizni kiriting ")

# baho = input(f"{ism} bugun nechi  baho oldingiz ")


# if baho == 0  or baho == 1:
#     print(" juda yomon ")
# if baho == 2 :
#     print(" qoniqarsiz ")
# if baho == 3 :
#     print(" qoniqarli")
# if baho == 4:
#     print(" yaxshi")
# if baho == 5 :
#     print("zor")



# ism = input("Ismingizni kiriting: ")
# bal = int(input(f"{ism} balingizni kiriting: "))
# grand = input("Nechinchi urini oldingiz: ")

# if bal >= 0 and bal <= 40:
#     print(f"{bal}ingiz juda yomon")
# elif bal >= 41 and bal <= 60:
#     print(f"{ism} Natijangiz qoniqarsiz")
# elif bal >= 61 and bal <= 80:
#     print(f"{ism} sizning natijangiz yaxshi")
# elif bal >= 81 and bal <= 90:
#     print(f"{ism} sizning natijangiz notug'ri")
# elif bal == 100:
#     print(f"{ism} tabriklaymiz siz 100% lik natijani korsatingiz")
# else: 
#     print(f" Siz faqat 0-100 dan katta sonlarni kiriting") 



# ism = input("Ismingizni kiriting: ")
# bal = int(input(f"{ism} balingizni kiriting: "))
# grand = input("Nechinchi urini oldingiz: ")
# if bal >= 0 and bal <= 40:
#     print(f"{bal}ingiz juda yomon")
# elif  bal <= 0  >= 68:
#     print("Failed")
# elif bal <= 68 >= 85:
#     print("Done")
# elif bal <= 85 >= 100:
#     print("ootdingiz")





# print("25 aylana yugurish kerak")
# aylana = int(input("nechta aylana yugurdingiz: "))
# if aylana >0 or aylana>20:
#     print("yana  yugurishingiz kerak")
# elif aylana==20:
#     print("siz 20 aylana yugurib boldingiz  boshqa yugurishingiz shart emas ")




# yosh  = int(input("yoshingizni kiriting: "))
# if yosh >0 and yosh<7:
#     print("sizga bepul")
# elif yosh >8 and yosh<18:
#     print("siz 15.000 tolashingiz kerak")
# elif yosh >18 and yosh<70:
#     print("siz 25.000 tolashingiz kerak")
# elif yosh >70 and yosh<100:
#     print("sizga bepul")
# elif yosh<0:
#     print("musbat son kiriting ")
# else:
#     print("siz hato kiritdingiz qaytadan urunib koring  ")






summa = 0
kishi = int(input("necha kishi kirmoqchisizlar: "))
for i in range(kishi):
    yosh  = int(input(f"{i+1}-kiradigan odamni yoshini kiriting: "))
    if yosh >0 and yosh<7:
        print("sizga bepul")
    elif yosh >8 and yosh<18:
        print("siz 15.000 tolashingiz kerak")
        summa = summa +15000
    elif yosh >18 and yosh<70:
        print("siz 25.000 tolashingiz kerak")
        summa = summa + 25000
    elif yosh >70 and yosh<100:
        print("sizga bepul")
    elif yosh<0:
        print("musbat son kiriting ")
    else:
        print("siz hato kiritdingiz qaytadan urunib koring  ")


print(summa)

   




















































































































