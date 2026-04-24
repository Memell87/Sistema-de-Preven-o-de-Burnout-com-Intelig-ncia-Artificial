from datetime import datetime

class ContaBancaria:
    LIMITE = 500
    LIMITE_SAQUES = 3

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"{datetime.now()} - Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.LIMITE
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"{datetime.now()} - Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return
        if valor > self.saldo:
            print("Operação falhou! Saldo insuficiente para transferência.")
            return

        # Realiza a transferência
        self.saldo -= valor
        conta_destino.saldo += valor

        self.extrato += f"{datetime.now()} - Transferência enviada: R$ {valor:.2f} para {conta_destino.titular}\n"
        conta_destino.extrato += f"{datetime.now()} - Transferência recebida: R$ {valor:.2f} de {self.titular}\n"

        print(f"Transferência de R$ {valor:.2f} para {conta_destino.titular} realizada com sucesso!")

    def mostrar_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("==========================================")

# Programa principal
def main():
    conta1 = ContaBancaria("Maria")
    conta2 = ContaBancaria("João")

    menu = """
    [d] Depositar
    [s] Sacar
    [t] Transferir
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                conta1.depositar(valor)
            except ValueError:
                print("Entrada inválida! Digite um número.")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                conta1.sacar(valor)
            except ValueError:
                print("Entrada inválida! Digite um número.")

        elif opcao == "t":
            try:
                valor = float(input("Informe o valor da transferência: "))
                conta1.transferir(valor, conta2)
            except ValueError:
                print("Entrada inválida! Digite um número.")

        elif opcao == "e":
            print("\nExtrato da conta de Maria:")
            conta1.mostrar_extrato()
            print("\nExtrato da conta de João:")
            conta2.mostrar_extrato()

        elif opcao == "q":
            print("Saindo... Obrigado por usar nosso sistema!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
