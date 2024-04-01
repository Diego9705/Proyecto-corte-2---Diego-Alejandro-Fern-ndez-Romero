import time
import random

def pokemones_pokedex():
    return [Pikachu(),Caterpie(),Pidgeotto(),Bulbasaur(),Charmander(),Squirtle(),Krabby(),Raticate(),Muk(),Kingler()]


def interface_batalla(jugador,pokemon1,pokemon2):
    print("▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲")
    print(f"------------------------->   Turno del jugador {jugador}   <-------------------------")
    print("▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲\n")
    print(f"Pokemon rival: {pokemon2.name}")   
    print(f"Vida: {pokemon2.vida} ❤️\n")

    print(f"Tu Pokemon: {pokemon1.name}")   
    print(f"Vida: {pokemon1.vida} ❤️\n")

    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f"                             🌌 \033[1mHABILIDADES\033[0m🌌")                               
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    pokemon1.display_ataques()


def ganador(contador,njugador,n_pokemones_por_equipo): 
    if contador == n_pokemones_por_equipo:
        print(f"\n ✨🎉\033[1m¡El jugador {njugador} ha ganado!\033[0m 🎉✨")
        exit()

def evento_sin_vida(poke_derrotado,poke_pelea,contador,jugador,njugador,n_pokemones_por_equipo):

    print(f"{poke_derrotado.name} ha caido")

    poke_pelea.dejar_pelea(poke_derrotado)
    poke_derrotado.dejar_pelea(poke_pelea)
    
    ganador(contador,njugador,n_pokemones_por_equipo)

    poke_derrotado = jugador.pokemones[contador]

    print(f"Vamos {poke_derrotado.name}, tu puedes")

    poke_derrotado.peleando_con(poke_pelea)
    poke_pelea.peleando_con(poke_derrotado)

    return poke_derrotado

def eligir_habilidad_PC(pokemon):
    n=0
    for x in range(4):
        if pokemon.ataques[x].pp == 0:
            n+=1
    numeros=[1,2,3,4]

    if n == 4:
        eleccion=-1
        return eleccion
    
    while(True):
        eleccion =random.choice(numeros)
    
        if pokemon.ataques[eleccion-1].pp==0:
            numeros.remove(eleccion)
        else:
            return eleccion
            



def eligir_habilidad(pokemon):
    while(True):
        ej1 = input("¿Qué habilidad decides mandar? (escribe el numero de la habilidad) \n")
        
        
        if ej1 not in ["1","2","3","4"]:
            print("Numero equivocado, intentalo de nuevo\n")
            continue
        n=0
        for x in range(4):
            if pokemon.ataques[x].pp == 0:
                n+=1
        if n==4:
            print("El pokemon esta exhausto y no puede realizar ninguna otra habilidad, usa Forcejeo.\n")
            time.sleep(1)
            ej1=-1
            return ej1
            
        elif pokemon.ataques[int(ej1)-1].pp==0:
            print("Ha usado una habilidad donde el pokemon no tiene más energia, escoga otro\n")

        else:
            return int(ej1)
        
            
        


def seleccionar_pokemones(jugador,n_pokemones):
    for i in range(n_pokemones):
        pokemones_disponibles = pokemones_pokedex()
        while(True):
            e = input(f"¿Qué pokemones quieres para tu equipo jugador {jugador.name}? (escribe el nombre del pokemon, restantes: {3-i})\n").lower()
            if e in nombre_pokemones:
                posicion=nombre_pokemones.index(e)
                jugador.añadir_pokemon(pokemones_disponibles[posicion])
                break
            else:
                print("\nNo se encuentra el nombre de ese Pokemon, intente de nuevo \n")


def seleccionar_aleatorio(jugador,n_pokemones):
    
    for i in range(n_pokemones):
        pokemones_disponibles = pokemones_pokedex()
        posicion = random.randint(0, len(pokemones_disponibles)-1)
        jugador.añadir_pokemon(pokemones_disponibles[posicion])

    print("Estos fueron tus pokemones seleccionados aleatoriamente\n")
    jugador.mostrar_pokemones()

def pokedex(pokemones):
    print("\033[1m---------------------------Bienvenido a la Pokedex---------------------------\033[0m")
    time.sleep(1.25)
    for poke in pokemones:
        poke.presentarse()
    print("▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲\n")



#Diseño de patron strategy en Ataques, usando una interface IAtaques para encapsular los distintos ataques que pueda llegar a tener un pokemon

class IAtaques: 
    def __init__(self,daño,pp,precision,name,prioridad):
        self.daño = daño
        self.pp = pp
        self.precision = precision
        self.name = name
        self.prioridad=prioridad

    def atacar(self):

        n=round(random.random(),2)
        self.pp-=1
        if n*100 <= self.precision:
            return [self.daño] #Puede que en el futuro se quieran implementar mas estadisticas ademas del ataque en una habilidad, como los estados alterados
        else:
            return [-1]

    def display_habilidad(self,n):
        print(f"{n}. \033[1m{self.name}\033[0m\n\nDaño: {self.daño} ⚔️\nPP: {self.pp} ⚡\nPrecision: {self.precision} 🎯")

    def display_descripccion(self):
        pass

class Impactrueno(IAtaques):
    def __init__(self):
        super().__init__(8,3,80,"Impactrueno",0)

    def display_descripccion(self):
        print("Lanza una potente descarga eléctrica que inflige un daño considerable al rival")
    
class Rayo(IAtaques):
    def __init__(self):
        super().__init__(5,3,100,"Rayo",0)
        
    def display_descripccion(self):
        print("Lanza una descarga electrica leve, pero precisa")

class Ataque_Rapido(IAtaques):
    def __init__(self):
        super().__init__(3,5,100,"Ataque Rapido",5)

    def display_descripccion(self):
        print("Lanza un ataque rapido que tiene prioridad 5 en el combate,\n atacas de primeras en la mayoría de los casos")

class Placaje(IAtaques):
    def __init__(self):
        super().__init__(4,7,100,"Placaje",0)
    
    def display_descripccion(self):
        print("Un ataque común y corriente con mucha energía, pero leve")


class Tacleada(IAtaques):
    def __init__(self):
        super().__init__(7,1,80,"Tacleada",1)

    def display_descripccion(self):
        print("Ataque potente que tiene 1 de prioridad, pero solo un uso,\n excelente para rematar al rival")


class Supersonico(IAtaques):
    def __init__(self):
        super().__init__(10,2,70,"Supersonico",0)

    def display_descripccion(self):
        print("Ataque muy potente pero poca energía, puede fallar")  

class Drenadoras(IAtaques):
    def __init__(self):
        super().__init__(6,4,90,"Drenadoras",0)
       
    def display_descripccion(self):
        print("Lanza raíces que crecen rápidamente e infligen un daño considerable")

class Picotazo(IAtaques):
    def __init__(self):
        super().__init__(5,3,90,"Picotazo",1)
       
    def display_descripccion(self):
        print("Ataque rápido y afilado, tiene una prioridad de 1")
       

class Remolino(IAtaques):
    def __init__(self):
        super().__init__(7,3,80,"Remolino",0)
       
    def display_descripccion(self):
        print("Remolino fuerte pero fácil de controlar")

class Tornado(IAtaques):
    def __init__(self):
        super().__init__(9,3,70,"Tornado",0)
       
    def display_descripccion(self):
        print("Tornado fuerte pero difícil de controlar")

class LatigoCepa(IAtaques):
    def __init__(self):
        super().__init__(6,4,100,"Látigo Cepa",0)
       
    def display_descripccion(self):
        print("Remolino fuerte pero difícil de controlar")

class Somnifero(IAtaques):
    def __init__(self):
        super().__init__(12,2,80,"Somnifero",0)
       
    def display_descripccion(self):
        print("Duerme al enemigo para asestar un golpe crítico")

class Lanzallamas(IAtaques):
    def __init__(self):
        super().__init__(7,4,90,"Lanzallamas",0)
       
    def display_descripccion(self):
        print("Lanza una intensa llamarada")

class Grunido(IAtaques):
    def __init__(self):
        super().__init__(4,4,100,"Gruñido",1)
       
    def display_descripccion(self):
        print("Gruñe, distrae e entorpece al rival, ataca con una prioridad de 1")

class Araniazo(IAtaques):
    def __init__(self):
        super().__init__(6,3,100,"Arañazo",0)
       
    def display_descripccion(self):
        print("Ataca con sus afiladas garras")

class Ascuas(IAtaques):
    def __init__(self):
        super().__init__(5,4,100,"Ascuas",0)
       
    def display_descripccion(self):
        print("Lanza una pequeña llama")

class PistolaAgua(IAtaques):
    def __init__(self):
        super().__init__(5,4,100,"Pistola Agua",0)
       
    def display_descripccion(self):
        print("Lanza un pequeño chorro, pero perforante")

class Burbuja(IAtaques):
    def __init__(self):
        super().__init__(7,3,90,"Burbuja",0)
       
    def display_descripccion(self):
        print("Asfixia al rival encerrandolo en una burbuja")

class RayoBurbuja(IAtaques):
    def __init__(self):
        super().__init__(8,3,80,"Rayo Brubuja",0)
       
    def display_descripccion(self):
        print("Lanza burbujas diminutas a una alta velocidad, pequeñas pero letales")

class TajoCruzado(IAtaques):
    def __init__(self):
        super().__init__(17,1,90,"Tajo Cruzado",0)
       
    def display_descripccion(self):
        print("Ataque fatal, solo una oportunidad para lanzarla")

class Hipercolmillo(IAtaques):
    def __init__(self):
        super().__init__(9,2,70,"Hipercolmillo",0)
       
    def display_descripccion(self):
        print("Ataca con su fuerte mandíbula")

class GolpeCabeza(IAtaques):
    def __init__(self):
        super().__init__(8,3,80,"Golpe Cabeza",0)
       
    def display_descripccion(self):
        print("Enviste al rival con su cabeza")

class Lodo(IAtaques):
    def __init__(self):
        super().__init__(6,3,90,"Lodo",2)
       
    def display_descripccion(self):
        print("Manda lodo que relentiza al pokemon enemigo,\n atacas con una prioridad de 2")

class BombaLodo(IAtaques):
    def __init__(self):
        super().__init__(8,2,80,"BombaLodo",3)
       
    def display_descripccion(self):
        print("Manda una bomba de lodo que atrapa al pokemon enemigo,\n atacas con una prioridad de 3")

class AtaqueAcido(IAtaques):
    def __init__(self):
        super().__init__(9,3,75,"Ataque Acido",0)
       
    def display_descripccion(self):
        print("Lanza un potente ácido")

class Infortunio(IAtaques):
    def __init__(self):
        super().__init__(10,1,90,"Ataque Acido",1)
       
    def display_descripccion(self):
        print("Maldices al enemigo y lo encadenas, atacas con un potente ataque al enemgio\ncon una prioridad de 1")

class Hidropulso(IAtaques):
    def __init__(self):
        super().__init__(8,3,80,"Hidropulso",0)
       
    def display_descripccion(self):
        print("Lanza una gran chorro y perforante")

#------        


#Clase Jugador, permite que cada jugar guarde sus pokemones en la lista pokemones.

class Jugador:
    def __init__(self,name):
        self.name=name
        self.pokemones = []

    def añadir_pokemon(self, poke):
        self.pokemones.append(poke)
    
    def mostrar_pokemones(self):
        for i in range(len(self.pokemones)):
            self.pokemones[i].presentarse()


#Esta clase es un observador y un notificador al mismo tiempo, implementa el diseño de patron Observer, teniendo la funcion de que los pokemones en ataque puedan notificarse entre ellos para bajarse la vida con sus ataques
class Pokemon:

    def __init__(self,name,vida,ataques,velocidad):
        self.name = name
        self.vida = vida
        self.ataques = ataques
        self.velocidad=velocidad
        self._en_combate=[]
       
        
    
    def peleando_con(self, poke):
        if poke not in self._en_combate:
            self._en_combate.append(poke)

    def dejar_pelea(self, poke):
        if poke in self._en_combate:
            self._en_combate.remove(poke)

    def actualizacion_estadisticas(self, ataque):

        if ataque[0] == -1:
            print("\nHa fallado el ataque")
        else:
            self.vida-=ataque[0]
            print(f"{self.name} fue atacado")
            print(f"Vida: {self.vida}\n")

    def realizar_ataque(self,n):
        for subscriber in self._en_combate:
            if n==-2: #Forcejeo
                dañoForcejeo = 5
                print(f"Tras no tener mas energia, ha usa Forcejeo, inflije {dañoForcejeo} PS pero el usuario pierde {dañoForcejeo} PS\n")
                self.vida-=dañoForcejeo
                subscriber.vida-=dañoForcejeo
            else:
                print(f"{self.name} ha usado {self.ataques[n].name}\n")
                subscriber.actualizacion_estadisticas(self.ataques[n].atacar())
            
    def display_ataques(self):
        i=1
        for ataque in self.ataques:
            ataque.display_habilidad(i)
            print("")
            ataque.display_descripccion()
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            i+=1

    def presentarse(self):
        print("▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲")
        print(f"                             👾 \033[1m{self.name}\033[0m👾")
        print("▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲")
        print(f"Vida: \033[1m{self.vida}\033[0m ❤️")
        print(f"Velocidad: \033[1m{self.velocidad}\033[0m 💨 👟")

        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print(f"                             🌌 \033[1mHABILIDADES\033[0m🌌")    
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        self.display_ataques()
        
    
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu",60,[Impactrueno(),Rayo(),Ataque_Rapido(),Placaje()],70)


class Caterpie(Pokemon):
    def __init__(self):
        super().__init__("Caterpie",75,[Placaje(),Tacleada(),Supersonico(),Drenadoras()],40)

class Pidgeotto(Pokemon):
    def __init__(self):
        super().__init__("Pidgeotto", 55, [Picotazo(),Remolino(),Tornado(),Ataque_Rapido()],80)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 65, [LatigoCepa(),Drenadoras(),Placaje(),Somnifero()],50) 

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 65, [Lanzallamas(),Grunido(),Araniazo(),Ascuas()],70)

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 70, [PistolaAgua(),Burbuja(),Ataque_Rapido(),Placaje()],45)

class Krabby(Pokemon):
    def __init__(self):
        super().__init__("Krabby", 80, [Burbuja(),RayoBurbuja(),Placaje(),TajoCruzado()],30)

class Raticate(Pokemon):
    def __init__(self):
        super().__init__("Raticate", 50, [Hipercolmillo(),Ataque_Rapido(),Placaje(),GolpeCabeza()],90)

class Muk(Pokemon):
    def __init__(self):
        super().__init__("Muk",100,[Lodo(),BombaLodo(),AtaqueAcido(),Infortunio()],10)

class Kingler(Pokemon):
    def __init__(self):
        super().__init__("Kingler",90,[Hidropulso(),RayoBurbuja(),Rayo(),Placaje()],20)

#Completar Pokemones



if __name__ == '__main__':
    delay = 0.5
    n_pokemones_por_equipo=3

    jg1=Jugador(1)
    
    pokemones_disponibles = pokemones_pokedex() #pokemones disponibles
    nombre_pokemones = []
    for x in pokemones_disponibles:
        nombre_pokemones.append(x.name.lower())
    
    while (True):
        e=input("\nBienvenido a Pokemon\n\n¿Qué modo quieres jugar?\n\n1. Dos jugadores\n2. Contra la PC\n")
        if e == "1" or e == "2":
            break
        print("Numero equivocado, intente de nuevo\n")

    if e == "1":
        
        jg2=Jugador(2)
        for i in range(2):
           
            if i == 0:
                selector=jg1
            else:
                selector=jg2
            
                
            while(True):
                e=input(f"Elegir los pokemones jugador {i+1}:\n 1. Aleatorios \n 2. Manualmente\n")
                
                #Eleccion aleatoria
                if e == "1":
                    seleccionar_aleatorio(selector,n_pokemones_por_equipo)
                    break
                    
                #Eleccion manual
                elif e == "2":
                    pokedex(pokemones_disponibles)
                    seleccionar_pokemones(selector,n_pokemones_por_equipo)
                    break

                else:
                    print("Numero equivocado, intente de nuevo\n")
             
        
        contador1=0
        contador2=0

        poke1=jg1.pokemones[contador1]
        poke2=jg2.pokemones[contador2]
        poke1.peleando_con(poke2)   
        poke2.peleando_con(poke1)

        while(True):
        
            interface_batalla(1,poke1,poke2)


            ej1=eligir_habilidad(poke1)-1

            #Para que el rival no vea la habilidad que mando el jugador    
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    
            interface_batalla(2,poke2,poke1)

            ej2=eligir_habilidad(poke2)-1


            print(f"\nPrioridad ataque pokemon 1: {poke1.ataques[ej1].prioridad}")
            print(f"Prioridad ataque pokemon 2: {poke2.ataques[ej2].prioridad}\n")

            if poke1.ataques[ej1].prioridad!=0 or poke2.ataques[ej2].prioridad!=0:
                if poke1.ataques[ej1].prioridad > poke2.ataques[ej2].prioridad:
                    poke_rapido = [poke1,ej1,jg1.name]
                    poke_lento = [poke2,ej2,jg2.name]
                elif poke2.ataques[ej2].prioridad > poke1.ataques[ej1].prioridad:
                    poke_rapido = [poke2,ej2,jg2.name]
                    poke_lento =[poke1,ej1,jg1.name]
                else:
                    n= random.randint(0, 1)
                    if n==0:
                        poke_rapido = [poke1,ej1,jg1.name]
                        poke_lento = [poke2,ej2,jg2.name]
                    else:
                        poke_rapido = [poke2,ej2,jg2.name]
                        poke_lento =[poke1,ej1,jg1.name]


            elif poke1.velocidad > poke2.velocidad:
                poke_rapido = [poke1,ej1,jg1.name]
                poke_lento = [poke2,ej2,jg2.name]

            elif poke2.velocidad > poke1.velocidad:
                poke_rapido = [poke2,ej2,jg2.name]
                poke_lento =[poke1,ej1,jg1.name]
            else:
                n= random.randint(0, 1)
                if n==0:
                    poke_rapido = [poke1,ej1,jg1.name]
                    poke_lento = [poke2,ej2,jg2.name]
                else:
                    poke_rapido = [poke2,ej2,jg2.name]
                    poke_lento =[poke1,ej1,jg1.name]
            
            print(f"\nPokemon jugador {poke_rapido[2]}:\n{poke_rapido[0].name} es más Rapido, ataca de primeras")
            time.sleep(delay)
            poke_rapido[0].realizar_ataque(poke_rapido[1])
            time.sleep(delay)
            
            if poke1.vida <= 0:
                contador1+=1
                poke1 = evento_sin_vida(poke1,poke2,contador1,jg1,jg2.name,n_pokemones_por_equipo)
                time.sleep(delay)
            if poke2.vida <= 0:
                contador2+=1
                poke2 = evento_sin_vida(poke2,poke1,contador2,jg2,jg1.name,n_pokemones_por_equipo)
                time.sleep(delay)

            if poke_lento[0].vida>0 and  poke_rapido[0].vida > 0:
                print(f"\nPokemon jugador {poke_lento[2]}:\n{poke_lento[0].name} es más Lento, ataca de ultimas")
                time.sleep(delay)
                poke_lento[0].realizar_ataque(poke_lento[1])
                time.sleep(delay)

                if poke1.vida <= 0:
                    contador1+=1
                    poke1 = evento_sin_vida(poke1,poke2,contador1,jg1,jg2.name,n_pokemones_por_equipo)
                    time.sleep(delay)
                if poke2.vida <= 0:
                    contador2+=1
                    poke2 = evento_sin_vida(poke2,poke1,contador2,jg2,jg1.name,n_pokemones_por_equipo)
                    time.sleep(delay)

            print(input("\nEnter para continuar\n"))

    else:

        jg2=Jugador("🤖")

        while(True):
            e=input(f"Elegir los pokemones jugador 1:\n 1. aleatorios \n 2. manualmente\n")
            
            #Eleccion aleatoria
            if e == "1":
                seleccionar_aleatorio(jg1,n_pokemones_por_equipo)
                break
                
            #Eleccion manual
            elif e == "2":
                pokedex(pokemones_disponibles)
                seleccionar_pokemones(jg1,n_pokemones_por_equipo)
                break

            else:
                print("Numero equivocado, intente de nuevo\n")
              
        seleccionar_aleatorio(jg2,n_pokemones_por_equipo)
        contador1=0
        contador2=0

        poke1=jg1.pokemones[contador1]
        poke2=jg2.pokemones[contador2]
        poke1.peleando_con(poke2)   
        poke2.peleando_con(poke1)

        while(True):
    
            interface_batalla(1,poke1,poke2)
            ej1=eligir_habilidad(poke1)-1
            ej2=eligir_habilidad_PC(poke2)-1

            print(f"\nPrioridad ataque pokemon 1: {poke1.ataques[ej1].prioridad}")
            print(f"Prioridad ataque pokemon 2: {poke2.ataques[ej2].prioridad}\n")

            if poke1.ataques[ej1].prioridad!=0 or poke2.ataques[ej2].prioridad!=0:
                if poke1.ataques[ej1].prioridad > poke2.ataques[ej2].prioridad:
                    poke_rapido = [poke1,ej1,jg1.name]
                    poke_lento = [poke2,ej2,jg2.name]
                elif poke2.ataques[ej2].prioridad > poke1.ataques[ej1].prioridad:
                    poke_rapido = [poke2,ej2,jg2.name]
                    poke_lento =[poke1,ej1,jg1.name]
                else:
                    n= random.randint(0, 1)
                    if n==0:
                        poke_rapido = [poke1,ej1,jg1.name]
                        poke_lento = [poke2,ej2,jg2.name]
                    else:
                        poke_rapido = [poke2,ej2,jg2.name]
                        poke_lento =[poke1,ej1,jg1.name]

            elif poke1.velocidad > poke2.velocidad:
                poke_rapido = [poke1,ej1,jg1.name]
                poke_lento = [poke2,ej2,jg2.name]

            elif poke2.velocidad > poke1.velocidad:
                poke_rapido = [poke2,ej2,jg2.name]
                poke_lento =[poke1,ej1,jg1.name]
            else:
                n= random.randint(0, 1)
                if n==0:
                    poke_rapido = [poke1,ej1,jg1.name]
                    poke_lento = [poke2,ej2,jg2.name]
                else:
                    poke_rapido = [poke2,ej2,jg2.name]
                    poke_lento =[poke1,ej1,jg1.name]
            
            print(f"\nPokemon jugador {poke_rapido[2]}:\n{poke_rapido[0].name} es más Rapido, ataca de primeras")
            time.sleep(delay)
            poke_rapido[0].realizar_ataque(poke_rapido[1])
            time.sleep(delay)
            
            if poke1.vida <= 0:
                contador1+=1
                poke1 = evento_sin_vida(poke1,poke2,contador1,jg1,jg2.name,n_pokemones_por_equipo)
                time.sleep(delay)
            if poke2.vida <= 0:
                contador2+=1
                poke2 = evento_sin_vida(poke2,poke1,contador2,jg2,jg1.name,n_pokemones_por_equipo)
                time.sleep(delay)

            if poke_lento[0].vida>0 and  poke_rapido[0].vida > 0:
                print(f"\nPokemon jugador {poke_lento[2]}:\n{poke_lento[0].name} tras ser más Lento, ataca de ultimas")
                time.sleep(delay)
                poke_lento[0].realizar_ataque(poke_lento[1])
                time.sleep(delay)

                if poke1.vida <= 0:
                    contador1+=1
                    poke1 = evento_sin_vida(poke1,poke2,contador1,jg1,jg2.name,n_pokemones_por_equipo)
                    time.sleep(delay)
                if poke2.vida <= 0:
                    contador2+=1
                    poke2 = evento_sin_vida(poke2,poke1,contador2,jg2,jg1.name,n_pokemones_por_equipo)
                    time.sleep(delay)

            print(input("\nEnter para continuar\n"))
