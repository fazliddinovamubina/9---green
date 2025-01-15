""" class """
""" OOP Object oriented programming """

class Car():
    """ docstring """

    def __init__(self, company:str, model:str, color:str, price:int, max_speed:int, year:int ): # parametr
        self.company= company # hususiyat
        self.model=model   
        self.color=color 
        self.price= price
        self.max_speed= max_speed
        self.year= year

    def grt_info(self):
        """ mashina haqida malumot beruvchi funksiya """


        info=f" mashina haqida malumotlat: \nkompaniya:{self.company}  \nmodeli:{self.model} \nrangi:{self.color} \nnarxi:{self.price}  \
        \ntezligi:{self.max_speed}  \nyili:{self.year} \n "   
        return info 


car1=Car("tesla", "model2", "black",30_300, 220, 2025 )
car2=Car("BMW", "model 3", "brown",30_600, 270, 2005 )
car3=Car("MERS", "model 23", "pink",30_6700, 320, 2015 )





class  Car():
    """ companiya va modelini aniqlab beradi """
    def __init__(self,company:str, model:str, color: str, narxi:int, yil: int):
        self.company=company
        self.model=model   
        self.color=color 
        self.price=narxi
        self.year= yil

    def get_info(self):
        """ mashina haqida malumot beradi """
        
        info= f" mashinaning modeli:{self.model}" \n compan










