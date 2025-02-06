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













import datetime 

def otgan_kunlar(yil:int,oy:int,kun:int)->str:
    """ yashab otgan vaqtingizni yil va kun hisobida hisoblab beruvchi funksiya. 
    
    year - tugilgan yil
    moth - tugilgan oy
    day  - kun 

    9 Green sinfi bilan yasalgan fuksiya(06-02-2025)

    """

    t_yil  = yil # tugilgan yil
    t_oy   = oy  # tugilgan oy 
    t_kun  = kun # tugilgan kun 
    t_sana = datetime.date( yil, oy, kun ) # tugilgan sana
    bugun  = datetime.date.today()         # bugungi sana 

    if (bugun-t_sana).days <= 365:         # hali bir yoshga tolmagan chaqaloq uchun
        return f" siz tugilganingizga {(bugun-t_sana).days} kun boldi"
    elif bugun.month > t_oy:
        yil = bugun.year - t_yil
        kun = bugun-datetime.date(bugun.year, t_oy, t_kun)
        return f" siz tugilganingizga {yil}-yilu, {kun.days} kun boldi"

    elif bugun.month == t_oy:
        if bugun.day < t_kun:
            yil = bugun.year - t_yil - 1
            kun = bugun-datetime.date(bugun.year - 1, t_oy, t_kun)
            return f" siz tugilganingizga {yil}-yilu, {kun.days} kun boldi"
        
        elif bugun.day == t_kun:
            yil =bugun.year = t_yil
            return f" siz bugun {yil} yoshga toldingiz. tabriklaymiz ! "
        
        else:
            yil = bugun.year - t_yil
            kun = bugun-datetime.date(bugun.year, t_oy, t_kun)
            return f" siz tugilganingizga {yil}-yilu, {kun.days} kun boldi"
    else:
        yil = bugun.year - t_yil - 1
        kun = bugun-datetime.date(bugun.year - 1, t_oy, t_kun)
        return f" siz tugilganingizga {yil}-yilu, {kun.days} kun boldi"



yil = int(input("tugilgan yilingizni kiriting:  "))
oy  = int(input("tugilgan oyingizni  kiriting:  "))
kun = int(input("tugilgan kuningizni kiriting:  "))


foydalanuvchi = otgan_kunlar( yil, oy, kun )
print( foydalanuvchi)























