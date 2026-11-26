
# usuarios/repositorio.py

from usuarios.controle_acesso import ControleAcesso
from usuarios.usuario import Usuario

# Criando o controle de acesso
_acesso = ControleAcesso()

# Cadastrando os usuários
_acesso.cadastrar(
    Usuario("1001", "Ana Souza", "senai123", ["solicitante"],
            supervisor="1002")
)

_acesso.cadastrar(
    Usuario("1002", "Bruno Lima", "senai123",
            ["supervisor", "solicitante"])
)

_acesso.cadastrar(
    Usuario("1003", "Carla Mendes", "senai123",
            ["almoxarifado"])
)


# Devolve o controle de acesso
def controle_acesso():
    return _acesso


# Busca um usuário pela matrícula
def buscar(matricula):
    return _acesso.buscar(matricula)
