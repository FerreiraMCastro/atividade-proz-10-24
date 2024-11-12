def obter_nome():
    nome = input("Digite seu nome completo: ")
    return nome

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021)"))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("O ano de nascimento deve estar entre 1922 e 2021")
        except ValueError:
            print("Valor invalido! Por favor, insira em número inteiro valido para o ano.")
            
def calcular_idade(ano_nascimento):
    ano_atual = 2022
    idade = ano_atual - ano_nascimento
    return idade 

def main():
    nome = obter_nome()
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    
    print(f"{nome}, Você completará {idade} anos em 2022")
    
    
main()         