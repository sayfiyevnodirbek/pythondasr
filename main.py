# son= int(input("Biror bir son kiriting: "))
# if son%2==0:
#     print("Bu son juft.")
# else:
#     print("Bu son toq son.")
# yosh=int(input("Sizning yoshingiz nechada: "))
# if yosh<=4 or yosh>=60:
#     narh=0
# elif yosh<=18:
#     narh=10000
# elif yosh>18:
#     narh=20000
# print(f"Siz uchun muzeyga kirish narxi {narh} so`m")
# son1=int(input("Birinchi sonni kiriting: "))
# son2=int(input("Ikkinchi sonni kiriting: "))
# if son1>son2:
#     print(f"Birinchi {son1} soni ikkinchi {son2} sonidan katta")
# elif son1==son2:
#     print(f"Birinchi {son1} soni ikkinchi {son2} soniga teng")
# else:print(f"Ikkinchi {son2} soni birinchi {son1} sonidan katta")
# mahsulotlar= ["fudbolka","mayka","kepka","tapichka","sumka","ochki","naski","botinka","rement","ro`mol"]
# savat=[]
# for n in range(5):
#     tovar=input(f"{n+1}-mahsulot nomini kiriting: ")
#     savat.append(tovar.lower())
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Ushbu {mahsulot} tovari do`konimizda  mavjud")
#     else:
#         print(f"Ushbu {mahsulot} tovari do`konimizda  mavjud emas")
#
# mahsulotlar= ["fudbolka","mayka","kepka","tapichka","sumka","ochki","naski","botinka","rement","ro`mol"]
# savat=[]
# for n in range(5):
#     mahsulot=input(f"{n+1} - mahsulot nomini kiriting: ")
#     savat.append(mahsulot.lower())
# savatcha=[]
# mavjud_emas=[]
# for mahsulot1 in savat:
#     if mahsulot1 in mahsulotlar:
#         savatcha.append(mahsulot1)
#     else: mavjud_emas.append(mahsulot1)
# if len(mavjud_emas)==0:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda yo`q")
# else:
#     print(f"Quyidagi mahsulotlar do`konimizda bor.")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# foydalanuvchi=["mail","uzbek","surket","jonona"]
# logi=input("Yangi login kiriting: ").lower()
# if logi in foydalanuvchi:
#     print("Bu login band.")
# else:
#     print(f"Xush kelibsiz hurmatli {logi} ")
# son = float(input("Juft son kiriting: "))
# if (son % 2) == 0:
#     print("Bu son juft son.")
# else:
#     print("Rahmat!")

# yosh = int(input("Yoshingiz nechida?"))
#
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}')
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n + 1}-mahsulotni qo\' shing: '))
#
#     bor_mahsulotlar = []
#     mavjud_emas = []
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             bor_mahsulotlar.append(mahslot)
#         else:
#             mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# users = ['alisher1983','aziza','yasina', 'umar']
#
# login = input("Yangi login tanlang:")
#
# if login.lower() in users:
#     print(login)
#     print('Login band, yangi login tanalang!')
#
# else:
#     print("Xush kelibsiz!")
car={'model':"Ferrary",
     'rang':"qizil",
     'Tezlik':"500"}
print(car['model'])
print(f"Modeli {car['model']} rangi {car['rang']} Tezligi {car.get('Tezlik')}")

