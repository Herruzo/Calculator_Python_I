from tkinter import*
raiz=Tk() # Llamamos a la clase y creamos una ventana
raiz.iconbitmap('logo-recortado.ico') # Insertamos un icono
raiz.title('Calculator') # Le ponemos un título
raiz.geometry('200x250') # Le damos unas dimensiones a la raíz
#--------------------Creamos el Frame-------------------------
miFrame=Frame(raiz) # Creamos un frame
miFrame.pack() # Lo empaquetamos en la raíz

operacion='' # Inicializamos la variable operación como una cadena vacía.
# Al pulsar una operación +,-,*,/ la variable operación cambie, gracias a la función 

resultado=0 # Es aquí donde de va a ir almacenando la suma de los valores introducidos

reset_pantalla=True # Inicializamos una variable bandera con true, para indicar que la pantalla está en posición de reset.

punto=True # Inicializamos la variable para indicar el punto de los decimales

#--------------------Pantalla---------------
numPantalla=StringVar() # Indicamos que la variable numPantalla es un string.
pantalla=Entry(miFrame, textvariable=numPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #Para que el ancho de la pantalla ocupe 4 columnas utilizamos la instrucción columnspan = nº de columnas
pantalla.config(bg='black', fg='#03f943', justify='right') # A la pantalla le damos color de fondo, de fuente y que escriba por la derecha-izquierda.

numero_inicio=0 # Inicializamos la calculadora con un cero en la pantalla.
numPantalla.set(numero_inicio)
#es_cero = True

#-----------------Pulsaciones teclado----------------------
def numPulsado(num):
    # Llamamos a la variables globales que vamos a utilizar dentro de la función.
    global operacion
    global reset_pantalla    
    #global es_cero
    global punto
    # Con este condicional, decimos si en la pantalla no hay nada es_cero lo ponemos en False.
    # if es_cero:
    #     numPantalla.set('')
    #     es_cero = False
    
    if reset_pantalla==True: # Si la pantalla está en posición de reset...
        # Si al inicio de la calculadora y se presiona la coma, el valor de num pasa a ser '0.' 
        if num == '.':
            num = '0.'
            # Ponemos la variable punto en False para que no volvamos a poner otro punto en la pantalla.
            punto = False
            # Mostramos el num en pantalla
        numPantalla.set(num)
        reset_pantalla=False # Ponemos la pantalla en posición of reset
    else: # Pantalla posición of reset
        # Si presionamos '.' y la variable punto está en False: num no tiene valor
        if num=='.' and punto==False:
            num=''
        # De lo contrario num tiene el valor de '.'
        elif num=='.' and punto==True:
            num='.'
            # Y ponemos la variable punto en False
            punto=False
        # Insertamos el valor de la pantalla más el valor de num
        numPantalla.set(numPantalla.get() + num)
        

   

#-----------------------Función Suma-----------------------
def suma(numP):
    global operacion
    global resultado
    global reset_pantalla
    global punto
    try:
        if reset_pantalla==True: # Si la pantalla es True, la ponemos en False
            reset_pantalla=False
        punto=True # Ponemos punto en True para que después de presionar suma se pueda volver a poner decimales.

        if numPantalla.get().isdigit(): # Si en la pantalla hay solo número...
            num = int(numP) # Convertir en entero
        else:
            num = float(numP) # Si no en flotante
        resultado+=num
        operacion='suma' # Renombramos la variable operación con 'suma'
        reset_pantalla=True
        resultado = float(resultado) # Antes de usar el método is_interger(), convertimos el número en flotante para que no nos de una Excepción.
        # Para comprobar que un número es entero o flotante se usa la función is_interger(), que previamente lo hemos pasado a flotante, si el resultado después de la coma son 0, el número es entero y nos dará True.
        if resultado.is_integer():
            # Ahora lo converimos a entero.
            resultado = int(resultado)
        numPantalla.set(resultado) # El resultado lo insertamos en pantalla
    except:
        # En caso de alguna excepción, insertaremos en pantalla la palabre 'Error'
        numPantalla.set('Error')


#------------------------Función Raíz cuadrada-------------------

def raizCuadrada():
    
    global operacion
    global resultado
    global reset_pantalla
    try:
        if numPantalla.get().isdigit():
            num = int(numPantalla.get())
        else:
            num = float(numPantalla.get())
        resultado = num**0.5
        operacion='raiz'

        # Realizamos lo mismo para que no aparezcan decimales, si después de la coma son ceros.
        resultado = float(resultado)
        if resultado.is_integer():
            resultado = int(resultado)
        numPantalla.set(resultado)
        reset_pantalla=True
    except:
        numPantalla.set('Error')

#-----------------------Función Resta-----------------------
# Para las siguiente funciones de restar, multiplicar y dividir, creamos la variable num1 y el contador de las respectivas funciones.
num1=0
contador_resta=0
def resta(numP):
    global operacion
    global resultado
    global reset_pantalla
    global contador_resta
    global num1
    global punto
    try:
        punto=True
        if reset_pantalla==True:
            reset_pantalla=False
        if contador_resta==0: # Si el contador está a cero, el valor de resultado es el número pasado con numP

            if numPantalla.get().isdigit():
                num1 = int(numP)
                resultado=num1
            else:
                num1 = float(numP)
                resultado=num1

        else: # Si no...
            if contador_resta==1: # Si el contador es 1, resultado es el valor de num1 menos el valor de numP
                if numPantalla.get().isdigit(): # Aquí seleccionamos si el resultado en entero o flotante
                    resultado=num1-int(numP)
                else:
                    resultado=num1-float(numP)
                
            else:
                if numPantalla.get().isdigit():
                    resultado=int(resultado)-int(numP)
                else:
                    resultado=float(resultado)-float(numP)
            numPantalla.set(resultado) # Mostramos el resultado en pantalla
            #resultado=numPantalla.get()

        contador_resta=contador_resta+1 # al contador le sumamos 1
        operacion='resta'
        reset_pantalla=True
    except: # En esta excepción ponemos el contador en cero y la variable num1
        contador_resta=0
        num1=0
        numPantalla.set('Error')
     

#-----------------------Función Multiplicar-----------------------
contador_multi=0
def multi(numP):

    global operacion
    global resultado
    global reset_pantalla
    global contador_multi
    global num1
    global punto
    try:
        punto=True
        if reset_pantalla==True:
            reset_pantalla=False
        if contador_multi==0:

            if numPantalla.get().isdigit():
                num1 = int(numP)
                resultado=num1
            else:
                num1 = float(numP)
                resultado=num1

        else:
            if contador_multi==1:
                if numPantalla.get().isdigit():
                    resultado=num1*int(numP)
                else:
                    resultado=num1*float(numP)
                
            else:
                if numPantalla.get().isdigit():
                    resultado=int(resultado)*int(numP)
                else:
                    resultado=float(resultado)*float(numP)
            numPantalla.set(resultado)
            #resultado=numPantalla.get()

        contador_multi=contador_multi+1
        operacion='multi'
        reset_pantalla=True

    except:
        contador_multi=0
        num1=0
        numPantalla.set('Error')

#-----------------------Función Dividir-----------------------
contador_divi=0
def divi(numP):
    global operacion
    global resultado
    global reset_pantalla
    global contador_divi
    global num1
    global punto
    try:
        punto=True
        if reset_pantalla==True:
            reset_pantalla=False
        if contador_divi==0:

            if numPantalla.get().isdigit():
                num1 = int(numP)
                resultado=num1
            else:
                num1 = float(numP)
                resultado=num1

        else:
            if contador_divi==1:
                if numPantalla.get().isdigit():
                    resultado=num1/int(numP)
                else:
                    resultado=num1/float(numP)
                
            else:
                if numPantalla.get().isdigit():
                    resultado=int(resultado)/int(numP)
                else:
                    resultado=float(resultado)/float(numP)
            resultado = float(resultado)
            if resultado.is_integer():
                resultado = int(resultado)
            numPantalla.set(resultado)
            resultado=numPantalla.get()

        contador_divi=contador_divi+1
        operacion='divi'
        reset_pantalla=True

    except:
        contador_divi=0
        num1=0
        numPantalla.set('Error')
        

#----------------------Función Igual----------------------
def igual():
    global resultado
    global operacion
    global reset_pantalla
    global contador_resta
    global contador_multi
    global contador_divi
    global punto
    try:
        if numPantalla.get().isdigit(): # Convertimos la variable numero en entero o flotante según corresponda.
            numero = int(numPantalla.get())
        else:
            numero = float(numPantalla.get())

        if operacion=='suma':        
            resulSuma = resultado + numero
            resulSuma = float(resulSuma)
            if resulSuma.is_integer():
                resulSuma = int(resulSuma)
            numPantalla.set(resulSuma)
            resultado=0
            punto=True
            reset_pantalla=True
            
        elif operacion=='resta':
            # La resta la metemos dentro de la variable resta
            resta = resultado-numero
            # La convertimos en flotante
            resta = float(resta)
            # La condicionamos a que si tiene como decimal 0, se convierta en entero.
            if resta.is_integer():
                resta = int(resta)
            # Mostramos el resultado en pantalla.
            numPantalla.set(resta)
            resultado=0
            reset_pantalla=True
            contador_resta=0
        elif operacion=='multi':
            multi = resultado*numero
            multi = float(multi)
            if multi.is_integer():
                multi = int(multi)
            numPantalla.set(multi)
            resultado=0
            reset_pantalla=True
            contador_multi=0
        elif operacion=='divi':
            divi = resultado/numero
            divi = float(divi)
            if divi.is_integer():
                divi = int(divi)
            numPantalla.set(divi)
            resultado=0
            reset_pantalla=True
            contador_divi=0

    except:
        numPantalla.set('Error')
        contador_resta=0
        contador_multi=0
        contador_divi=0


#----------------------Función C y CE----------------------------------
def tecla_c():
    global reset_pantalla
    global punto
    global resultado
    global contador_resta
    global contador_multi
    global contador_divi
    reset_pantalla=True
    punto=True
    resultado=0
    numPantalla.set('0')
    contador_resta=0
    contador_multi=0
    contador_divi=0
def tecla_ce():
    global punto
    global reset_pantalla
    reset_pantalla=False
    punto=True
    numPantalla.set('')


#-------------------Fila 1 de botones----------------------
botonR=Button(miFrame, text='√', width=3, command=lambda:raizCuadrada()) # Ubicar los botones
botonR.grid(row=2, column=1)
botonCe=Button(miFrame, text='CE', width=3, command=lambda:tecla_ce())# Metemos la llamada a la función numPulsado() en una función lambda, para se ejecute solo cuando se presione la tecla.
botonCe.grid(row=2, column=2)
botonC=Button(miFrame, text='C', width=3, command=lambda:tecla_c())
botonC.grid(row=2, column=3)
botonDiv=Button(miFrame, text='/', width=3, command=lambda:divi(numPantalla.get()))
botonDiv.grid(row=2, column=4)

#-------------------Fila 3 de botones----------------------
boton7=Button(miFrame, text='7', width=3, command=lambda:numPulsado('7')) # Ubicar los botones
boton7.grid(row=3, column=1)
boton8=Button(miFrame, text='8', width=3, command=lambda:numPulsado('8'))# Metemos la llamada a la función numPulsado() en una función lambda, para se ejecute solo cuando se presione la tecla.
boton8.grid(row=3, column=2)
boton9=Button(miFrame, text='9', width=3, command=lambda:numPulsado('9'))
boton9.grid(row=3, column=3)
botonMult=Button(miFrame, text='X', width=3, command=lambda:multi(numPantalla.get()))
botonMult.grid(row=3, column=4)

#-------------------Fila 4 de botones--------
boton4=Button(miFrame, text='4', width=3, command=lambda:numPulsado('4')) # Ubicar los botones
boton4.grid(row=4, column=1)
boton5=Button(miFrame, text='5', width=3, command=lambda:numPulsado('5'))
boton5.grid(row=4, column=2)
boton6=Button(miFrame, text='6', width=3, command=lambda:numPulsado('6'))
boton6.grid(row=4, column=3)
botonRes=Button(miFrame, text='-', width=3, command=lambda:resta(numPantalla.get()))
botonRes.grid(row=4, column=4)

#-------------------Fila 5 de botones--------
boton1=Button(miFrame, text='1', width=3, command=lambda:numPulsado('1')) # Ubicar los botones
boton1.grid(row=5, column=1)
boton2=Button(miFrame, text='2', width=3, command=lambda:numPulsado('2'))
boton2.grid(row=5, column=2)
boton3=Button(miFrame, text='3', width=3, command=lambda:numPulsado('3'))
boton3.grid(row=5, column=3)
botonSum=Button(miFrame, text='+', width=3, command=lambda:suma(numPantalla.get()))
botonSum.grid(row=5, column=4)

#-------------------Fila 6 de botones--------

botonComa=Button(miFrame, text=',', width=3,  command=lambda:numPulsado('.')) # Ubicar los botones
botonComa.grid(row=6, column=1)
botonCero=Button(miFrame, text='0', width=3, command=lambda:numPulsado('0'))
botonCero.grid(row=6, column=2)
botonIgual=Button(miFrame, text='=', width=8, command=lambda:igual())
botonIgual.grid(row=6, column=3, columnspan=4)



raiz.mainloop()



