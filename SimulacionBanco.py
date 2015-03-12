import time
import thread
import random
from collections import deque

cola=deque([])
caja=[0,0,0,0]
ubicacion=0

Npersona=["Pedro","Luis","Juan","Alberto","Abiu","Julian","Jorge"]

def tiempo_persona(Tpersona, Npersona):
    for persona in Npersona:
        time.sleep(Tpersona)
        cola.append(persona)
        print persona+" llego al banco!"

def tiempo_caja(Tcaja, ubicacion):
    global caja
    time.sleep(Tcaja)
    caja[ubicacion]=0
    print "Caja "+str(ubicacion+1)+" vacia!\n"

def persona_a_caja(cola,ubicacion):
    global caja, Tcaja
    aux=''
    if(cola_vacia(cola)==False and caja[0]==0):
        aux=cola.popleft()
        caja[0]=1
        print "Persona a caja 1: "+aux+"\n"
        ubicacion=0
        tiempo_caja(Tcaja, ubicacion)
        
    elif(cola_vacia(cola)==False and caja[1]==0):
        aux=cola.popleft()
        caja[1]=1
        print "Persona a caja 2: "+aux+"\n"
        ubicacion=1
        tiempo_caja(Tcaja, ubicacion)
        
    elif(cola_vacia(cola)==False and caja[2]==0):
        aux=cola.popleft()
        caja[2]=1
        print "Persona a caja 3: "+aux+"\n"
        ubicacion=2
        tiempo_caja(Tcaja, ubicacion)
        
    elif(cola_vacia(cola)==False and caja[3]==0):
        aux=cola.popleft()
        caja[3]=1
        print "Persona a caja 4: "+aux+"\n"
        ubicacion=3
        tiempo_caja(Tcaja, ubicacion)

def cola_vacia(cola):
    if not cola:
        return True
    else:
        return False
    
Tpersona=int(raw_input("Ingrese tiempo (segundos) en el cual una persona llegara al banco: ")) 


thread.start_new_thread(tiempo_persona, (Tpersona,Npersona,))
print "Esperando banco\n"
time.sleep(5)
while True:
    Tcaja=random.randint(5,35)
    thread.start_new_thread(persona_a_caja,(cola,ubicacion))
    time.sleep(2)
    






























    

