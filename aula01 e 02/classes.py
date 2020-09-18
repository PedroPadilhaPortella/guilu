class Filmes:

    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

    __assistido = 'Pendente'
    favorito = False

    def assistir(self): # Setter setAssistido()
        print("Assistindo {}".format(self.titulo))
        self.__assistido = 'Assistido'

    def favoritar(self): #Setter setFavoritos()
        self.favorito = True

    def mostrar(self): #Getter
        return [
            self.titulo,
            self.autor,
            self.ano,
            self.genero,
            self.__assistido,
            self.favorito
        ]
    def jsonificar(self):
        return{
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "genero": self.genero,
            "assistido": self.__assistido,
            "favorito": self.favorito
        }

    @property #Decorator
    def status(self): #Getter
        return self.__assistido

    @staticmethod # metodo estatico, não está preso a classe
    def cadastrar(titulo, autor, ano, genero):
        genero = genero.capitalize()
        return Filmes(titulo, autor, ano, genero)