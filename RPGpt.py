import os, time, random
os.system('cls')

#Funções--
#dados-
def rollDice(side):
  dice = random.randint(1, side)
  return dice

#hp-
def hpGen():
  hp = (rollDice(6)*rollDice(12))/2 + 10

  if race == "orc":
    hp = hp - 6
  elif race == "elfo":
    hp = hp + 8
  elif race == "humano":
    hp = hp + 2
  elif race == "meio-elfo":
    hp = hp + 3

  elif Class == "guerreiro":
    hp = hp + 4
  elif Class == "barbaro":
    hp = hp + 8
  elif Class == "bardo":
    hp = hp + 3
  elif Class == "ladino":
    hp = hp + 3

  print(f"VIDA: {hp:.1f} PONTOS")
  return hp

#força-
def strengthGen():
  str = (rollDice(6)*rollDice(12))/2 + 12

  if race == "orc":
    str = str + 8
  elif race == "elfo":
    str = str - 3
  elif race == "meio-elfo":
    str = str - 1
  elif race == "humano":
    str = str + 2

  elif Class == "bardo":
    str = str - 3
  elif Class == "ladino":
    str = str - 5
  elif Class == "barbaro":
    str = str + 3
  elif Class == "guerreiro":
    str = str - 2

  print(f"FORÇA: {str:.1f} PONTOS")
  return str

#titulo-
def title():
  if race == "humano":
    title1 = "o persistente"
  elif race == "elfo":
    title1 = "o glorioso"
  elif race == "meio-elfo":
    title1 = "a sombra"
  elif race == "orc":
    title1 = "o gigantesco"
  else:
    title1 = race

  if Class == "bardo":
    title2 = "cantor"
  elif Class == "guerreiro":
    title2 = "guerreiro"
  elif Class == "barbaro":
    title2 = "esmaga crânios"
  elif Class == "ladino":
    title2 = "sagaz"
  else:
    title2 = Class

  print(name, title1, title2)
  return name + " " + title1 + " " + title2

#Código--
#criação de personagens-
while True:
  print("\033[35m""Criador de personagens!")
  print("-----""\033[0m")
  print()

  name = input("Nomeie seu herói: ")
  race = input("Raça do herói (humano, elfo, meio-elfo and orc): ")
  Class = input("Classe do herói (bardo, guerreiro, barbaro and ladino): ")

  print()
  C1name = title()
  C1hp = hpGen()
  C1str = strengthGen()
  print()

  time.sleep(2)
  print("\033[31m""Quem você irá batalhar?")
  print("---""\033[0m")
  print()
  time.sleep(3)

  name = input("Nomeie seu herói: ")
  race = input("Raça do herói (humano, elfo, meio-elfo and orc): ")
  Class = input("Classe do herói (bardo, guerreiro, barbaro and ladino): ")

  print()
  C2name = title()
  C2hp = hpGen()
  C2str = strengthGen()
  print()

  time.sleep(5)
  os.system('cls')

#batalha-
  print("\033[35m""⚔️  HORA DA BATALHA! ⚔️")
  print()
  print(f"{C1name} x {C2name}")
  print("QUE COMECE A LUTA! ⚔️""\033[0m")

  round = 1

  while True:
    if C1hp >= 1 and C2hp >= 1:
      print()
      damage = abs(C1str-C2str) + 1
      C1result = rollDice(6)
      C2result = rollDice(6)

      if C1result > C2result:
        print(f"\033[32m{C1name}\033[0m vence a rodada {round}!")
        C2hp -= damage
        time.sleep(5)
        print()
        print(f"{C2name} \033[31mrecebe {damage} de dano!\033[0m")
        time.sleep(5)
        round += 1

      elif C1result == C2result:
        print("\033[0m""Empate!""\033[0m")
        time.sleep(5)
        round += 1

      else:
        print(f"\033[36m{C2name}\033[0m vence a rodada {round}!")
        C1hp -= damage
        time.sleep(5)
        print()
        print(f"{C1name} \033[31mrecebe {damage} de dano!\033[0m")
        time.sleep(5)
        round += 1

#exibindo status-
      print()
      print("---")
      print(f"{C1name} possuí {C1hp} hp!")
      print()
      print(f"{C2name} possuí {C2hp} hp!")
      print()
      time.sleep(3)

#rounds-
      if C1hp >= 1 and C2hp >= 1:
        print(f"\033[35mComeça a rodada {round}!\033[0m")
        time.sleep(3)
        os.system('cls')

      elif C1hp < 1:
        print(f"\033[31m{C1name} morreu!\033[0m")
        time.sleep(3)
        os.system('cls')

      else:
        print(f"\033[31m{C2name} morreu!\033[0m")
        time.sleep(3)
        os.system('cls')

#decisão da batlha-
    else:
      if C1hp < 1:
        print()
        print(f"\033[36m{C2name} VENCE!!\033[0m")
        print("---")
        time.sleep(5)
        print()
        print("Parabéns!")
        print("Obrigado por jogar :)")
        print("---")
        break

      else:
        print(f"\033[32m{C1name} VENCE!!\033[0m")
        print("---")
        time.sleep(5)
        print()
        print("Parabéns!")
        print("Obrigado por jogar :)")
        print("---")
        break

#repetição-
  time.sleep(5)
  print()
  again = input("Gostaria de jogar denovo? ")
  if again != "yes":
    exit()


  else:
    time.sleep(2)
    os.system('cls')
    continue