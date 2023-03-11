import os
os.system('cls')

print("Conversor de Libras/Reais")
print("=====")
print()

print("Bem vindos ao meu conversor de Libras para Reais e vice-versa!")
print("A operação é bem simples, primeiramente digite que tipo de conversão você deseja fazer:") 
print("1. - Para conversão Libras -> Reais.")
print("2. - Para conversão Reais -> Libras.")
cotLb = float(input("3. - Informe a cotação da libra aqui (Utilizando PONTO para decímais!): ")) 
print()

tipo = int(input("Informe o que você deseja aqui: "))
if tipo == 1:
    while True:
        print()
        print("Você digitou 1.")
        print("Conversão Libras -> Reais")
        print("Atenção! Digite valores utilizando PONTO para decímais!")
        print()
        valorLb = float(input("Digite o valor em Libras que você deseja converter: ")) 
        print()
        conRS = valorLb*cotLb
        print(f"Utilizando a cotação de {cotLb}R$  à Libra, o valor do seu produto é: {conRS:.2f}R$!")
        print()
        continuar = int(input("Digite 1 para realizar outra operação, caso queira trocar de modo digite 2, caso queira para digite 3: "))
        if continuar == 3:
            break
        elif continuar == 2:
          print()
          print("Você digitou 2.")
          print("Conversão Reais -> Libras")
          print("Atenção! Digite valores utilizando PONTO para decímais!")
          print()
          valorRS = float(input("Digite o valor em Reais que você deseja converter: ")) 
          print()
          conLb = valorRS/cotLb
          print(f"Utilizando a cotação de {cotLb}R$ à Libra, o valor do seu produto é: {conLb:.2f}£!")
          print()
          continuar = int(input("Digite 1 caso queira trocar de modo, caso queira parar digite 2: "))
          if continuar != 1:
                break   

elif tipo == 2:
    while True:
        print()
        print("Você digitou 2.")
        print("Conversão Reais -> Libras")
        print("Atenção! Digite valores utilizando PONTO para decímais!")
        print()
        valorRS = float(input("Digite o valor em Reais que você deseja converter: ")) 
        print()
        conLb = valorRS/cotLb
        print(f"Utilizando a cotação de {cotLb}R$ à Libra, o valor do seu produto é: {conLb:.2f}£!")
        print()
        continuar = int(input("Digite 1 para trocar de modo , caso queira realizar outra operação digite 2, caso queira para digite 3: "))
        if continuar == 3:
            break
        elif continuar == 1:
            print()
            print("Você digitou 1.")
            print("Conversão Libras -> Reais")
            print("Atenção! Digite valores utilizando PONTO para decímais!")
            print()
            valorLb = float(input("Digite o valor em Libras que você deseja converter: ")) 
            print()
            conRS = valorLb*cotLb
            print(f"Utilizando a cotação de {cotLb}R$  à Libra, o valor do seu produto é: {conRS:.2f}R$!")
            print()
            continuar = int(input("Digite 1 caso queira parar digite, caso queira trocar de modo digite 2: "))
            if continuar != 2:
                break

else: 
    print("Desculpe número informado invalído!")
