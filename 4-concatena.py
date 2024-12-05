name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
gamePrice = float(input("Digite o preço do jogo:\n"))
planIncluded = input("Está incluso no serviço mensal?\n")


print("###Dados do Jogo###")
print("===================")
'''
print("Ano do Jogo:", yearLaunch)
print("Preço do Jogo:", gamePrice)
print("Está incluído no plano?", planIncluded)'''

'''
print("Nome do Jogo:", name, "\n Ano de lançamento:", yearLaunch,
      "\n Preço do Jogo:", gamePrice, "\n Está incluso no plano?", planIncluded)'''
      
      # alternativa 3
print(f"Nome do Jogo: {name} \nAno de lançamento{yearLaunch} \nPreço do Jogo: {gamePrice} \nEstá inclusi no serviço? {planIncluded}")