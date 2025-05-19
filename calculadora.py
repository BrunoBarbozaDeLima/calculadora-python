def calculadora():
    while True:
        try:
            # Solicita os dois números
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Solicita a operação
            operacao = input("Digite a operação (+, -, *, /): ")

            # Realiza a operação
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida.")

            # Exibe o resultado e encerra o programa
            print(f"Resultado: {resultado}")
            break

        except ValueError as ve:
            print(f"Erro: {ve}. Tente novamente.")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

# Executa a calculadora
calculadora()
