#creamos la clase
class Cuenta:
#creamos el constructor
#definimos los atributos como una funcion
    def __init__(self,titular,cantidad = 10000):#siempre iniciamos con init y dentro de los atributos primero siempre self
#estos son atributos de instancia
        self.titular = titular
        self.cantidad = cantidad
#ahora definimos los metodos como una funcion comun 
#en este caso son metodos sin argumentos
    def mostrar(self):
#describo lo que quiero mostrar cuando llame a la funcion mostrar()
        print("El titular de la cuenta es:",self.titular,"\nEl saldo de la cuenta es:$",self.cantidad)
    def ingresar(self,ingreso):
        total = 0
        if ingreso > 0:
            total = self.cantidad + ingreso
            print("El total de la cuenta es: ", total)
        else:
            return print("Digito mal el numero")
    def retirar(self, retiro):
        self.retiro = retiro
        if retiro > self.cantidad:
            print("Recuerde que esta retirando mas dinero del que cuenta en su caja\n",self.cantidad - self.retiro,"$ es el monto que le queda")
        else:
            return print("Usted quiere retirar $",self.retiro,"\nEl saldo de su cuenta es $",self.cantidad - self.retiro)
#creo el objeto cuenta1 y lo asocio a la clase Cuenta y le paso los parametros necesarios cuando cree la clase
cuenta1 = Cuenta("Facundo Cervera")
#con el objeto creado llamo a la funcion mostrar 
cuenta1.mostrar()
cuenta1.ingresar(-12)
cuenta1.ingresar(2000)

cuenta2 = Cuenta("Federico")
cuenta2.mostrar()
cuenta2.retirar(10001)
cuenta2.retirar(5000)


        