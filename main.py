dia = int(input())
mes = int(input())

if (dia >= 21 and dia <= 31 and mes == 3) or (dia >= 1 and dia <=19 and mes == 4):
    print("tu signo es aries")
elif (dia >= 20 and dia <= 30 and mes == 4) or (dia >= 1 and dia <=20 and mes == 5):
    print("tu signo es tauro")
elif (dia >= 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia <=20 and mes == 6):
    print("tu signo es geminis")  
elif (dia >= 21 and dia <= 30 and mes == 6) or (dia >= 1 and dia <=22 and mes == 7):
    print("tu signo es cancer")    
elif (dia >= 23 and dia <= 31 and mes == 7) or (dia >= 1 and dia <=22 and mes == 8):
    print("tu signo es leo")
elif (dia >= 23 and dia <= 31 and mes == 8) or (dia >= 1 and dia <=22 and mes == 9):
    print("tu signo es virgo")
elif (dia >= 23 and dia <= 30 and mes == 9) or (dia >= 1 and dia <=22 and mes == 10):
    print("tu signo es libra")
elif (dia >= 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia <=21 and mes == 11):
    print("tu signo es escorpion")
elif (dia >= 22 and dia <= 30 and mes == 11) or (dia >= 1 and dia <=21 and mes == 12):
    print("tu signo es sagitario")
elif (dia >= 22 and dia <= 31 and mes == 12) or (dia >= 1 and dia <=19 and mes == 1):
    print("tu signo es capricornio")
elif (dia >= 20 and dia <= 31 and mes == 1) or (dia >= 1 and dia <=18 and mes == 2):
    print("tu signo es acuario")
elif (dia >= 19 and dia <= 28 and mes == 2) or (dia >= 1 and dia <=20 and mes == 3):
    print("tu signo es piscis")
else:
    print("fecha invalida xv")