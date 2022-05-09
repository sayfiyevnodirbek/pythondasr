son= int(input("Biror bir son kiriting: "))
if son%2==0:
    print("Bu son juft.")
else:
    print("Bu son toq son.")
yosh=int(input("Sizning yoshingiz nechada: "))
if yosh<=4 or yosh>=60:
    narh=0
elif yosh<=18:
    narh=10000
elif yosh>18:
    narh=20000
print(f"Siz uchun muzeyga kirish narxi {narh} so`m")
son1=int(input("Birinchi sonni kiriting: "))
son2=int(input("Ikkinchi sonni kiriting: "))
if son1>son2:
    print(f"Birinchi {son1} soni ikkinchi {son2} sonidan katta")
elif son1==son2:
    print(f"Birinchi {son1} soni ikkinchi {son2} soniga teng")
else:print(f"Ikkinchi {son2} soni birinchi {son1} sonidan katta")
