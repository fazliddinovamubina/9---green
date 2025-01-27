#theme: ro'yhatlar
""" element index"""
"""
mevalar = ["olma", "gilos", "orik" , " olcha "]
                0       1       2       3
                -4      -3      -2      -1



"""

# mevalar1 = ["olma", "gilos", "orik" , " olcha "]
# mevalar2 = {"olma", "gilos", "orik" , " olcha "}
# mevalar3 = ("olma", "gilos", "orik" , " olcha ")


# print (type(mevalar1))



# mevalar = ["olma", "gilos", "orik" , " olcha "]
# print(mevalar)
# print(mevalar[0])
# print(mevalar[-1])
# print(mevalar[-3])



# print(f"mening sevimli mevam {mevalar[0]. title()}")




""" royhatlar"""

# ismlar=["ali", "olim", "anvar"]
# sonlar=["3", "4", "5"]
# darslar= [ "phyton", "django", 3, 10 ]
# bosh_royhat=[]

# """ royhat elementlarni ozgartirish """
 
# print(darslar)
# darslar[0] = " telegram bot"
# print(darslar)




# son= [ 2, 6 , -5 ]
# print(son[0]* son[2])
# print(son[0]+ son[2])

"""vazifa"""
# ismlar=[ "oysha", "muslima", "abdulloh", "odina", "naima"]
# print(f"salom {ismlar [0]. title()}")
# print(f"salom {ismlar [1]. title()}")
# print(f"salom {ismlar [2]. title()}")
# print(f"salom {ismlar [3]. title()}")
# print(f"salom {ismlar [4]. title()}")


# sonlar=[ 5,-7, 12.1, 20 ]

# sonlar[ 0 ]= 15
# print(sonlar)
# print(sonlar [0]* sonlar [3] )

"""
ismlar degan ro'yxat yarating va kamida 5 ta yaqin do'stingizning ismini kiriting. 
   Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
2) sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang(musbat, manfiy, butun, o'nlik). 
    Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa o'chirib tashlaymiz.
"""





# students= [ "ali", " maruf", " bahrom"]

""" . append () - royhatga element qoshiladi """
# print (students)
# students. append (" umarbek")
# students.append(345345)
# print(students)



""" input blan qoshish """
# ism= input (" ism kiriting: ")
# students. append(ismn)


# students. append(input("ism kiriting : "))



# students = [ ]
""" . insert ( 3, " name ) - royhatga elementni index boyicha qoshiladi """
# students.insert (2, " jasur ")
# print( students )
  

# friends=[]

# friends.append(input("1 - dostingizni ismini kiriting")) 
# friends.append(input("2 - dostingizni ismini kiriting")) 
# friends.append(input("3 - dostingizni ismini kiriting")) 

# friends.insert(3 ,input("1 - dostingizni ismini kiriting")) 
# friends.insert( 2 ,input("2 - dostingizni ismini kiriting")) 
# friends.insert(   -3 , input("3 - dostingizni ismini kiriting"))

# print(friends)






""" extend() -- > bir ro'yhatni ikkinchisiga qoshish """
# fruts = [ " apple", " banana", "cherry "]
# tropic_frut= [ " mango ", "pineapple", "papaya"]
# fruts.extend(tropic_frut)
# print(fruts)
# print(tropic_frut)

# students= ["ali", "maruf", 'bahrom ']

"""del -  royxatdan elementni indexi boyicha ochiradi """
"""del->  kalit sozi royhatni butunlay ochirib tashlashi mumkin """
# print(students)


# del students[5]
# print(students)

"""   .remove( - royhatdan elementni qiymati boyicha ochiradi )"""
# students. remove("ali")

"""  .pop() - ro'yhatdan elementni sug'urib oluvchi metod"""
""" Agar pop() ga index bermasak u ro'yhat oxiridagi elementni aftomatik oladi """
# students.pop()
# print(students)



"""
4) friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan 
    do'stlaringizni kiriting. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi 
    yordamida o'chrib tashlang. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing


3) aktyorlar va honandalar degan ro'yhatlaer yarating va ularga o'zingiz eng ko'p kuzatadigan
    aktyorlar va honandalar ni kiriting, ulardan ikkitadan aktyorni o'chirib tashalng,va yangi 3tadan qo'shing.
    song'ra har ikkala ro'yhatdagi elementlarni insonlar degan yangi ro'yhatga jamlang

"""
# friends=[]
# friends.append ("anora")
# friends.append("malika")
# friends.append("oydina")
# friends.append("muslima")
# friends.append("soliha")


# friends.remove("anora")
# friends.remove("malika")
# friends.remove("oydina")
# friends.insert (1 ,"hadicha")
# friends.insert(3, "oisha")
# print(friends)



"""len() - royhatning uizunligini olchaydi"""
# family = ["father", "mpther","me"]
# print(f"bizningoilada{len(family)} tas inson bor ")
# print(f"they are {family[0]}, {family[1]},{family[2]]}")


# sonlar = [1,2,3,4,5,6,7,8,9]
# print(len(sonlar))


"""list( - royhat shaklllantirish uchun funksiya )"""
# country= list()# royhat yaratish 
# davlatlar=[]# bosh royhat

# print(country)
# print(davlatlar)


"""royhatni tozlash (elementlardan) clear()"""
# fruts = ["apple", "banana", "cherry"]
# print(fruts)
# fruts.clear()
# print(fruts)






"""range()  - sonle oraliq shakllantirish uchun funksiya """
# sonlar = list (range(-10,11 ))
# sonlar2 = list(range(0,100,5))
# print(sonlar)
# print(sonlar2)



"""royhatdAN nusxa olish """
# son = list(range(100,300 ))
# print(son)



# son2= son[50:70]
# son2= son[:70]
# son2= son[50:]
# print(son2)




"""8) Taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting.
    -nonushta degan yangi ro'yxatga taomlardan nusxa oling;
    -yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shi
qoldiring, va qo'shimcha 2 ta taom qo'shing;
    -ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring"""


# taomlar=["non","osh","lagman","shorva","ramen","corndog"]
# nonushta= taomlar[:]
# nonushta.remove("ramen")
# nonushta.remove("shorva")
# nonushta.append("non")
# taomlar.append("malako")
# print(taomlar)
# print(nonushta)



"""  .sort() - royhatni alifbo tartibida tartiblaydi """
# name  = ["olim", "anvar", "sarvar","ali","murod"]

# print(name)
# name.sort()     #togri tartiblash
# name.sort(reverse=True)   # teskari tartibdfa tartiblash 
# print(name)

# """sorted() -  royhatni bir marta alifbo tartibida tartiblab beradi """
# print(name)
# print(sorted(name))  # togri tartibda 
# print(sorted(name,  reverse =True))   # teskari tartibda 
# """ reverse() - royhatni boshini va ohirini aylantirib chiqaruvchi funksiya """
# country = ["uzbekistan","afrikaans","albanian", "englind", "russian", "serbian"]
# print(country)
# country.reverse()   # royhatni boshi va ohirini aylantirtib konsulga chiqaramiz 
# print(country)

# """range()"""
# number = list(range(1,21))
# print(number)
# """   max(), min(), sum() funksiyalari """

# print(max(number))   # eng katta sonni topib beradi  
# print(min(number))    # eng kichik sonni topib beradi
# print(sum(number))   # sonlarni yigindisini topib beradi 




# #1 
# country= ["korea", "afg'oniston", "hitoy", "vetnam","yaponiya","thailand","amerika"]
# print(f"royhatda {len(country)} shahar bor ")
# print(country)
# print(sorted (country))

# topshiriq

from math import sqrt 
print(sqrt(15))
print(1**100)
print(sqrt(100**2)+42342)
print(3434**2+123**2)
print(sqrt(834+5+34355))



# 4-mashq 
print("mening 'max' nomli mushugim bor")
print("salimning asablari doimgidek 'zo'r'")
ism_familiya= "aziizov abdug'affor "
meros="500 dollor"
ism_familiya="jafarov ali"



#5-mashq
x=int(23.5)
print(x)
y=float("9348")
print(y)
z=str(3.2)
print(z)

















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































