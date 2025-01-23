# """ class """
# """ OOP Object oriented programming """

# class Car():
#     """ docstring """

#     def __init__(self, company:str, model:str, color:str, price:int, max_speed:int, year:int ): # parametr
#         self.company= company # hususiyat
#         self.model=model   
#         self.color=color 
#         self.price= price
#         self.max_speed= max_speed
#         self.year= year

#     def grt_info(self):
#         """ mashina haqida malumot beruvchi funksiya """


#         info=f" mashina haqida malumotlat: \nkompaniya:{self.company}  \nmodeli:{self.model} \nrangi:{self.color} \nnarxi:{self.price}  \
#         \ntezligi:{self.max_speed}  \nyili:{self.year} \n "   
#         return info 


# car1=Car("tesla", "model2", "black",30_300, 220, 2025 )
# car2=Car("BMW", "model 3", "brown",30_600, 270, 2005 )
# car3=Car("MERS", "model 23", "pink",30_6700, 320, 2015 )





# class  Car():
#     """ companiya va modelini aniqlab beradi """
#     def __init__(self,company:str, model:str, color: str, narxi:int, yil: int):
#         self.company=company
#         self.model=model   
#         self.color=color 
#         self.price=narxi
#         self.year= yil

#     def get_info(self):
#         """ mashina haqida malumot beradi """
        
#         info= f" mashinaning modeli:{self.model}" 
#         return info 



# """  talaba haqidagi class"""


# class Talaba :
#     def __init__(self, ism:str, familiya:str, kurs:int, baholar: list, year: int,  friends:str  ):
#         """   taqlaba haqidagi malumotlarni aytadgan funksiya   """
#         self.ism=ism
#         self.familiya=familiya
#         self.kurs=kurs
#         self.baholar=baholar
#         self.year= year
#         self.friends=friends

#     def get_habar(self):
#         "talaba haqida maklumot beradi "
#         return f" talabaning ismi {self.ism} \ntalabaning familiyasi {self.familiya} \nkursi {self.kurs}"
    
#     def orta_arifmetik(self):
#         return  sum(self.baholar)/  len (self.baholar) 
    

#     def get_full_name(self):
#         """ toliq ismini naytadi """
#         return f"{self.ism} {self.familiya}"
    

#     def get_age(self, now=2025):
#         """ talabaning yoshini qaytaradi """
#         return now-self.year
    

#     def get_friends(self):
#         """ talabaning dostlarini royhatini chiqaradi """
#         info=f"{self.ism}ning dostlari:"
#         for ism in self.friends:
#             info += f"{ism}"
#         return info
    
#     def set_kurs(self):
#         """ talabaning kursini ozgartiruvchi """
#         if self.kurs< 6:
#             self.kurs += 1
#         else:
#             return" siz hozirda eng ohirga kursdasiz" 

#     def get_kurs(self):
#         """ kursidaligi YTADI"""
#         return self.get_kurs




# ali = Talaba("ali", " valiyev", 2, [1,2,4,4], 2000, " ahror, asad, akrom, aziz")
# print(ali.get_habar())
# print(ali.orta_arifmetik())
# print(ali.get_full_name())
# print(ali.get_age())
# print(ali.get_friends())




class Library():
    """ kutubhona classi """
    def __init__(self, name:str, adress:str):
        self.name = name 
        self.adress = adress
        self.books = []
        self.books_count = 0 


    def __str__(self):
        return self.name



    def add_book(self, book:str):
        """ kutubxonaga kitob qo'shuvchi funksiya """
        if self.books< 6:
            self.books += 1



    def get_books(self):
        """  KUTUBXONADAGI KITROBLAR    NOMINI QAYTARADIGAN funksiya"""
        return len(self.books)

    def delete_book(self, book):
        """ kutubxonadagi kitobni ochiriladi """
        if book in self.books:
            self.books.remove(book)
            self.books_count -= 1
            return f"{book} kitob kutubxonadan ochirildi "
        else:
            return f"{book} kitob kutubxonadan topilmitti  "



    def get_info(self):
        """ kutubxona haqidagi malumotlarni qaytaradi (nomi, manzili, kutubxonadagi kitoblar soni)"""
        return f" kutubhona nomi { self.name}, \nmanzili {self.adress},  \nkutubxonadagi kitoblar soni {self.books_count}"

kitob=(Library("the books shelf", "toshkent"))
print(kitob.get_books())
print(kitob.get_info())



class Book():
    """ """
    def __init__(self, name:str , muallif: str, yil: int, nashriyot:str , narx:int ):
        """ """
        self.name= name
        self.muallif=muallif 
        self.yil=yil 
        self.nashriyot= nashriyot
        self.narx = narx 

    def __str__(self):
        return self.name

    def get_info(self):
        n=( f"ismi {self.name},\nmuallifi {self.muallif}, \nyili {self.yil},\nnashriyot {self.nashriyot}, \nnarxi {self.narx} " )
        return n

    def get_name(self):
        return self.name


    def get_price(self):
        return self.narx




book1= Book("ikki eshik orasi", "otkir hoshimov", 1988, "ziyo", 69_000)
book2= Book("otkan kunlar", "abdulla qodiriy", 1925, "oliy", 35_000)

print(book1.get_info())
print(book1.get_name())
print(book1.get_price())


print(book2.get_info())
print(book2.get_name())
print(book2.get_price())




""" obyektning hususiyat va metodlarini korish """
""" dir() funksiyasi """

from pprint import pprint # prety print 

pprint(dir(kitob))
pprint(dir(book1))





""" __dict__ metodi """
""" __dict__metodi obyektining xususiyatlarini lugat korinishida qaytaradi """

print(kitob.__dict__)
print(book1.__dict__)
print(book2.__dict__)






































