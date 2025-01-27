"""------ 9B001 ------"""
# #1-mashq
# ism="mubina"
# familiya="fazliddinova"
# yosh="14"
# kitoblar=["matem,ing liz, it, ona tili"]
# kasb=" doktor, kompyuter "
# print(type(ism))           
# print(type(familiya))
# print(type(yosh))
# print(type(kitoblar))
# print(type(kasb))

# #2-mashq
# from math import sqrt
# print(round(sqrt(4364+1233)**2))

# #3-mashq
# son1= int(input("1-son kiriting:"))
# son2= int(input("2-son kiriting:"))
# print((son1**2+son2**2)/23)

#4-mashq
# x=input("butun son kiriting: ")
# x=int(x)
# print(type(x))
# x=float(x)
# print(type(x))
#5-mashq
# kitoblar=[]
# kitoblar.append (print(input("1-kitob kiriting:")))
# kitoblar.append (print(input("2-kitob kiriting:")))
# kitoblar.append (print(input("3-kitob kiriting:")))
# kitoblar.append (print(input("4-kitob kiriting:")))
# kitoblar.append (print(input("5-kitob kiriting:")))

# #6-mashq
# students=["ali","maruf","bahrom"]
# students.append[0]
# students.append[1]
# students.append[2]
# students[2]="anvar"
# students[1]="aziz"


"""------ 9B002 ------"""

#1-mashq
# import random
# son1= int(input("1-son kiriting:"))
# son2= int(input("2-son kiriting:"))
# print(random.randrange)

#2-mashq
# kitoblar=[]
# kitoblar.append (input("1-kitob kiriting:"))
# kitoblar.append (input("2-kitob kiriting:"))
# kitoblar.append (input("3-kitob kiriting:"))
# kitoblar.append (input("4-kitob kiriting:"))
# kitoblar.append (input("5-kitob kiriting:"))
# del kitoblar[1]
# kitoblar.append[2]
# kitoblar.append[3]

#3-mashq
# fanlar=["matem","it"]
# fanlar.append("ona tili")
# fanlar.insert(3,"ing tili ")
# fanlar[0]="jistar"
# fanlar[1]="kimyo"
# del fanlar[2]
# fanlar.remove("kimyo")
# fanlar.pop(1)
# subject=[]
# subject=fanlar.copy()
# print(subject)
# fanlar.clear( )
# #4-mashq
# oila=[]
# oila.append(input("1-oila azolaringizni kiriting: "))
# oila.append(input("2-oila azolaringizni kiriting: "))
# oila.append(input("3-oila azolaringizni kiriting: "))
# oila.append(input("4-oila azolaringizni kiriting: "))
# oila.append(input("5-oila azolaringizni kiriting: "))
# oila.append(input("6-oila azolaringizni kiriting: "))
# oila.append(input("7-oila azolaringizni kiriting: "))
# print (oila)
#5-mashq
# cars=["mers","bmw","jenesis","malibu","tiko"]
# print(len(cars))
# cars.sort()
# cars.sort(reverse=True)
# print(cars)
# print(cars)
# cars.reverse()
# cars.sort()  

"""------ 9B004 ------"""
#1-mashq
# sonlar=[45, -96, 0, 63.2, 1257, -6752.2, 42, 3, 542]
# sonlar.sort()
# sonlar.sort(reverse=True)
# sonlar.reverse()
#2-mashq
# mevalar=["olma","orik","shaftoli","apelsin","malina","hurmo"]
# for meva in mevalar:
#     if meva=="olma"or meva=="malina":
#         print(meva.upper())
#     else:
#         print(meva.title())
#3-mashq
# books={
#     "1":"matem",
#     "2":"it"
# }
# books.update({"3":"ona tili "})
# print(books)
# books["4"]="ing tili "
# print(books)
# books["1"]="sarlavha "
# print(books)
# books.update({"2":"qashqirlar makoni"})
# print(books)

# books.popitem()

# del books["2"]

# books.pop("1")
 
#4-mashq
# sonlar= list(range(102,2020))
# for son in sonlar:
    # if son <1000:
        # print(son**3)
    # elif son>1500:
        # print(son-4)
# if son%7 == 0:
    # print(son)




#5-mashq
# natija=int(input("imtihonda necha foizlik natija korsatdingiz: "))
# if natija>=0 and natija<=100:
#     print("imtihondan ota olmadio")
# elif natija<=65 and natija>=100:
#     print("imtihondan otdi: ")

# # Kod: 9G001
# # 9 Green sinfi uchun haftalik(13-09-24) imtihon savollari
# # 1-	Mashq | 5 Ball
# # Bir vaqtni o’zida 4 ta o’zgaruvchi yarating(Bu ishni bir qatorda bajarish zarur !). Hamda o’zgaruvchilarni konsulga chiqaring.
# a, b, c,x= "alma","behi","anor","asal"
# print(a,b,c,x)

# # 2-	Mashq | 5 Ball |  Ushbu matinni konsulga chiqaring:
# # “Ahmadning “yuvvosh” mushugi meni ko’rsa, doim yugurib keladi.”
# print("ahmadning “yuvvosh”  mushugi meni korsa doim yugurib keladi ")


# # 3-	Mashq | 5 Ball | Misolni pyhtonda bajaring:
# # 93434 ga 94903 ni qoshing, hosil bo’lgan natijadaan 22344 ni ayring va unga 7363 ni qo’shing
# print(93434+94903-22344+7363)

# #  4-	Mashq | 10 Ball
# # Ism, yosh, manzil, maktab, sinf deb nomlangan o’zgaruvchilar yarating va ularni konsulga f”” yordamida chiqaring.

# ism="mubina"
# yosh="14"
# manzil="oromgoh"
# maktab="BM"
# sinf="9-green"
# print(f"ismim {ism} yoshi {yosh} manzilim {manzil} maktab {maktab} sinfim {sinf}")



# # 5-	Mashq | 10 Ball
# # Name, surname deb nomlangan o’zgaruvchilar yarating va ularni yangi full_name 
# # deb nomlangan o’zgaruvida jamlang. Hamda full_name deb nomlangan o’zgaruvchining 
# # qiymatini ba’zi metodlar ishlatgan holda barcha hariflarini kichhik qilib konsulga chiqaring.

# name="mubina"
# surname=" fazliddinova"
# print(name , surname)

# """ 1mashq"""
# y = int(input("yosh kirt:"))
# yil =2024
# print(yil-y+10)

"""2 mashq"""
# #1
# from math import sqrt
# print(round((23+(sqrt(9876))**2)/21),3)
# #2
# x=int(input("x kiriting"))
# y = 4*(x-3)**5-7(x-3)**3+2
# print(y)
# #3
# son = int(input("son kiriting:"))
# son1 = int(input("son kiriting:"))
# import random
# print(random.randrange(son,son1))
# #4
# s = int(input("son kiriting:"))
# a = int(input("son kiriting:"))
# n = int(input("son kiriting:"))
# k = int(input("son kiriting:"))
# print(round((s**a)/n),k)
#5


# """ 3 mashq """
# bozorlik=[]
# bozorlik.append("olma")
# bozorlik.append("anor")
# bozorlik.append("kivi")
# bozorlik.append("banaa")
# bozorlik.append("sshaftoli")

# bozorlik.insert(0,"banana")
# bozorlik.insert(4,"avocado")
# bozorlik.insert(-1,"uzum")
# print(bozorlik)

#1
print("hello ")
print("men hursandman")
print("'night has come' bu eng zor kino ")
print("bu noto'g'ri emas")
print("before and after")
#2 
print("ahmadhon")
print("mahbubahon")
print("fazliddin")
print("mubina")
print("muhammadamin")
print("muslima")
print("hadicha")
#3
print("456677")
print("77777")
print("665333766")
#4

"""imtihon tahlili"""
#1 -mashq   
# x, y, n,r,= "olma","anor" , "tarvuz", "ruchka"
# print(x,y,n,r)
#2- mashq 
# print("Ahmadning \"yuvvosh\" mushugi meni ko'rsa, doim yugurib keladi")
 #3-mashq                                                                                                                                                                                        
# print(93434+94903-22344+7363)
#4-mashq
# ism= "Mubina"
# yosh= "14"
# manzil= "oromgoh"
# maktab= "B.M."
# sinf= "9-green"
# print(f" ismim {ism} yoshim {yosh} manzilim {manzil} maktabim {maktab} sinfim {sinf}" )
#5-mashq
# name="Mubina"
# surename="Fazliddinova"
# fullname=f"{name} {surename}"
# print(fullname.lower())
#6-mashq
# gul="  BoyCHeCHak "
# print(gul.lstrip())
# print(gul.strip())
# print(gul.title())
# print(gul.upper())
# print(gul.lower())

"""type () funksiyasi """
# yosh= 34
# pi= 3.14
# print(type(ism)) # string--> str--> matn 
# print(type(yosh)) # integer--> int--> butun son
# print(type(pi)) # float-->float--> o'nlik son

""" maxsus belgilar"""
# \ '    ' belgisi ucun 
#\"       "belgisi uchun
#\n        yangi qator
# \b       tab 
#\b        boshliqni yoqotadi










































































































































































