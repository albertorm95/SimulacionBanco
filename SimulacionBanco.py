from __future__ import print_function
import time
import thread
import random
from collections import deque
from colorconsole import terminal

def tiempo_persona(Npersona):
    for persona in Npersona:
        Tpersona=random.randint(1,7)
        time.sleep(Tpersona)
        cola.append(persona)
        personaestado(cola)
        screen.set_color(15)
        strinp="    "+persona+" llego al banco!  \n"
        screen.print_at(0,5,"                                       \n")
        screen.print_at(0,5,strinp)

def tiempo_caja(Tcaja, ubicacion):
    global caja
    time.sleep(Tcaja)
    caja[ubicacion]=0
    cajaestado(ubicacion)
    strinc="    Caja "+str(ubicacion+1)+" vacia!                                                                                    "
    screen.set_color(15)
    screen.print_at(0,7,strinc)

def persona_a_caja(cola,ubicacion):
    global caja
    Tcaja=random.randint(10,45)
    aux=''
    if(cola_vacia(cola)==False and caja[0]==0):
        aux=cola.popleft()
        personaestado(cola)
        caja[0]=1
        strinp="    Persona a caja 1: "+aux+"        \n"
        screen.set_color(15)
        screen.print_at(0,6,"                                       \n")
        screen.print_at(0,6,strinp)
        ubicacion=0
        cajaestado(ubicacion)
        time.sleep(5)
        tiempo_caja(Tcaja, ubicacion)
        
    elif(cola_vacia(cola)==False and caja[1]==0):
        aux=cola.popleft()
        personaestado(cola)
        caja[1]=1
        strinp="    Persona a caja 2: "+aux+"\n"
        screen.set_color(15)
        screen.print_at(0,6,"                                       \n")
        screen.print_at(0,6,strinp)
        ubicacion=1
        cajaestado(ubicacion)
        tiempo_caja(Tcaja, ubicacion)
        
    elif(cola_vacia(cola)==False and caja[2]==0):
        aux=cola.popleft()
        personaestado(cola)
        strinp="    Persona a caja 3: "+aux+"\n"
        screen.set_color(15)
        screen.print_at(0,6,"                                       \n")
        screen.print_at(0,6,strinp)
        caja[2]=1
        ubicacion=2
        cajaestado(ubicacion)
        tiempo_caja(Tcaja, ubicacion)
        
    elif(cola_vacia(cola)==False and caja[3]==0):
        aux=cola.popleft()
        personaestado(cola)
        strinp="    Persona a caja 4: "+aux+"\n"
        screen.set_color(15)
        screen.print_at(0,6,"                                       \n")
        screen.print_at(0,6,strinp)
        caja[3]=1
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
        screen.set_color(10)
        if ubicacion==0:
            screen.print_at(56,3, 'XXXXXX               \n')
            screen.print_at(56,4, 'XXXXXX               \n')
            screen.print_at(56,5, 'XXXXXX               \n')
            screen.print_at(56,6, 'XXXXXX               \n')
        elif ubicacion==1:
             screen.print_at(56,8, 'XXXXXX               \n')
             screen.print_at(56,9, 'XXXXXX               \n')
             screen.print_at(56,10, 'XXXXXX               \n')
             screen.print_at(56,11, 'XXXXXX               \n')            
        elif ubicacion==2:
            screen.print_at(56,13, 'XXXXXX               \n')
            screen.print_at(56,14, 'XXXXXX               \n')
            screen.print_at(56,15, 'XXXXXX               \n')
            screen.print_at(56,16, 'XXXXXX               \n')  
        elif ubicacion==3:
            screen.print_at(56,18, 'XXXXXX               \n')
            screen.print_at(56,19, 'XXXXXX               \n')
            screen.print_at(56,20, 'XXXXXX               \n')
            screen.print_at(56,21, 'XXXXXX               \n')
    elif caja[ubicacion]==1:
        screen.set_color(12)
        if ubicacion==0:
            screen.print_at(56,3, 'XXXXXX               \n')
            screen.print_at(56,4, 'XXXXXX               \n')
            screen.print_at(56,5, 'XXXXXX               \n')
            screen.print_at(56,6, 'XXXXXX               \n')
        elif ubicacion==1:
            screen.print_at(56,8, 'XXXXXX               \n')
            screen.print_at(56,9, 'XXXXXX               \n')
            screen.print_at(56,10, 'XXXXXX               \n')
            screen.print_at(56,11, 'XXXXXX               \n')           
        elif ubicacion==2:
            screen.print_at(56,13, 'XXXXXX               \n')
            screen.print_at(56,14, 'XXXXXX               \n')
            screen.print_at(56,15, 'XXXXXX               \n')
            screen.print_at(56,16, 'XXXXXX               \n')             
        elif ubicacion==3:
            screen.print_at(56,18, 'XXXXXX               \n')
            screen.print_at(56,19, 'XXXXXX               \n')
            screen.print_at(56,20, 'XXXXXX               \n')
            screen.print_at(56,21, 'XXXXXX               \n')
def personaestado(cola):
    encola=len(cola)
    if encola<1:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
    elif encola==1:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(45,12,' *\n')
    elif encola==2:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(43,12,' * *\n')
    elif encola==3:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(41,12,' * * *\n')
    elif encola==4:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(39,12,' * * * *\n')
    elif encola==5:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(37,12,' * * * * *\n')
    elif encola==6:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(35,12,' * * * * * *\n')
    elif encola==7:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(33,12,' * * * * * * *\n')
    elif encola==8:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(31,12,' * * * * * * * *\n')
    elif encola==9:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(29,12,' * * * * * * * * *\n')
    elif encola==10:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(27,12,' * * * * * * * * * *\n')
    elif encola==11:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(25,12,' * * * * * * * * * * *\n')
    elif encola==12:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(23,12,' * * * * * * * * * * * *\n')
    elif encola==13:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(21,12,' * * * * * * * * * * * * *\n')
    elif encola==14:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(19,12,' * * * * * * * * * * * * * *\n')
    elif encola==15:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(17,12,' * * * * * * * * * * * * * * *\n')
    elif encola==16:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(15,12,' * * * * * * * * * * * * * * * *\n')
    elif encola==17:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(13,12,' * * * * * * * * * * * * * * * * *\n')
    elif encola==18:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(11,12,' * * * * * * * * * * * * * * * * * *\n')
    elif encola==19:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(9,12,' * * * * * * * * * * * * * * * * * * *\n')
    elif encola==20:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(7,12,' * * * * * * * * * * * * * * * * * * * *\n')
    elif encola==21:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(5,12,' * * * * * * * * * * * * * * * * * * * * *\n')
    elif encola==22:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(3,12,' * * * * * * * * * * * * * * * * * * * * * *\n')
    elif encola==23:
        screen.set_color(0)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')
        screen.set_color(9)
        screen.print_at(1,12,' * * * * * * * * * * * * * * * * * * * * * * *\n')

def Proceso(): 
    thread.start_new_thread(tiempo_persona, (Npersona,))
    time.sleep(5)
    while True:
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
Npersona=["Pedro","Luis","Juan","Alberto","Abiu","Julian","Jorge","Daniela","Karla","Alejandro","Sandra","Jose","Fulanito","Leonardo","Andrea","Blanca","Gabriela","Maria","Paula","Isabel","Eduardo","Elena","Ingrid"]

#Main
screen.set_color(15)
screen.clear()
screen.print_at(0,0,"Simulacion de Banco\n")

print(' +--------------------------------------------------------------+\n',
      '                                                              \n',
      '                                                       XXXXXX \n',
      '                                                       XXXXXX \n',
      '                                                       XXXXXX \n',
      '                                                       XXXXXX \n',
      '                                                              \n',
      '                                                       XXXXXX \n',
      '                                                       XXXXXX \n',
      ' +------------------------------------------->         XXXXXX \n',
      '                                                       XXXXXX \n\n',
      '                                                       XXXXXX \n',
      ' +------------------------------------------->         XXXXXX \n',
      '                                                       XXXXXX \n',
      '                                                       XXXXXX \n',
      '                                                              \n',
      '                                                       XXXXXX \n',
      '                                                       XXXXXX \n',
      '                                                       XXXXXX \n',
      '                                                       XXXXXX \n',
      '                                                              \n',
      '+--------------------------------------------------------------+')
Proceso()






























    

