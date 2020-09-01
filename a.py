while True:
    a = int(input("presione para ingresar 1(alumno) o 2(profesor): "))
    if a == 1:
        print("Alumno: ")
        i = int(input("Ingrese dni: "))
        j = input("Ingrese nombre del alumno: ")
        k = int(input("Ingrese edad: "))
        l = print("Ingrese notas: ")
        while True:
            while True:
                try:
                    a = int(input("nota-1: "))
                    break
                except ValueError:
                    print("vuelva a ingresar ")
        
        
            while True:
                try:    
                    b = int(input("nota-2: "))
                    break
                except ValueError:
                    print("vuelva a ingresar")
            
            
            while True:
                try:    
                    c = int(input("nota-3: "))
                    break
                except ValueError:
                    print("vuelva a ingresar")
     
        
            while True:
                try:    
                    d = int(input("nota-4: "))
                    break
                except ValueError:
                    print("vuelva a ingresar")
            break

        x = [a, b, c, d]
        suma = 0
        I = 0
        for z in x:
            suma += z
            I += 1
        promedio = suma / I    

        mayor = max(x)
        menor = min(x)

        archivo = open("Alumnos.txt","a")
        archivo.write("---------nuevo alumno---------\n")
        archivo.write(j + '\n')
        archivo.write('edad= %s ,'%k)
        archivo.write('DNI= %s ,'%i)
        archivo.write('notas= %s ,'%x)
        archivo.write('nota mayor= %s ,'%mayor)
        archivo.write('nota menor= %s ,'%menor)
        archivo.write('promedio= %s '%promedio)
        archivo.write("\n")
        
        archivo.close()

        break
        
            
    elif a == 2 :
        print("Docente: ")
        i = int(input("Ingrese dni: "))
        j = input("Ingrese nombre del docente: ")
        k = int(input("Ingrese edad: "))

        archivo = open("Docentes.txt","a")
        archivo.write("---------nuevo docente---------\n")
        archivo.write(j + '\n')
        archivo.write('edad= %s ,'%k)
        archivo.write('DNI= %s '%i)
        archivo.write("\n")
        
        archivo.close()

        
        break

    else:
        print("vuelva a ingresar ")


print(f"_________Los datos son_________")    
B = [i, j, k]
class A:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def dni(self):
        print(f"DNI: {self.i}")
    def nombre(self):
        print(f"nombre: {self.j}")
    def edad(self):
        print(f"edad: {self.k}")

class alumno(A):
    pass
class docente(A):
    pass

alumno_1 = alumno(i, j, k)

alumno_1.dni()

alumno_1.nombre()
  
alumno_1.edad() 





        




