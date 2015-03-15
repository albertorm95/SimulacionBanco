Simulacion de Banco
-----------------------------------------
Descripción: 

El programa se encarga de simular un banco con cuatro cajas y una cola, entran las personas a las colas y luego entran a hacer atendidas.
-----------------------------------------
Como funciona: 

Se inica un timer aleatorio para que las pensonas empiezen a formarce en la cola, luego de un pequeño timer el banco empieza a atender a la gente, cada caja tiene un tiempo alatorio de atencion a cliente, cuando ese tiempo pasa la caja se desocupa y esa persona se va del banco, luego de un pequeño tiempo otra persona entra a ser atendida en una caja. Se utilizaron hilos para poder correr el timer de las personas que llegaban al banco an paralelo al tiempo en el cual una caja atendia una persona, al igual se utilizo la estructura de datos colas y arreglos para representar las personas y las cajas respectivamente.

Se utilizo librerias internas de python: time, thread, random y collections/deque.
Se utilizo librerias externas a python: colorconsole/terminal, __future__/print_fuction 
-----------------------------------------
Entorno:

Python.
Git.
-----------------------------------------
Desarrollado por:

Alberto Manuel Rojas Mendez
-----------------------------------------
Propósito:

Estructura de Datos
Experiencia de Aprendizaje 2
Mazro 2015 - Marzo 2015
Universidad Autónoma de Guadalajara, Campus Tabasco
-----------------------------------------
Ubicación: https://github.com/albertorm95/SimulacionBanco
