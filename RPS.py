from getpass import getpass as input
import os
os.system("cls")

print("E P I C 🗿 ✂️   📃 B A T T L E")
counter = 0
p1wins = 0
p2wins = 0
while True:
  print()
  print("Selecione seu movimento: ")
  print("\033[33m""Pedra = P""\033[0m")
  print("\033[36m""Papel = F""\033[0m")
  print("\033[32m""Tesoura = T""\033[0m")
  print("\033[31m""Atenção! Os movimentos devem ser colocados em MAÍUSCULO.""\033[0m")
  print("---")

  print()
  p1 = input("Player 1 > ")
  p2 = input("Player 2 > ")
  print()

  if p1 == "P" and p2 == "F":
    print("A Pedra do Player1 é completamente encoberta pelo Papel do Player2!")
    print("\033[34m""Player 2 é o vencedor!!!""\033[0m")
    p2wins += 1

  elif p2 == "P" and p1 == "F":
    print("A Pedra do Player2 é completamente encoberta pelo Papel do Player1!")
    print("\033[31m""Player 1 é o vencedor!!!""\033[0m")
    p1wins += 1

  elif p2 == "P" and p1 == "P":
    print("As Pedras dos Players 1 e 2 se ESMAGAM violentamente!")
    print("\033[35m""É um empate!""\033[0m")

  elif p1 == "F" and p2 == "T":
    print("O Papel do Player1 é transformado em átomos pela Tesoura do Player2!")
    print("\033[34m""Player 2 é o vencedor!!!""\033[0m")
    p2wins += 1

  elif p2 == "F" and p1 == "T":
    print("O Papel do Player2 é transformado em átomos pela Tesoura do Player1!")
    print("\033[31m""Player 1 é o vencedor!!!""\033[0m")
    p1wins += 1

  elif p1 == "F" and p2 == "F":
    print("Os Papéis dos Players 1 e 2 se chocam e formam uma bola inútil de Papel!")
    print("\033[35m""Niguém ganha!""\033[0m")
    
  elif p1 == "T" and p2 == "P":
    print("A Tesoura do Player1 é OBLITERATADA pela Pedra do Player2!")
    print("\033[34m""Player 2 é o vencedor!!!""\033[0m")
    p2wins += 1

  elif p1 == "P" and p2 == "T":
    print("A Tesoura do Player2 é OBLITERATADA pela Pedra do Player1!")
    print("\033[31m""Player 1 é o vencedor!!!""\033[0m")
    p1wins += 1

  elif p1 == "T" and p2 == "T":
    print("As Tesouras dos Players 1 e 2 cortam uma a outra!")
    print("\033[35m""Todo mundo perde!""\033[0m")

  else:
    print("\033[31m""Desculpa! Um de vocês digitou algo errado...""\033[0m")

  print()
  continuar = input("Se deseja PARAR de jogar digite P, caso contrario aparte enter: ")
  counter += 1
  if continuar == "P":
      break
  
print("\033[36m")
print(f"Vocês jogaram {counter} partidas!")
print("\033[0m")
print("O número de vitórias do Player 1 foi...", p1wins)
print("O número de vitórias do Player 2 foi...", p2wins)
print("\033[32m""O grande vencedor é........""\033[0m")

if p1wins > p2wins:
  ganhador = "PLAYER 1!!!!!"
elif p1wins < p2wins:
  ganhador = "PLAYER 2!!!!!"
elif p1wins == p2wins:
  ganhador = "EMPATADO."

print("\033[32m",ganhador, "PARABÉNS!!!""\033[0m")
print()
print("Obrigado por jogarem!!")
