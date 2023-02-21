class pesonaje:
#atributos del pesonaje
especie="humano"
nombre="Octane"
altura=1.85

#metoods personaje
 def correr(self,status):
     if(status):
         print("el personaje"+self.nombre+"esta corriendo")
    else:
        print("el personaje"+self.nombre+"se detuvo")

#metodo lanzar granada

def lanzarGranada (self):
    print("se lanzo granada")

#metodo recargar arma

def recargarArma(self,municiones):
    cargador=30
    cargador = cargador + municiones 
    print("el arma tiene ahora"+cargador+"balas")