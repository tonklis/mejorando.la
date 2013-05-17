class Estudiante:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def imprime(self):
    #print "Me llamo %s y tengo %i" % (self.nombre, self.edad),
    return "Me llamo %s y tengo %i" % (self.nombre, self.edad)

def main():
  e = Estudiante("Benjamin", 30)
  e.imprime()

  freddier = Estudiante("Freddier", 2000)
  cadena = freddier.imprime()
  print cadena

main()
