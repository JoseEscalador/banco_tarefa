extrato = {}
saldo = 0
cont_op = 1
saques = 0

def alimentar_extrato (op, valor,cont_op):
    valor = str(valor)
    if op == "saque":
        extrato[f"{cont_op}: {op.upper()}"] = "    - " + valor
    elif op == "deposito":
        extrato[f"{cont_op}: {op.upper()}"] = f" + {valor}"
    
    print(f"operação de número: {cont_op}")

# def erro(valor):
#     while not valor.isnumeric():
#         input("Tente novamente digitando apenas números: ")

op = input("Qual operação você deseja realizar? (DEPOSITO/SAQUE/EXTRATO/SALDO/SAIR) ").lower()


while not op == "sair":
    if op == "deposito":
        valor = int(input("Qual é o valor a ser depositado?"))
        #erro(valor)
        saldo = saldo + valor
        alimentar_extrato(op, valor, cont_op)
        cont_op = cont_op + 1
    elif op == "saque":
        valor = int(input("Qual é o valor a ser sacado?"))
        #erro(valor)
        if valor > saldo:
            print("Você não possui saldo suficiente")
        elif valor <= 500 and not saques == 3:
            saldo = saldo - valor
            alimentar_extrato(op, valor, cont_op)
            cont_op = cont_op + 1
            saques = saques + 1
        else:
            print("Não foi possível realizar o saque")
    elif op == "extrato":
        for key in extrato.keys():
            print(f"{key}: {extrato.get(key)} ")
    elif op == "saldo":        
        print(f"R$ {float(saldo):.2f} ".replace(".",","))
    op = input("Qual operação você deseja realizar? (DEPOSITO/SAQUE/EXTRATO/SALDO/SAIR) ").lower()