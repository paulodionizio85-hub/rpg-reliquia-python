import time

# ==========================================
# PROJETO: A Busca pela Relíquia de Python
# ==========================================

# Arte em texto para a tela de título
print("      /| ________________")
print("O|===|* >________________>")
print("      \\|")
print("")
print("=== BEM-VINDO À CAVERNA DOS ALGORITMOS ===\n")
time.sleep(1)

print("A lenda diz que você é um jovem aprendiz na lendária Guilda de Análise e Desenvolvimento de Sistemas...")
time.sleep(3)

print("Para provar seu valor e se tornar um Mestre Programador, você deve encontrar o artefato perdido: A Relíquia de Python.")
time.sleep(3)

print("Mas cuidado... a caverna não perdoa erros de lógica.\n")
time.sleep(2)

nome_heroi = input("Mestre Ancião: 'Diga-me, aprendiz... qual é o seu nome?' ")
energia_heroi = 100

print("\nO aprendiz", nome_heroi, "inicia sua jornada com", energia_heroi, "pontos de energia.")
print("--------------------------------------------------")
time.sleep(2)

# FASE 1: A Ponte da Lógica (Matemática)
print("FASE 1: Você chega a uma ponte vigiada por um Troll.")
time.sleep(1)
print("Troll: 'Para passar, resolva meu enigma matemático!'")
print("Troll: 'Se você tem 50 moedas, gasta 15 na taverna e acha um baú com 20... com quantas moedas você fica?'")

resposta_moedas = input("Sua resposta: ")

if resposta_moedas == "55":
    print("Troll: 'Pode passar, aventureiro esperto!'")
else:
    print("Troll: 'Errado! Tome uma paulada!'")
    energia_heroi = energia_heroi - 20
    print("Você perdeu 20 de energia. Energia atual:", energia_heroi)

print("--------------------------------------------------")
time.sleep(2)

# FASE 2: A Porta de Pedra (Repetição e Decisão)
print("FASE 2: Você encontra uma imensa Porta de Pedra com 3 cristais brilhantes.")
tentativas = 3
porta_aberta = False

# Laço de repetição: continua enquanto houver tentativas
while tentativas > 0:
    senha = input("Qual é a senha mágica gravada na porta? ")

    if senha == "Python":
        print("A porta de pedra se abre com um estrondo!")
        tentativas = 0  # Força a saída do laço
        porta_aberta = True
    else:
        print("Senha incorreta! Um cristal se apaga.")
        tentativas = tentativas - 1
        porta_aberta = False

if porta_aberta == False:
    print("Todos os cristais se apagaram. A porta trancou para sempre.")
    print("=== FIM DE JOGO ===")
    energia_heroi = 0 # Fim de jogo para o herói

# FASE 3: O Chefe Final (Apenas se a porta abriu e o herói está vivo)
if energia_heroi > 0 and porta_aberta == True:
    print("--------------------------------------------------")
    time.sleep(2)
    print("FASE 3: A SALA DA RELÍQUIA!")
    print("Um Guardião de Fogo aparece para proteger o tesouro!")
    
    energia_chefe = 50
    
    # Batalha: o laço continua enquanto os dois estiverem vivos
    while energia_heroi > 0 and energia_chefe > 0:
        print("\nEnergia do Herói:", energia_heroi, "| Energia do Chefe:", energia_chefe)
        acao = input("Digite 'atacar' para golpear: ")
        
        if acao == "atacar":
            print("Você desfere um golpe de espada! (-25 no Chefe)")
            energia_chefe = energia_chefe - 25
            time.sleep(1)
            
            # O Chefe revida se ainda estiver vivo
            if energia_chefe > 0:
                print("O Guardião revida com uma bola de fogo! (-30 no Herói)")
                energia_heroi = energia_heroi - 30
                time.sleep(1)
        else:
            print("Você hesitou! O Guardião te acerta em cheio! (-30 no Herói)")
            energia_heroi = energia_heroi - 30
            time.sleep(1)

    # Verifica quem venceu a batalha
    print("--------------------------------------------------")
    if energia_heroi > 0:
        print("O Guardião de Fogo virou cinzas!")
        print("🏆 PARABÉNS,", nome_heroi, "! Você conquistou a Relíquia de Python!")
    else:
        print("Você caiu em batalha...")
        print("=== FIM DE JOGO ===")