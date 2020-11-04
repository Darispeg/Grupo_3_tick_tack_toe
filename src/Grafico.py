from tkinter import *
import Rules
import Board

# ----------------------
Board.inicializar()
fichasEnTablero=0
#-----------------------

raiz = Tk()
raiz.geometry("500x470+550+150")
raiz.config(bg="#4431AE")
raiz.resizable(False, False)
raiz.iconbitmap("src\Image\ia.ico")
raiz.title("3 en Raya")
miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(cursor="hand2")
miFrame.config(bg="#4431AE")

miNombre = StringVar()
txtNombre = Entry(miFrame, textvariable=miNombre)

libre = PhotoImage(file="src\Image\cargando.png")
rick = PhotoImage(file="src\Image\Sanchez-rick.png")
morty = PhotoImage(file="src\Image\morty.png")

def iniciaMaquina():
    casilla2=Rules.colocarFichaMaquina('O','X',Board.tablero)
    cambiarMorti(casilla2)
    Board.casillasVacias.remove(casilla2)
    btoIniciaMaquina.config(state="disabled")

#-------------------Fila Inicio-------------------------------
nombreLabel = Label(miFrame, text="Nombre: ", font=("Comic Sans MS",15), background="#4431AE")
nombreLabel.grid(row=0, column=1)
textPantalla = Entry(miFrame, font=("Comic Sans MS",12))
textPantalla.grid(row=0, column=2, columnspan=2)
textPantalla.config(background="#252526", fg="#03f943", justify="center")
btoIniciaMaquina = Button(miFrame,text="Inicia Maquina", bg="#574F7D", width=28, font=("Comic Sans MS",12), command=iniciaMaquina)
btoIniciaMaquina.grid(row=1,column=1,columnspan=3)
#--------------------------------------------------------

def cambiarMorti(casilla):
    if casilla == 0:
        botonPos1.config(image=morty, state="disabled")
    if casilla == 1:
        botonPos2.config(image=morty, state="disabled")
    if casilla == 2:
        botonPos3.config(image=morty, state="disabled")
    if casilla == 3:
        botonPos4.config(image=morty, state="disabled")
    if casilla == 4:
        botonPos5.config(image=morty, state="disabled")
    if casilla == 5:
        botonPos6.config(image=morty, state="disabled")
    if casilla == 6:
        botonPos7.config(image=morty, state="disabled")
    if casilla == 7:
        botonPos8.config(image=morty, state="disabled")
    if casilla == 8:
        botonPos9.config(image=morty, state="disabled")



def cambiarRick(boton, _row, _column):
    btoIniciaMaquina.config(state="disabled")
    maquina=False 
    humano=False
    boton.config(image=rick)
    casilla=Rules.colocarFicha('X',_row-2,_column-1)
    Board.casillasVacias.remove(casilla)
    if(Rules.hemosGanado(casilla,'X',Board.tablero)):
        humano = True
        ganaste(maquina, humano)
    else:
        if len(Board.casillasVacias) <= 0 :
            ganaste(maquina, humano)
            congelar()
        else:
            casilla2=Rules.colocarFichaMaquina('O','X',Board.tablero)
            cambiarMorti(casilla2)
            Board.casillasVacias.remove(casilla2)
            if(Rules.hemosGanado(casilla2,'O',Board.tablero)):
                maquina = True
                ganaste(maquina, humano)


# ------------------Fila 1-------------------------------
botonPos1 = Button(miFrame, image=libre, bg="#293C65", width=96, command=lambda:cambiarRick(botonPos1, 2, 1))
botonPos1.grid(row=2,column=1)
botonPos2 = Button(miFrame, image=libre, bg="#293C65", width=96, command=lambda:cambiarRick(botonPos2, 2, 2))
botonPos2.grid(row=2,column=2)
botonPos3 = Button(miFrame, image=libre, bg="#293C65", width=96, command=lambda:cambiarRick(botonPos3, 2, 3))
botonPos3.grid(row=2,column=3)

# ------------------Fila 2-------------------------------
botonPos4 = Button(miFrame, image=libre, bg="#293C65", width=96, command=lambda:cambiarRick(botonPos4, 3, 1))
botonPos4.grid(row=3,column=1)
botonPos5 = Button(miFrame, image=libre, bg="#293C65", width=96, command=lambda:cambiarRick(botonPos5, 3, 2))
botonPos5.grid(row=3,column=2)
botonPos6 = Button(miFrame, image=libre, bg="#293C65", width=96, command=lambda:cambiarRick(botonPos6, 3, 3))
botonPos6.grid(row=3,column=3)

# ------------------Fila 3-------------------------------
botonPos7 = Button(miFrame, image=libre, bg="#293C65", width=96, command=lambda:cambiarRick(botonPos7, 4, 1))
botonPos7.grid(row=4,column=1)
botonPos8 = Button(miFrame, image=libre, bg="#293C65", width=96, command=lambda:cambiarRick(botonPos8, 4, 2))
botonPos8.grid(row=4,column=2)
botonPos9 = Button(miFrame, image=libre, bg="#293C65", width=96, command=lambda:cambiarRick(botonPos9, 4, 3))
botonPos9.grid(row=4,column=3)


# ----------------Fila Ganador -----------------------------
ganasteLabel = Label(miFrame, font=("Comic Sans MS",15), bg="#4431AE")


def ganaste(maquina, humano):
    congelar()
    if maquina:
        ganasteLabel.config(text='Ganador: Maquina',fg="red")
        ganasteLabel.grid(row=5, column=1, columnspan=3)
    if humano:
        miNombre.set(textPantalla.get())
        ganasteLabel.config(text='Ganador: ' + str(textPantalla.get()))
        ganasteLabel.grid(row=5, column=1, columnspan=3)
    if not maquina and not humano:
        ganasteLabel.config(text='Empate', fg="green")
        ganasteLabel.grid(row=5, column=1, columnspan=3)
    
    btoReiniciar = Button(miFrame, text="Reiniciar", width=28, font=("Comic Sans MS",12), bg="green", command=reiniciarJuego)
    btoReiniciar.grid(row=6, column=1, columnspan=3)

def reiniciarJuego():
    Board.inicializar()
    iniciarImagenes()
    ganasteLabel.config(text="")


def iniciarImagenes():
    botonPos1.config(image=libre, state="normal")
    botonPos2.config(image=libre, state="normal")
    botonPos3.config(image=libre, state="normal")
    botonPos4.config(image=libre, state="normal")
    botonPos5.config(image=libre, state="normal")
    botonPos6.config(image=libre, state="normal")
    botonPos7.config(image=libre, state="normal")
    botonPos8.config(image=libre, state="normal")
    botonPos9.config(image=libre, state="normal")
    btoIniciaMaquina.config(state="normal")

def congelar():
    botonPos1.config(state="disabled")
    botonPos2.config(state="disabled")
    botonPos3.config(state="disabled")
    botonPos4.config(state="disabled")
    botonPos5.config(state="disabled")
    botonPos6.config(state="disabled")
    botonPos7.config(state="disabled")
    botonPos8.config(state="disabled")
    botonPos9.config(state="disabled")

#------------------------------------------------------------
raiz.mainloop()
