import time
import thread
import random
from collections import deque

cola=deque([])
caja=[0,0,0,0]
Tcaja=35

Npersona=["Pedro","Luis","Juan","Alberto","Abiu","Julian","Jorge"]

def tiempo_persona(Tpersona, Npersona):
    print "ENTRE A TPERSONA"
    for persona in Npersona:
        time.sleep(Tpersona)
        cola.append(persona)
        print persona+" llego al banco!\n"

def tiempo_caja(Tcaja,ubicacion,caja):
    print "ENTRE A TCAJA"
    time.sleep(Tcaja)
    caja[ubicacion]=0
    print "Caja "+str(ubicacion+1)+" 1 vacia!\n"

def persona_a_caja(cola, caja):
    print "ENTRE A PERSONA\n"
    aux=''
    print str(caja)+" CAJA"
    if(cola_vacia(cola)==False and caja[0]==0):
        aux=cola.popleft()
        caja[0]=1
        print "Persona a caja 1: "+aux
        ubicacion=0
        tiempo_caja(Tcaja,ubicacion,caja)
    elif(cola_vacia(cola)==False and caja[1]==0):
        aux=cola.popleft()
        caja[1]=1
        print "Persona a caja 1: "+aux
        ubicacion=1
        tiempo_caja(Tcaja,ubicacion,caja)
    elif(cola_vacia(cola)==False and caja[2]==0):
        aux=cola.popleft()
        caja[2]=1
        print "Persona a caja 1: "+aux
        ubicacion=2
        tiempo_caja(Tcaja,ubicacion,caja)
    elif(cola_vacia(cola)==False and caja[3]==0):
        aux=cola.popleft()
        caja[3]=1
        print "Persona a caja 1: "+aux
        ubicacion=3
        tiempo_caja(Tcaja,ubicacion,caja)

def cola_vacia(cola):
    if not cola:
        return True
    else:
        return False

    
Tpersona=int(raw_input("Ingrese tiempo (segundos) en el cual una persona llegara al banco: ")) 
#Npersona=int(raw_input("Ingrese el numero de personas: "))
#Tcaja=int(raw_input("Ingrese tiempo (segundos) en el que una caja tarda en atender a alguien: "))


thread.start_new_thread(tiempo_persona, (Tpersona,Npersona,))
print "Esperando banco\n"
time.sleep(5)
#k=0

#while k!=5:
 #   k=+1
    #Tcaja=random.randint(5,35)
    #print str(caja)
thread.start_new_thread(persona_a_caja,(cola, caja,))
    
    






























    

