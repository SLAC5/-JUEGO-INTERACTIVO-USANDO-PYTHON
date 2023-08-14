
import random
import numpy as np
    


class MyGame ():
    def __init__ (self, player1, player2,height,width):
        self.player1 = player1.upper()
        self.player2 = player2.upper()  
        self.code1 = player1[0].upper()
        self.code2 = player2[0].upper()
        self.P1position = 1
        self.P2position = 1
        self.height = height
        self.width = width
        self.D = Dice ()

    def Tablero (self):
        width = self.width
        height = self.height
        self.position = np.array([[0 for i in range(width)] for j in range(height)])
        p = height * width
        if not height %2:
            for i in range (height):
                if  i %2:
                    for k in range(width,0,-1):

                        self.position [i][k-1] = p
                        p-=1
                
                else:
                    for k in range(width):
                        self.position [i][k] = p
                        p -= 1

        else:
            for i in range (height):
                if  not i %2:
                    for k in range(width,0,-1):

                        self.position [i][k-1] = p
                        p-=1
                
                else:
                    for k in range(width):
                        self.position [i][k] = p
                        p -= 1


        self.board = np.array([[["-" for i in range(width)] for j in range(height)]for k in range(3)])

    
        
        for i in range (3):
            check = False
            while check == False:
                y = random.randint(1,height -1)
                x = random.randint(0,width -1)

                if self.board [0][y][x] != "-":
                    check = False

                elif y != height -1:
                    if  self.board [0][y-1][x] != "-" or self.board [0][y+1][x] != "-":
                        check = False
                    
                    else:
                        self.board[0][y][x] = "|"
                        check = True

                elif y == height -1:
                    if  self.board [0][y-1][x] != "-":
                        check = False
                    
                    else:
                        self.board[0][y][x] = "|"
                        check = True



                    

                else:
                    self.board[0][y][x] = "|"
                    check = True
        
        p = height*width 
        final = np.where(self.position==p)
        for i in range (3):
            check = False
            while check == False:
                y = random.randint(0,height-2)
                x = random.randint(0,width -1)

                if self.board [0][y][x] != "-" or self.board [0][y+1][x] == "|":
                    check = False

                elif x == final [1][0] and y == final [0][0]:
                    check = False
                
                elif y != 0:
                    if  self.board [0][y-1][x] != "-" or self.board [0][y+1][x] != "-":
                        check = False
                    
                    else:
                        self.board[0][y][x] = "/"
                        check = True

                elif y == height -1:
                    if  self.board [0][y+1][x] != "-":
                        check = False
                    
                    else:
                        self.board[0][y][x] = "/"
                        check = True

                
                else:
                    self.board[0][y][x] = "/"
                    check = True

        self.board [1] = self.board [0]
        self.board [2] = self.board [0]
       
        


        

    def Start(self):
        self.board [0][self.height-  1][0] = ":"
        self.board [1][self.height-  1][0] = self.code1
        self.board [2][self.height-  1][0] = self.code2 
        self.xcoor1 = 0
        self.xcoor2 = 0
        self.ycoor1 = self.height-1
        self.ycoor2 = self.height-1
        
        


    def Info(self):
        info = "\n"
        for i in range (self.height):
            info = info + "\n" + "\n"
            for k in range (self.width):
                info = info + self.board [0][i][k] + "\t"

        info = info + "\n"
        return info

    
    
    def Move(self,move,player):
        ax = 0
        ay = 0
        if player == 1:
            

            self.P1position += move
            self.board [0] = self.board [2] 
            x = np.where(self.position == self.P1position)
            ax = x [1][0]
            ay = x [0][0]

            if self.board [0][ay][ax] == "|":

                ay -= 1
                self.board [0][ay][ax] = self.code1
                self.board [1][ay][ax] = self.code1

                self.board [1][self.ycoor1][self.xcoor1] = "-"
                self.P1position = self.position [ay][ax]
                self.ycoor1 = ay
                self.xcoor1 = ax


                return "Escalera!! subes un nivel"
            
            elif self.board [0][ay][ax] == "/":

                ay += 1
                self.board [0][ay][ax] = self.code1
                self.board [1][ay][ax] = self.code1

                self.board [1][self.ycoor1][self.xcoor1] = "-"
                self.P1position = self.position [ay][ax]
                self.ycoor1 = ay
                self.xcoor1 = ax


                return "Serpiente :( bajas un nivel."

            elif self.board [0][ay][ax] == self.code2:

                self.board [0][ay][ax] = ":"
                self.board [1][ay][ax] = self.code1

                self.board [1][self.ycoor1][self.xcoor1] = "-"
                self.P1position = self.position [ay][ax]
                self.ycoor1 = ay
                self.xcoor1 = ax

                return ""


            else:

                self.board [0][ay][ax] = self.code1
                self.board [1][ay][ax] = self.code1

                self.board [1][self.ycoor1][self.xcoor1] = "-"
                self.P1position = self.position [ay][ax]
                self.ycoor1 = ay
                self.xcoor1 = ax

                return ""


            
            

            
            
  
            


        else:
        
            self.P2position += move
            self.board [0] = self.board [1] 
            x = np.where(self.position == self.P2position)
            ax = x [1][0]
            ay = x [0][0]

            if self.board [0][ay][ax] == "|":

                ay -= 1
                self.board [0][ay][ax] = self.code2
                self.board [2][ay][ax] = self.code2

                self.board [2][self.ycoor2][self.xcoor2] = "-"
                self.P2position = self.position [ay][ax]
                self.ycoor2 = ay
                self.xcoor2 = ax

                

                return "Escalera!! subes un nivel"
            
            elif self.board [0][ay][ax] == "/":

                ay += 1

                self.board [0][ay][ax] = self.code2
                self.board [2][ay][ax] = self.code2

                self.board [2][self.ycoor2][self.xcoor2] = "-"
                self.P2position = self.position [ay][ax]
                self.ycoor2 = ay
                self.xcoor2 = ax

                return "Serpiente :( bajas un nivel."

            elif self.board [0][ay][ax] == self.code1:

                self.board [0][ay][ax] = ":"
                self.board [2][ay][ax] = self.code2

                self.board [2][self.ycoor2][self.xcoor2] = "-"
                self.P2position = self.position [ay][ax]
                self.ycoor2 = ay
                self.xcoor2 = ax

                return ""

            else:

                self.board [0][ay][ax] = self.code2
                self.board [2][ay][ax] = self.code2

                self.board [2][self.ycoor2][self.xcoor2] = "-"
                self.P2position = self.position [ay][ax]
                self.ycoor2 = ay
                self.xcoor2 = ax

                return ""



            
            
            

            
            
  
           

    
    def Check (self):
        if self.xcoor1 == self.xcoor2 and self.ycoor1 == self.ycoor2:
            self.board [0] [self.ycoor1] [self.xcoor1] = ":"

    def Menu (self):
        height = self.height
        menu = ""
        
        if not height %2:
            for i in range (height):
                if  not i %2:
                    menu += "| ---> ---> | \n"
                
                else:
                    menu +="| <--- <--- | \n"
        else:
            for i in range (height):
                if   i %2:
                    menu +="| <--- <--- | \n"
                
                else:
                    menu += "| ---> ---> | \n"

        print()
        print("...Especificaciones...")
        print("Los jugadores avanzarán en el tablero en modo serpiente. Empezarán en la esquina izquiera inferior en modo serpiente.")
        print (menu)
        print("El ganador será el que llegue a la última casilla primero.") 
        print("Cada jugador será representado en el tablero como la inicial del nombre que escoja. Al igual las serpientes /, escaleras | , y espacios neutros - . Cuando ambos jugadores estén en el mismo lugar, estará representado como : .")
        print("Listo?")
        print()

            
        
        
            
class Dice:

    def Roll (self):
        return random.randint(1,6)

    def Dado (self,x):
        if x == 1:
            return "\n      *\n"
        
        elif x == 2:
            return "\t* \n\n    *"
        
        elif x == 3:
            return "\t* \n      *\n    *"
        
        elif x == 4:
            return "    *\t* \n\n    *\t*"
        
        elif x == 5:
            return "    *\t* \n      *\n    *\t*"
        
        else:
            return "    *\t* \n    *\t* \n    *\t*"
            


        




    
    


def main():

  play = True
  turno = 1
  
  print("\n \t Serpientes y Escaleras\n")
  p1 = input("Primer Jugador:       ")
  p2 = input("Segundo Jugador:      ")
  h = int(input("Altura del tablero:    "))
  w = int(input("Ancho del tablero:     "))
  NewGame = MyGame(p1,p2, h, w)
  NewGame.Menu()
  NewGame.Tablero()
  NewGame.Start()
  print(NewGame.Info())
  print()
  print("Empieza el juego!")
  print()
  print("Presiona C para continuar con el siguiente turno, T para terminar el juego o M para volver a mostrar las instrucciones.")
  print()

  while play == True:

    instrucciones = input()
    instrucciones = instrucciones [0].upper()
    if turno < 11:
        if instrucciones == "C":

            print()
            print ("# de turno: ", turno)
            print()
            turno += 1
            print ("Turno de ",NewGame.player1)
            print()
            x = NewGame.D.Roll()

            print(NewGame.D.Dado(x))
            if x == 1:
                print("Avanza",x,"casilla")
            else:
                print("Avanza",x,"casillas")

                
            z = True
                
            while z == True:
                y = input()
                y = y[0].upper()
                    
                if y == "C":
                    break

                elif y == "T":
                    print ("Ha elegido acabar el juego")
                    print("GAME OVER")
                    break
                        
                    
                elif y == "M":
                    NewGame.Menu()
                    
                else:
                    print(" Opción invalida, por favor presiona C para continuar con el siguiente turno o T para terminar el juego") 

            if y == "T":
                break

                
            if NewGame.P1position+x >=30:
                print(NewGame.player1," es el ganador!!")
                print("Gracias por jugar :)")
                print("GAME OVER")
                break
                
            else:
                move = NewGame.Move(x,1)
                if NewGame.P1position == 30:
                    print(NewGame.player2," es el ganador!!")
                    print("Gracias por jugar :)")
                    print("GAME OVER")
                    break

                else:

                    print(move)
                    NewGame.Check()
                    print(NewGame.Info())


            
            z = True
            while z == True:
                y = input()
                y = y[0].upper()
                
                if y == "C":
                    break

                elif y == "T":
                    print ("Ha elegido acabar el juego")
                    print("GAME OVER")
                    break
                        
                    
                elif y == "M":
                    NewGame.Menu()
                    
                else:
                    print(" Opción invalida, por favor presiona C para continuar con el siguiente turno o T para terminar el juego") 

            if y == "T":
                break 

            print()
            print ("turno de ",NewGame.player2)
            print()
            x = NewGame.D.Roll()

            print(NewGame.D.Dado(x))
            print()
            if x == 1:
                print("Avanza",x,"casilla")
            else:
                print("Avanza",x,"casillas")

            z = True
                
            while z == True:
                y = input()
                y = y[0].upper()
                    
                if y == "C":
                    break

                elif y == "T":
                    print ("Ha elegido acabar el juego")
                    print("GAME OVER")
                    break
                        
                    
                elif y == "M":
                    NewGame.Menu()
                    
                else:
                    print(" Opción invalida, por favor presiona C para continuar con el siguiente turno o T para terminar el juego") 

            if y == "T":
                break

            



                        
                
            

            if NewGame.P2position+x >=30:
                print(NewGame.player2," es el ganador!!")
                print("Gracias por jugar :)")
                print("GAME OVER")
                break
                
            else:
                move = NewGame.Move(x,2)
                if NewGame.P2position == 30:
                    print(NewGame.player2," es el ganador!!")
                    print("Gracias por jugar :)")
                    print("GAME OVER")
                    break

                else:

                    print(move)
                    NewGame.Check()
                    print(NewGame.Info())
                

            
        elif instrucciones == "T":

            print ("Ha elegido acabar el juego")
            print("GAME OVER")
            break

        elif instrucciones == "M":
            NewGame.Menu()
            
        else:
            print(" Opción invalida, por favor presiona C para continuar con el siguiente turno o T para terminar el juego")

    else:
            
        print("El numero máximo de turnos se ha alcanzado...")
        print("GAME OVER")
        break



            
            


            
                  

            
                
            


        
          


  




   
   

  

  
   
   
  


if __name__== "__main__" :
    main()

         
