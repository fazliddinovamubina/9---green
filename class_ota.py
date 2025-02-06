"""
ota class
"""
# class Shaxs():
#     """"""

#     def __init__(self, ism, familiya, sharif, t_yil, passport, millat):
#         self.ism=ism
#         self.familiya=familiya
#         self.sharif= sharif
#         self.t_yil=t_yil
#         self.passport=passport
#         self.millat=millat


#     def __str__(self):
#         return f"{self.ism}  {self.familiya}  {self.sharif}"    

#     def get_info(self):
#         """ shaxs haqida toliq malumot beruvchi funksiya """

#         return f"{self.familiya} {self.ism} {self.sharif}  {self.t_yil}-yilda tug'ilgan. millati {self.millat}. passport raqami: {self.passport}"

#     def get_age(self,h_yil):
#         """ shaxsni yoshini qaytaruvchi funksiya"""
#         return h_yil-self.t_yil

#     def get_pasport(self):
#         """ shaxsni pasportini qaytaruvchi funksiya"""
#         return self.passport


#     def get_millat(self):
#         """ shaxsni millatini qaytaruvchi funksiya"""

#         return self.millat
 



# shaxs1= Shaxs("sarvinoz", "olimjanova", "shuxratova", 2009, "ac1234555", "ozbek" )
# print(shaxs1)
# print(shaxs1.get_info())
# print(shaxs1.get_age(2025))

# class Students(Shaxs): #voris klass
#     """oquchi haqida malumot beradi"""

#     def __init__(self, ism:str, familiya:str, sharif:str, t_yil:int, passport:str, millat:str, maktab:str, sinf :int, baholar:int ):
#         """ talabaning hususiyatlari """
#         super().__init__(ism, familiya, sharif, t_yil, passport, millat)
#         self.maktab=maktab
#         self.sinf=sinf
#         self.baholar=baholar

#     def get_baxolar(self):
#         """ umumiy ballni qaytaruvchi funksiya"""
#         return f"{self.maktab}"

#     def get_maktab(self):
#         """ umumiy ballni qaytaruvchi funksiya"""
#         return sum(self.baholar)



#     def change_maktab(self, new_school):
#         """ maktabni almashtirib  qaytaruvchi funksiya"""
#         self.maktab = new_school
#         return self.maktab
#     def set_sinf(self):
#         """ umumiy ballni qaytaruvchi funksiya"""
#         if self.sinf< 11:
#             self.sinf += 1
#             return self.sinf
#         else:
#             return" siz hozirda eng ohirga sinfdasiz" 



#     def get_sinf(self):
#         """ umumiy ballni qaytaruvchi funksiya"""
#         return f"{self.sinf}"

# student1= Students("sarvinoz", "olimjanova", "shuxratova", 2009, "ac1234555", "ozbek", "bm maktab", 9, [3,54,6,75,66] )
# print(student1)
# print(student1.get_info())
# print(student1.get_age(2025))
# print(student1.get_maktab())
# print(student1.get_sinf())
# print(student1.set_sinf())
# print(student1.get_baxolar())
# print(student1.change_maktab())




""" vazifa """
class Naima(): 
    """oquchi haqida malumot beradi"""

    def __init__(self, ism:str, familiya:str, sharif:str, t_yil:int, passport:str, millat:str ):
        """ sotuvchining hususiyatlari """
        self.ism=ism
        self.familiya=familiya
        self.sharif= sharif
        self.t_yil=t_yil
        self.passport=passport
        self.millat=millat

    def __str__(self):
        return f"{self.ism}  {self.familiya}  {self.sharif}"    

    def get_info(self):
        """ shaxsni  haqida toliq malumot beruvchi funksiya """

        return f"{self.familiya} {self.ism} {self.sharif}  {self.t_yil}-yilda tug'ilgan. millati {self.millat}. passport raqami: {self.passport}"

    def get_age(self,h_yil):
        """ shaxsni  yoshini qaytaruvchi funksiya"""
        return h_yil-self.t_yil

    def get_pasport(self):
        """ shaxsni  pasportini qaytaruvchi funksiya"""
        return self.passport


    def get_millat(self):
        """ shaxsni  millatini qaytaruvchi funksiya"""

        return self.millat


shaxs1= Naima("saida", "anvarova", "ahmedova", 2010, "ac1234775", "ozbek" )
print(shaxs1)
print(shaxs1.get_info())
print(shaxs1.get_age(2025))
print(shaxs1.get_pasport())
print(shaxs1.get_millat())


class Students(Naima): #voris klass
    """oquchi haqida malumot beradi"""

    def __init__(self, ism:str, familiya:str, sharif:str, t_yil:int, passport:str, millat:str, maktab:str, sinf :int, baholar:int ):
        """  hususiyatlari """
        super().__init__(ism, familiya, sharif, t_yil, passport, millat)
        self.maktab=maktab
        self.sinf=sinf
        self.baholar=baholar


    def __str__(self):
        return f"ISMI {self.ism}  FAMILIYASI {self.familiya} SHARIFI  {self.sharif} MAKTABI {self.maktab}"    


    def get_baxolar(self):
        """ umumiy ballni qaytaruvchi funksiya"""
        return sum(self.baholar)



    def get_maktab(self):
        """ umumiy ballni qaytaruvchi funksiya"""
        return f"maktabi {self.maktab}"


    # def change_maktab(self, new_school):
    #     """ maktabni almashtirib  qaytaruvchi funksiya"""
    #     self.maktab = new_school
    #     return self.maktab
    def set_sinf(self):
        """ umumiy ballni qaytaruvchi funksiya"""
        if self.sinf< 11:
            self.sinf += 1
            return self.sinf
        else:
            return" siz hozirda eng ohirga sinfdasiz" 



    def get_sinf(self):
        """ umumiy ballni qaytaruvchi funksiya"""
        return f" {self.ism}ning sinfi {self.sinf}"

student1= Students("hadicha", "yolbarsova", "ahmedova", 2010, "ac1234775", "ozbek", "31 maktab", 9, [3,4,5,6,7] )
print(student1)
print(student1.get_info())
print(student1.get_age(2025))
print(student1.get_maktab())
print(student1.get_sinf())
print(student1.set_sinf())
print(student1.get_baxolar())
# print(student1.change_maktab())



















"TEXNIKA NOUTBOOK TELEFON"


class Texnika():
    """ texnika haqida malumot beradi """
    def __init__(self, yil:int, kompaniya:str , brend:str,  model:str,  narx:int, rang:str, muddat:int):
        """ texnika malumotlari """
        self.yil=yil
        self.kompaniya=kompaniya
        self.brend=brend
        self.model=model
        self.narx=narx
        self. rang= rang
        self.muddat=muddat

    def __str__(self):
        """ brendi va  rangini chiqaruvchi funksiya"""
        return f"brendi {self.brend} rangi {self.rang}"

    

    def get_kompany(self):
        """ kompaniyasi chiqaruvchi funksiya"""
        return f"kopmaniyasi {self.kompaniya}"


    def get_brend(self):
        """brend chiqaruvchi funksiya"""
        return f"brendi {self.brend} "


    def get_model(self):
        """ modelini chiqaruvchi funksiya"""
        return f"modelini {self.model}"


    def get_narx(self):
        """ narxini chiqaruvchi funksiya"""
        return f" narxini {self.narx} "

    def change_rang(self,rang):
        """ rangini chiqaruvchi funksiya"""
        self.rang=rang
        return rang 

    def get_muddat(self):
        """ brendi va  rangini chiqaruvchi funksiya"""
        return f"muddati  {self.muddat} yil "


    def change_company(self,kompaniya):
        """ brendi va  rangini chiqaruvchi funksiya"""
        self.kompaniya=kompaniya
        return kompaniya


texnika=Texnika(2000,"cloud","brain","gv80",8000,  "qizil", 3 )
print(texnika.get_narx())
print(texnika.get_muddat())
print(texnika.change_rang("qora"))
print(texnika.change_company("atlanta"))
print(texnika.get_brend())
print(texnika.get_kompany())
print(texnika.get_model())



class Noutbook(Texnika):
    """ voris class"""
    super().__init__()
























