""" New thame"""
"""
Thame: Dictionary (lugat)
"""

# taomlar = {
#      'ali': 'osh',
#      'vali':'lagmon',
#      'ali':'osh',
#     'husan':'mastava',
#     'olim':'somsa',
#      'nodir':'kabob'
#  }

"""
taomlar = {'ali':'osh'}               
nomi    = {'key':'value' }     
""" 
  
# print(taomlar)
# print(type(taomlar))  # dictionary -->  dict --> lug'at 

# print(taomlar['ali'])
# print(f"olimning ning sevimli taomi {taomlar['ali']}")

# buyumlar ={
#     "ism":"ali",
#     "yosh":"23",
#     "student":"true",
#     "oila":["ota","ona","aka"]
                                                                     
# }
# print(buyumlar)

# green_9= {
#     "olimjanova":"sarvinoz",
#     "botirova":"hadicha",
#     "malikova":"naima",
#     "tohirova":"naima"
# }
# print(green_9)

""" element qoshish """
# green_9.update({"mamadova":"oydina"})
# print(green_9)

# green_9["fazliddinova"] = "mubina"
# print(green_9)

# green_9[input("familiya kiriting: ").lower() ]=input("ism kiriting: ")
# print(green_9)

"""elementni qiymatini yangilash """
# green_9.update({"mamadova":"muslima"})
# print(green_9)

# green_9["fazliddinova"] = "masrura"
# print(green_9)

# """ elementni o'chirish """
# del green_9["botirova"]
# print(green_9)

# green_9.pop("fazliddinova")
# print(green_9)

# green_9.popitem()
# print(green_9)

""" lugatni o'chirish """
# del green_9

# oila={
#     "ona":"mahbuba",
#     "aka":"fazliddin",
#     "uka":"muhammadamin",
#     "men":"mubina"
# }
# #1-mashq
# print(f"mening otamning ismi {oila["ota"]}, onamning ismi {oila["ona"]},\
# akamning ismi {oila["aka"]}, ukamning ismi {oila["uka"]},\
# mening ismim {oila["ozim"]}")
# #2-mashq
# family={
#     "ota":"shorva",
#     "ona":"shorva1",
#     "aka":"chuchvara",
#     "uka":"osh",
#     "men":"ramen"
# }

# print(f"otamning sevimli taomi{family["ota"]}")
# print(f"onamning sevimli taomi{family["ona"]}")
# print(f"akamning sevimli taomi{family["aka"]}")



""" .get() --> metodi"""
# # print(green_9["abdulahad"])# hato chiqadiga kod 
# print(green_9.get("abdulahad", "bunday isim yoq "))
# print(green_9.get(input("key kiriting: "), "bunday ism yoq "))





# lugat_eng_uzb={
#     "ink":"siyoh",
#     "bad":"yomon",
#     "sun":"quyosh",
#     "apple":"olma",
#     "water melon":"tarvuz"
# }

# print(lugat_eng_uzb.get(input("lugat kiriting: "), "bunday lugat yoq "))


# dost={
#     "ism":input("ism kiriting:"),
#     "familiya":input("familiya kiriting"),
#     "yosh":input("yosh kiriting"),
#     "hobbi":input("hobbiyingizni n kiriting"),
#     "sport":input("sportingizni kiiriting")
# }


# print(f"mening dostimning ismi {dost["ism"]} \
#     mening dostimning familiyasi{dost["familiya"]}\
#     yoshi {dost['yosh']}  hobbisi {dost["hobbi"]}\
#     yoqtirgan sporti {dost["sport"]}")


""" keys(), values(), items() - metodlari """

# green_9={
#     "olimjanova":"sarvinoz",
#     "botirova":"hadicha",
#     "malikova":"naima",
#     "tohirova":"naima"
#     }
# print(green_9.keys())
# print(green_9.values())

# print(f"9 green sinfida quidagi oquvchilar bor: ", end=" ")
# for family in green_9.keys():
#     print(family, end=" ")

# print(f"\n9 green sinfida quidagi oquvchilar bor: ", end=" ")
# for ismlar in green_9.values():
#     print(ismlar, end=" ")

""" items()- metodi"""
# print(green_9.items())
# for key, value in green_9.items():
#     print(f"{key}-{value}")


# eng_uz ={
#     "apple":"olma",
#     "bread":"non"
# }
# word= input("soz kiriting: ").lower()
# for key, value in eng_uz.items():
#     if word == key:
#         print(f"{key}-{value}")
#     elif word == value:
#         print(f"{value}-{key}")


# if word not in eng_uz.keys() and word not in eng_uz.values():
#         print("bizda bu soz haqida malumot yoq")



# dav = {
#     "korea":"seul",
#     "kitay":"pekin",
#     "singapour":"singapour",
#     "turkiya":"anqara"
# }
# dav.sorted()
# print(dav)




# davlatlar = {
#     "Korea":"seul",
#     "Xitoy":"pekin",
#     "Singapour":"singapour",
#     "Turkiya":"anqara",
# }

# dav= input("davlat kiriting: ").lower()
# for key, value in davlatlar.items():
#     if dav == key:
#         print(f"{key}-{value}")
#     elif dav == value:
#         print(f"{value}-{key}")



# if dav not in davlatlar.keys() and dav  not in davlatlar.values():
#         print("bizda bu davlat haqida malumot yoq")


# green_9={
#     "olimjanova":"sarvinoz",
#     "botirova":"hadicha",
#     "malikova":"naima",
#     "tohirova":"naima",
#     "fazliddinova":"mubina"
#     }

# ism= input("ism kiriting: ").lower()
# for key, value in green_9.items(): 
#     if ism == key:
#         print(f"{key}-{value}")
#     elif ism == value:m
#         print(f"{value}-{key}")


# if ism not in green_9.keys() and ism  not in green_9.values():
#         print("bizda bu oquvchi haqida malumot yoq")




# taom={
#      "ramen":"15",
#      "lagmon":"25",
#      "kfc":"100gramm 25",
#      "shorva":"35",
#      "mastava":"25",
#      "osh":"20",
#      "qotirma":"60",
     
# }

























































































































































































































































































































































