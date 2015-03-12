import time
import thread
from collections import deque

cola=deque([])
personas=0
caja1=0
caja2=0
caja3=0
caja4=0
i=0

Npersona=["Pedro","Luis","Juan","Alberto","Abiu","Julian","Jorge"]

def tiempo_persona(Tpersona, Npersona):
    global personas
    for i in Npersona:
        time.sleep(Tpersona)
        cola.append(i)
        print i+" llego al banco!\n"

def tiempo_caja1(Tcaja1):
    global caja1
    time.sleep(Tcaja1)
    caja1=0
    print "Caja 1 vacia!\n"

def tiempo_caja2(Tcaja2):
    global caja2
    time.sleep(Tcaja2)
    caja2=0
    print "Caja 2 vacia!\n"


def tiempo_caja3(Tcaja3):
    global caja3
    time.sleep(Tcaja3)
    caja3=0
    print "Caja 3 vacia!\n"

def tiempo_caja4(Tcaja4):
    global caja4
    time.sleep(Tcaja4)
    caja4=0
    print "Caja 4 vacia!\n"

def persona_a_caja(cola):
    global caja1, caja2, caja3, caja4, Tcaja1, Tcaja2, Tcaja3, Tcaja4
    aux=''
    if(cola_vacia(cola)==False and caja1==0):
        aux=cola.popleft()
        caja1=1
        print "Persona a caja 1: "+aux
        tiempo_caja1(Tcaja1)
    elif(cola_vacia(cola)==False and caja2==0):
        aux=cola.popleft()
        caja2=1
        print "Persona a caja 2: "+aux
        tiempo_caja2(Tcaja2)
    elif(cola_vacia(cola)==False and caja3==0):
        aux=cola.popleft()
        caja3=1
        print "Persona a caja 3: "+aux
        tiempo_caja3(Tcaja3)
    elif(cola_vacia(cola)==False and caja4==0):
        aux=cola.popleft()
        caja4=1
        print "Persona a caja 4: "+aux
        tiempo_caja4(Tcaja4)
    #else:
        #print "Esperando"
    #elif(cola_vacia(cola)==True and (caja1==0 and caja2==0 and caja3==0 and caja4==0)):
        #print "Hay nadie en la cola y la cajas estan vacias"
    #elif(cola_vacia(cola)!=True and (caja1!=0 or caja2!=0 or caja3!=0 or caja4!=0)):
        #print str(cola)+" estan en la cola y no hay cajas libres"
    

def cola_vacia(cola):
    if not cola:
        return True
    else:
        return False

def tiempos():
    persona_a_caja(cola)
    #thread.start_new_thread(persona_a_caja,(cola,))
    time.sleep(2)
    #thread.start_new_thread(tiempo_caja1, (Tcaja1,))
    #thread.start_new_thread(tiempo_caja2, (Tcaja2,))
    #thread.start_new_thread(tiempo_caja3, (Tcaja3,))
    #thread.start_new_thread(tiempo_caja4, (Tcaja4,))
    
Tpersona=int(raw_input("Ingrese tiempo (segundos) en el cual una persona llegara al banco: ")) 
#Npersona=int(raw_input("Ingrese el numero de personas: "))
#Tcaja=int(raw_input("Ingrese tiempo (segundos) en el que una caja tarda en atender a alguien: "))
Tcaja1=20
Tcaja2=15
Tcaja3=35
Tcaja4=5
thread.start_new_thread(tiempo_persona, (Tpersona,Npersona))
print "Esperando banco\n"
time.sleep(5)
while True:
    tiempos()

