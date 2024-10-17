# p--> capital incial--> El dinero que tienes en el banco
# t--> años
# r--> Interés anual en %
# n--> nº de periodos por año
# a--> capital final
def calcularinteres(p,r,t,n):   
    A=p*(1+r/n)**(n*t)
    return A
p=float(input("capital inicial"))
r=float(input("interes anual en %"))
t=float(input("numero de años"))
n=float(input("numero de periodos por año"))

capitalfinal = calcularinteres(p,r,t,n)

capitalfinal = calcularinteres(p,r,1,n)
print(f"la cantidad final despues de {1} años sera {capitalfinal}")
capitalfinal = calcularinteres(p,r,2,n)
print(f"la cantidad final despues de {2} años sera {capitalfinal}")
capitalfinal = calcularinteres(p,r,3,n)
print(f"la cantidad final despues de {3} años sera {capitalfinal}")
capitalfinal = calcularinteres(p,r,4,n)
print(f"la cantidad final despues de {4} años sera {capitalfinal}")
capitalfinal = calcularinteres(p,r,5,n)
print(f"la cantidad final despues de {5} años sera {capitalfinal}")
capitalfinal = calcularinteres(p,r,6,n)
print(f"la cantidad final despues de {6} años sera {capitalfinal}")
capitalfinal = calcularinteres(p,r,7,n)
print(f"la cantidad final despues de {7} años sera {capitalfinal}")
capitalfinal = calcularinteres(p,r,8,n)
print(f"la cantidad final despues de {8} años sera {capitalfinal}")
capitalfinal = calcularinteres(p,r,9,n)
print(f"la cantidad final despues de {9} años sera {capitalfinal}")
capitalfinal = calcularinteres(p,r,10,n)
print(f"la cantidad final despues de {10} años sera {capitalfinal}")

