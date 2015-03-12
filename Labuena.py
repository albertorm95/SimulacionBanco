import time
import thread
import Queue
from collections import deque

cola=deque([])
personas=0
caja=0
i=0

Npersona=["Pedro","Luis","Juan","Alberto","Abiu"]

def tiempo_persona(Tpersona, Npersona):
    print " TIEMPO PERSONA \n"
    global personas
    for i in Npersona:
        time.sleep(Tpersona)
        cola.append(i)
        print str(cola)+" En la cola"

def tiempo_caja(Tcaja):
    print " TIEMPO CAJA \n"
    global caja
    time.sleep(Tcaja)
    caja=0
    print str(caja)+" Caja vacia"

def persona_a_caja(cola):
    print " PERSONA A CAJA \n"
    global caja
    if(cola_vacia(cola)!=True and caja==0):
        cola.popleft()
        caja=1
        print "Persona a caja"+str(cola)+"Cola"
    else:
        print "Esperando en cola"

def cola_vacia(cola):
    if not cola:
        return True
    else:
        return False


def tiempos():   
    time.sleep(5)
    print "Esperando banco"
    thread.start_new_thread(persona_a_caja,(cola,))
    time.sleep(2)
    print "Persona caminando a caja"
    thread.start_new_thread(tiempo_caja, (Tcaja,))
    
Tpersona=int(raw_input("Ingrese tiempo (segundos) en el cual una persona llegara al banco: ")) 
#Npersona=int(raw_input("Ingrese el numero de personas: "))
Tcaja=int(raw_input("Ingrese tiempo (segundos) en el que una caja tarda ena tender a alguien: "))
thread.start_new_thread(tiempo_persona, (Tpersona,Npersona))
while True:
    tiempos()



