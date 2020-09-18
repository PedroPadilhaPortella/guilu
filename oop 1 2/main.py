import classes, requests

batman = classes.Filmes.cadastrar('Batman, O cavaleiro das trevas', 'Christopen Nolan', 2008, 'ação, policial')

batman.assistir()

batman.favoritar()

# batman.__assistido = 'Em Curso' => atributo privado
# batman.genero = 'ação, policial, violência' # atributo publico

print(batman.mostrar())

print(batman.jsonificar())

print(batman.status)

print(requests.get('https://www.google.com.br/'))