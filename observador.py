from datetime import date

def formatCnpj(value):
    date = str(value)
    return f"{date[0]}{date[1]}.{date[2]}{date[3]}{date[4]}.{date[5]}{date[6]}{date[7]}/{date[8]}{date[9]}{date[10]}-{date[11]}{date[12]}"

def imprime(razao_social, cnpj,pessoas):
    print(f"\n[] Imprimindo NF para {razao_social} - {formatCnpj(cnpj)}\n")
    for i in pessoas:  
        if pessoas != []:
            notifica(i, razao_social, cnpj)
    print("")
    print(f"[V] NF para {razao_social} - {formatCnpj(cnpj)} impressa!\n\n")
    
def mail(razao_social, cnpj, pessoas):
    print(f"[] Mandando por email NF para {razao_social} - {formatCnpj(cnpj)}\n")
    for i in pessoas:  
        if pessoas != []:
            notifica(i, razao_social, cnpj)
    print("")
    print(f"[V] NF enviada por email!\n\n")
    
def salva(razao_social, cnpj):
    print(f"[] Salvando NF para {razao_social} - {formatCnpj(cnpj)}\n")
    print(f"[V] Salva com sucesso!\n\n")
    
def notifica(pessoa, razao_social, cnpj):
    print(f"[V] Notificando {pessoa} sobre NF para {razao_social} - {formatCnpj(cnpj)}...\n")
    
    
def gerenciaNf(razao_social, cnpj, pessoas=[]):
    imprime(razao_social, cnpj, pessoas)
    mail(razao_social, cnpj, pessoas)
    salva(razao_social, cnpj)