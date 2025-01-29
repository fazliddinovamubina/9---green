"""
ota class
"""
class Shaxs():
    """"""

    def __init__(self, ism, familiya, sharif, t_yil, passport, millat):
        self.ism=ism
        self.familiya=familiya
        self.sharif= sharif
        self.t_yil=t_yil
        self.passport=passport
        self.millat=millat


    def __str__(self):
        return f"{self.ism}  {self.familiya}  {self.sharif}"    

    def get_info(self):
        """ shaxs haqida toliq malumot beruvchi funksiya """

        return f"{self.familiya} {self.ism} {self.sharif}  {self.t_yil}-yilda tug'ilgan. millati {self.millat}. passport raqami: {self.passport}"

    def get_age(self,h_yil):
        """ shaxsni yoshini qaytaruvchi funksiya"""
        return h_yil-self.t_yil

    def get_pasport(self):
        """ shaxsni pasportini qaytaruvchi funksiya"""
        return self.passport


    def get_millat(self):
        """ shaxsni millatini qaytaruvchi funksiya"""

        return self.millat
 



shaxs1= Shaxs("sarvinoz", "olimjanova", "shuxratova", 2009, "ac1234555", "ozbek" )
print(shaxs1)
print(shaxs1.get_info())
print(shaxs1.get_age(2025))

class Students(Shaxs): #voris klass
    """oquchi haqida malumot beradi"""

    def __init__(self, ism:str, familiya:str, sharif:str, t_yil:int, passport:str, millat:str, maktab:str, sinf :int, baholar:int ):
        """ talabaning hususiyatlari """
        super().__init__(ism, familiya, sharif, t_yil, passport, millat)
        self.maktab=maktab
        self.sinf=sinf
        self.baholar=baholar

    def get_baxolar(self):
        """ umumiy ballni qaytaruvchi funksiya"""
        return f"{self.maktab}"

    def get_maktab(self):
        """ umumiy ballni qaytaruvchi funksiya"""
        return sum(self.baholar)


    def set_sinf(self):
        """ umumiy ballni qaytaruvchi funksiya"""
        if self.sinf< 11:
            self.sinf += 1
            return self.sinf
        else:
            return" siz hozirda eng ohirga sinfdasiz" 



    def get_sinf(self):
        """ umumiy ballni qaytaruvchi funksiya"""
        return f"{self.sinf}"

student1= Students("sarvinoz", "olimjanova", "shuxratova", 2009, "ac1234555", "ozbek", "bm maktab", 9, [3,54,6,75,66] )
print(student1)
print(student1.get_info())
print(student1.get_age(2025))
print(student1.get_maktab())
print(student1.get_sinf())
print(student1.set_sinf())
print(student1.get_baxolar())
