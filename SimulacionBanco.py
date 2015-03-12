from __future__ import print_function
import time
import thread
import random
from collections import deque
from colorconsole import terminal

def tiempo_persona(Tpersona, Npersona):
    for persona in Npersona:
        time.sleep(Tpersona)
        cola.append(persona)
        screen.set_color(15)
        strinp=persona+" llego al banco!"
        screen.print_at(5,5,"                      ")
        screen.print_at(5,5,strinp)
        #print persona+" llego al banco!"

def tiempo_caja(Tcaja, ubicacion):
    global caja
    time.sleep(Tcaja)
    caja[ubicacion]=0
    cajaestado(ubicacion)
    strinc="Caja "+str(ubicacion+1)+" vacia!"
    screen.set_color(15)
    screen.print_at(5,7,"                          ")
    screen.print_at(5,7,strinc)
    #print "Caja "+str(ubicacion+1)+" vacia!\n"

def persona_a_caja(cola,ubicacion):
    global caja, Tcaja
    aux=''
    if(cola_vacia(cola)==False and caja[0]==0):
        #cola.popleft()
        aux=cola.popleft()
        caja[0]=1
        strinp="Persona a caja 1: "+aux+"\n"
        screen.set_color(15)
        screen.print_at(5,6,"                          ")
        screen.print_at(5,6,strinp)
        #print "Persona a caja 1: "+aux+"\n"
        ubicacion=0
        cajaestado(ubicacion)
        time.sleep(5)
        tiempo_caja(Tcaja, ubicacion)
        
    elif(cola_vacia(cola)==False and caja[1]==0):
        #cola.popleft()
        aux=cola.popleft()
        caja[1]=1
        strinp="Persona a caja 2: "+aux+"\n"
        screen.set_color(15)
        screen.print_at(5,6,"                          ")
        screen.print_at(5,6,strinp)
        #print "Persona a caja 2: "+aux+"\n"
        ubicacion=1
        cajaestado(ubicacion)
        tiempo_caja(Tcaja, ubicacion)
        
    elif(cola_vacia(cola)==False and caja[2]==0):
        #cola.popleft()
        aux=cola.popleft()
        strinp="Persona a caja 3: "+aux+"\n"
        screen.set_color(15)
        screen.print_at(5,6,"                          ")
        screen.print_at(5,6,strinp)
        caja[2]=1
        #print "Persona a caja 3: "+aux+"\n"
        ubicacion=2
        cajaestado(ubicacion)
        tiempo_caja(Tcaja, ubicacion)
        
    elif(cola_vacia(cola)==False and caja[3]==0):
        #cola.popleft()
        aux=cola.popleft()
        strinp="Persona a caja 4: "+aux+"\n"
        screen.set_color(15)
        screen.print_at(5,6,"                          ")
        screen.print_at(5,6,strinp)
        caja[3]=1
        #print "Persona a caja 4: "+aux+"\n"
        ubicacion=3
        cajaestado(ubicacion)
        tiempo_caja(Tcaja, ubicacion)

def cola_vacia(cola):
    if not cola:
        return True
    else:
        return False

def cajaestado(ubicacion):
    global caja
    if caja[ubicacion]==0:
        screen.set_color(2)
        if ubicacion==0:
            for i in range(3,7):
                screen.print_at(57,i, 'XXXXXX')
        elif ubicacion==1:
            for i in range(8,12):
                screen.print_at(57,i, 'XXXXXX')            
        elif ubicacion==2:
            for i in range(13,17):
                screen.print_at(57,i, 'XXXXXX')            
        elif ubicacion==3:
            for i in range(18,22):
                screen.print_at(57,i, 'XXXXXX')
    elif caja[ubicacion]==1:
        screen.set_color(4)
        if ubicacion==0:
            for i in range(3,7):
                screen.print_at(57,i, 'XXXXXX')
        elif ubicacion==1:
            for i in range(8,12):
                screen.print_at(57,i, 'XXXXXX')            
        elif ubicacion==2:
            for i in range(13,17):
                screen.print_at(57,i, 'XXXXXX')            
        elif ubicacion==3:
            for i in range(18,22):
                screen.print_at(57,i, 'XXXXXX')

def Proceso(): 
    thread.start_new_thread(tiempo_persona, (Tpersona,Npersona,))
    #print "Esperando banco\n"
    time.sleep(5)
    while True:
        #Tcaja=random.randint(5,35)
        thread.start_new_thread(persona_a_caja,(cola,ubicacion))
        time.sleep(2)    

#Screen    
screen = terminal.get_terminal(conEmu=False)
screen.clear()
screen.set_title("BANCO")

#Variables
cola=deque([])
caja=[0,0,0,0]
ubicacion=0
Npersona=["Pedro","Luis","Juan","Alberto","Abiu","Julian","Jorge"]
Tcaja=random.randint(5,35)

#Main
Tpersona=int(raw_input("Ingrese tiempo (segundos) en el cual una persona llegara al banco: "))
screen.print_at(0,0,"Simulacion de Banco\n")

print(' +--------------------------------------------------------------+\n',
      '|                                                              |\n',
      '|                                                       XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '|                                                              |\n',
      '|                                                       XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '| +------------------------------------------->         XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '| * * * * * * * * * * * * * * * * * * * * * * *                |\n',
      '|                                                       XXXXXX |\n',
      '| +------------------------------------------->         XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '|                                                              |\n',
      '|                                                       XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '|                                                       XXXXXX |\n',
      '|                                                              |\n',
      '+--------------------------------------------------------------+\n')
Proceso()

    






























    

