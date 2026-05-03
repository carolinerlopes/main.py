from colorama import Fore, Style, init

init()

def definir_alerta_reservatorio(nivel):
    """
    Função principal que associa o nível à mensagem e cor correspondente.
    """
    niveis = [
        {"msg": "Muito baixo (crítico)", "cor": Fore.RED},    # Nível 1
        {"msg": "Baixo", "cor": Fore.YELLOW},                 # Nível 2
        {"msg": "Médio", "cor": Fore.GREEN},                  # Nível 3
        {"msg": "Alto", "cor": Fore.CYAN},                   # Nível 4
        {"msg": "Muito alto (alerta)", "cor": Fore.BLUE}      # Nível 5
    ]

    indice = nivel - 1
    
    if 0 <= indice < len(niveis):
        alerta = niveis[indice]
        print(f"Status do Reservatório [Nível {nivel}]: {alerta['cor']}{alerta['msg']}{Style.RESET_ALL}")
    else:
        print(f"Erro: Nível {nivel} está fora da faixa de monitoramento.")

# --- ÁREA DE TESTES ---
if __name__ == "__main__":
    print("--- INICIANDO SIMULAÇÃO DE MONITORAMENTO ---\n")
    
    # Lista de dados fictícios para simular o sensor 
    leituras_do_dia = [3, 4, 5, 2, 1, 3] 
    
    for leitura in leituras_do_dia:
        definir_alerta_reservatorio(leitura)
        
    print("\n--- FIM DA SIMULAÇÃO ---")