
# testes/teste_api.py
from fastapi.testclient import TestClient

from main import app

api = TestClient(app)


# Faz o login e devolve o cabeçalho com o token
def entrar(matricula):
    resposta = api.post(
        "/auth/login",
        json={"matricula": matricula, "senha": "senai123"}
    )
    return {"Authorization": "Bearer " + resposta.json()["token"]}


print("Saúde:", api.get("/saude").json())

print("=== Login ===")
r = api.post("/auth/login", json={"matricula": "1001", "senha": "errada"})
print(r.status_code, r.json())

ana = entrar("1001")
bruno = entrar("1002")
carla = entrar("1003")

print(api.get("/auth/eu", headers=ana).json()["nome"])
print("Sem token:", api.get("/produtos").status_code)

print("=== Estoque ===")
print("Ana dá entrada:", api.post(
    "/produtos/P002/entrada",
    json={"quantidade": 5},
    headers=ana
).status_code)

r = api.post(
    "/produtos/P002/entrada",
    json={"quantidade": 5},
    headers=carla
)
print("Carla dá entrada:", r.status_code, r.json()["quantidade"])

r = api.post(
    "/produtos/P003/saida",
    json={"quantidade": 1},
    headers=carla
)
print("Saída sem saldo:", r.status_code, r.json()["detail"])

print("=== Solicitação ===")
r = api.post(
    "/pedidos",
    json={"itens": [{"codigo": "P003", "quantidade": 10}]},
    headers=ana
)
print("Ana abre:", r.status_code, r.json()["numero"], r.json()["status"])

r = api.patch("/pedidos/2026-0001/aprovar", headers=carla)
print("Carla aprova:", r.status_code, r.json()["detail"])

r = api.patch("/pedidos/2026-0001/aprovar", headers=bruno)
print("Bruno aprova:", r.status_code, r.json()["status"])

r = api.patch("/pedidos/2026-0001/avancar", headers=carla)
print("Carla avança:", r.status_code, r.json()["status"])

print(
    "Pedido que não existe:",
    api.get("/pedidos/2026-0099", headers=ana).status_code
)

