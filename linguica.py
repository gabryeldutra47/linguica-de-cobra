from tabulate import tabulate
from rich import print
import os

#dicionario de sabores de linguiçeta e o preço por kg
dados_linguiça = {
    'bode com queijo': {
        'preço': 20,
        'estoque': 40
    },
    'rã com bacon': {
        'preço': 22,
        'estoque': 40
    },
    'coelho com sol': {
        'preço': 19,
        'estoque': 40
    },
    'frango com charque': {
        'preço': 24,
        'estoque': 30
    }
}
compras = {}
aperte_enter = '\n Pressione ENTER para continuar...'

#Lista de sabores disponiveis
sabores_disponiveis = list(dados_linguiça)

#laço principal para escolher as operaçoes
while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  mydata = [["1", " Vizualizar sabores de linguiça disponiveis"],
            ["2", "Escolher sabores de linguiça"], ["3", "Finalizar compra"],
            ["4", "Remover itens"], ["5", "Fechar programa"]]

  # create header
  head = ["Opções", "Descrição"]
  print(tabulate(mydata, headers=head, tablefmt="fancy_grid"))

  opcao = int(input('Digite a operação que deseja realizar: '))

  if opcao == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('========================================')
    print('[bold blue]          Sabores disponiveis       [/bold blue]    ')
    print('========================================')
    for sabor in sabores_disponiveis:
      print(
          f"{sabor.capitalize()}: preço por kg R${dados_linguiça[sabor]['preço']} - Estoque: [bold green] {dados_linguiça[sabor]['estoque']}[/bold green] kg"
      )
    input(aperte_enter)

  elif opcao == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Escolha o sabor de linguiça que deseja comprar!! ')
    print('\nSabores disponiveis: \n')
    for sabor in sabores_disponiveis:
      print(
          f"{sabor.capitalize()}: preço por kg R${dados_linguiça[sabor]['preço']} - Estoque: [bold green] {dados_linguiça[sabor]['estoque']} [/bold green] kg"
      )
    input(aperte_enter)

    escolha = input(
        'Digite o sabor que deseja comprar (ou "0" para finaliza): ').lower()

    while escolha != '0':
      if escolha in dados_linguiça:
        quantidade = int(
            input(
                f'Digite quantos kg de {escolha.capitalize()} deseja comprar: '
            ))
        if quantidade > dados_linguiça[escolha]['estoque']:
          print(
              f'Desculpe nos não temos {quantidade}kg de {escolha.capitalize()} em estoque :('
          )
        else:
          if escolha in compras:
            compras[escolha] += quantidade
          else:
            compras[escolha] = quantidade
          dados_linguiça[escolha][
              'estoque'] = dados_linguiça[escolha]['estoque'] - quantidade
        escolha = input(
            'Digite o sabor que deseja comprar (ou "0" para finalizar): '
        ).lower()
      else:
        print('Escolha de sabor invalido!!!')
        break
    input(aperte_enter)

  elif opcao == 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    total_pg = 0
    for sabor, quantidade in compras.items():
      total_pg += quantidade * dados_linguiça[sabor]['preço']
      print(
          f'Você comprou [bold green] {quantidade}[/bold green]kg de linguiça sabor {sabor.capitalize()} '
      )
    print(f'O valor a ser pago é de R${total_pg:.2f}.')
    input(aperte_enter)

  elif opcao == 4:
      os.system('cls' if os.name == 'nt' else 'clear')
      print('Itens na lista de compras:')
      for sabor, quantidade in compras.items():
          print(f"{quantidade}kg de {sabor.capitalize()}")

      sabor_remover = input('Digite o sabor que deseja remover (ou "0" para finalizar): ').lower()

      while sabor_remover != '0':
          if sabor_remover in compras:
              quantidade_remover = int(input(f'Digite quantos kg de {sabor_remover.capitalize()} deseja remover: '))
              if quantidade_remover <= compras[sabor_remover]:
                  compras[sabor_remover] -= quantidade_remover
                  dados_linguiça[sabor_remover]['estoque'] += quantidade_remover
                  print(f'{quantidade_remover}kg de {sabor_remover.capitalize()} removidos da lista de compras.')
              else:
                  print(f'Você não comprou {quantidade_remover}kg de {sabor_remover.capitalize()} ainda.')
          else:
              print('Escolha de sabor para remover inválida!!!')

          sabor_remover = input('Digite o sabor que deseja remover (ou "0" para finalizar): ').lower()

      input(aperte_enter)

  elif opcao == 5:
      os.system('cls' if os.name == 'nt' else 'clear')
      print('Programa encerrado, aproveite sua linguiça!! ( ͡° ͜ʖ ͡°)')
      input(aperte_enter)
