# # """ funksiyalar"""
# # print("hello world")

# def salom_ber():
#     print("assalomu aleykum😀")


# # salom_ber()




# # def yosh_top():
# #     ism = input("ismingizni kiriting: ")
# #     t_yil = int(input(f"{ism.title()}tug'ilgan yilingizni kiriting: "))

# #     print(f"{ism.title()} sizning yoshingiz-{2024-t_yil} da ")


# # yosh_top()


# def yosh_top(t_yil):
#     """
#     Tug'ilgan yilni  qabul qilib olib yoshni hisoblaydigan funksiya😀

#     t_yil ----> int
#     """
#     print(f"Sizning yoshingiz {2024-t_yil}da😉")
# yosh_top(2009)
# yosh_top(2010)

# x = int(input("T yil kiriitng:"))
# # yosh_top(x)



# print(print.__doc__)# duble4 under score --> dunder me
# """ parametrni key word blan berish """

# def yosh_top(ism, t_yil):
#     print(f"salom{ism.title()}, siz {t_yil}- da tug'ilgansiz va yoshingiz {2024- t_yil} da ")

# yosh_top("ali", t_yil=2012)


# """ standart qiymat """

# def yosh_top(ism, t_yil=2000):
#     print(f"salom{ism.title()}, siz {t_yil}- da tug'ilgansiz va yoshingiz {2024- t_yil} da ")

# yosh_top("ali", t_yil=2012)


#1-mashq 
# print(len.__doc__)
# print(max.__doc__)
# print(sum.__doc__)
# print(range.__doc__)
# print(list.__doc__)


#2-mashq


# son=int(input("balingizni kiriting: "))

# def baho():
#     """son=int
#     balingizni kiritsangiz yaxshi yoki yomonligini aytib beradi 
#     """
#     if son>=0 and son<=50:
#         print(f"siz {son } topladingiz qoniqarsiz")
#     elif son<=51 and son>=70:
#         print(f"siz {son } topladingiz qoniqarli")
#     elif son<=71 and son>=90:
#         print(f"siz {son } topladingiz yaxshi ")
#     elif son>=91 and son<=100:
#         print(f"siz {son } topladingiz alo")
#     else: 
#         print("0 dan katta 100 dan kichik sonlar ni kiritishingiz kerak ")

# baho()
         
# #3-mashq
# s=int(input("to'g'ri to'rt burchakni tomonini kiriting  kiriting yuzini hisoblab beradfi :"))
# p=int(input("to'g'ri to'rt burchakni tomonini kiriting  kiriting perimetrini hisoblab beradi :"))
# def p_top():
#     """ to'g'ri to'rt burchakni yuzini va perimetrni hisoblab beradi 
#     s=int
#     p=int
#     """

# sonlar=[0,-5, 9, -12, 99]

# def tartibla (qiymat):
#     qiymat.sort()
#     print(qiymat)

# tartibla(sonlar)

# """funksiyadan qiymat qaytarish """
# #def yosh_top(t_yil: int, ism: str, oila: list)-> int: # t_yil -parametr 
# def yosh_top(t_yil:  int ) -> int: #t_yil - parametr
#     """tugilgan yilni qabul qilib olin yoshini qaytaradgan funksiya"""
#     yosh=2024-t_yil
#     return yosh # return ---> qaytarish print ni orniga ikkkalai bir narsa 😀

# malikovaning_yoshi = yosh_top(2010)
# print(f"malikaning yoshi {malikovaning_yoshi } da")

# def person(name:str, surename:str, email:int, age:int, phone: int)-> dict:
#     """ """
#     person = {
#         "name":name,
#         "surname":surename,
#         "email": email,
#         "age":age,
#         "phone":phone
#     }
#     return person 

# person1=person("ali", "ahmadov", "ali.gmail.com",33, 2225343)

# print(person1)


# def oila(ota: str, ona:str, aka:str, uka:str)->list:
#     """ oila azolaringizni kiritsangiz royhat qilib chiqarib beradi """
#     oila=[ota, ona, aka, uka ]
#     return oila
# oila1=oila("ali", "aziza", "aziz","axror")

# print(oila1)

    


# #mashq
# def baholash(ismlar):
#     """talabaning bahosini kiritsangiz siz uni royhat qilib chiqarib beradi """
#     score={}
#     while ismlar:
#         name = ismlar.pop()
#         baho = input(f" talaba {name.title()}ning bahosini kiriting:  ")
#         baho = input(f" talaba {name.title()}ning bahosini kiriting:  ")
#         score[name]=baho
#     return score
    
# students=["ali","aziz","ikrom"]
# score= baholash(students)
# print(baholash)

# def info (name:str, age:int, sinf="9-green")-> str: # sinf= "9-green" -> standart qiymat 
#     """"""
#     return f"{name.title()} your age{age}, your class {sinf}"
# students1 = info (sinf="10 green")
#3-maqshq
""" *args usuli """
# def my_sum(*sonlar):# *arg
#     summa = 0 
#     for son in sonlar :
#         summa= summa + son 
#     return summa 
# print(my_sum(4,5,6,7,8,-8,9,8,3))
# print(my_sum(2,3,4))
# print(my_sum())



"""----------------- takrorlash -----------------------"""

# def yosh(ism, yil, hyil)->str :
#     """"""
#     return f"{ism.title()} ning yoshi {hyil-yil}da "



# lola=yosh("lola",2006)
# aziza=yosh("aziza",2009,hyil=2021)




# def oraliq(a,b):
#     for n in a :
#         n+=1
#         if n==b:

# def oraliq(a:int,b:int):# *arg
#     numbers= [a]
#     for son in numbers:
#         if son> b-1: 
#             break  
#         numbers.append(son+1) 
#     return numbers
# print(oraliq(1,8))




# range funksiyasi 


# def oraliq(a:int,b:int, qadam=1):# *arg
#     numbers= [a]
#     for son in numbers:
#         if son> b-1: 
#             break  
#         numbers.append(son+ qadam) 
#     return numbers
# print(oraliq(1,8,2))




"unli va undosh harflarni topuvchi "


# def harf(harf:str)->str:
#     """ harf kiritsangiz unli va undosh harfni aniqlab ajratib beradi"""

#     unli= "eoiau"
#     if harf in unli:
#         return f"{harf} is vowel"
#     else:
#         return f"{harf} is not vowel"

# print(harf(input(" harf kiriting: ")))




# def orta_arifmetik(*son)-> int:
#     """ sonlarni kiritsangiz orta arifmetigini topib beradi """
#     sonlar=0
#     for son1 in son:
#         sonlar+=son1
#     return sonlar/len(son)

# # print(orta_arifmetik(21,3,4,5,11,56))




# def middle(*numbers:int)->int:
#     """  """
#     summa = 0
#     count = 0 

#     for number in numbers:
#         summa+= number 
#         count+= 1 
#     return summa/count



# # print(middle(12,33,4,5,3))
# # print(middle(22,44,66,767))































