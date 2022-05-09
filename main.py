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

