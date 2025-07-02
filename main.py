import urllib
import urllib.request
# nu = input("Informe seu nome de usuario no github: ")


teste = urllib.request.urlopen('https://api.github.com/users/kamranahmedse/events')
dados = teste.read()
print(dados)