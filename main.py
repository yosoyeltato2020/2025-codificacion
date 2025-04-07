print("Códigos ASCII")
for i in range(256):
    if i % 6 == 0:
        print() 
        print()
    if 32 <= i <= 255:
        print(f"{str(i).ljust(15)}: {chr(i)}", end="\t")
    else:
        pass
        # print(f"{str(i).ljust(20)}: no imprimible", end="\t")
