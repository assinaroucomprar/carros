def calcular_valor_total_financiamento(principal, taxa_juros_mensal, periodos):
    """
    Calcula o valor total a ser pago em um financiamento com base na fórmula de juros compostos.

    :param principal: Valor inicial do financiamento.
    :param taxa_juros_mensal: Taxa de juros mensal (em percentual).
    :param periodos: Número total de meses do financiamento.
    :return: Valor total a ser pago.
    """
    taxa_juros_mensal = taxa_juros_mensal / 100  # Convertendo a taxa de juros para forma decimal
    valor_total = principal * ((1 + taxa_juros_mensal) ** periodos)
    return valor_total

def calcular_taxa_juros_mensal(valor_futuro, valor_atual, meses):
    """
    Calcula a taxa de juros mensal para juros compostos.

    :param valor_futuro: Valor total ao final do período (Valor Futuro).
    :param valor_atual: Valor inicial do empréstimo ou investimento (Valor Atual).
    :param meses: Total de meses do período de investimento ou empréstimo.
    :return: Taxa de juros mensal.
    """
    taxa_juros = (valor_futuro / valor_atual) ** (1 / meses) - 1
    return taxa_juros * 100

def calcular_valor_futuro(valor_inicial, taxa_juros, n_meses):
    """
    Calcula o valor futuro de um investimento a uma taxa de juros composta durante n meses.

    :param valor_inicial: O valor inicial do investimento.
    :param taxa_juros: A taxa de juros mensal (em porcentagem).
    :param n_meses: O número de meses que o dinheiro será investido.
    :return: O valor futuro do investimento.
    """

    # Convertendo a taxa de juros para uma forma decimal
    taxa_juros_decimal = taxa_juros / 100

    # Calculando o valor futuro usando a fórmula de juros compostos
    valor_futuro = valor_inicial * ((1 + taxa_juros_decimal) ** n_meses)

    return valor_futuro




def soma_custos_veiculo(valor_veiculo):
    """
    Calcula a soma dos custos adicionais de um veículo financiado, incluindo IPVA, licenciamento e manutenção.

    :param valor_veiculo: Valor de compra do veículo.
    :return: Soma total dos custos adicionais.
    """
    # IPVA: Geralmente é cerca de 4% do valor do veículo, mas pode variar dependendo do estado.
    ipva = valor_veiculo * 0.04

    # Licenciamento: O custo pode variar muito, mas uma média nacional poderia ser R$150.

    # Manutenção: Estima-se que custe cerca de 1% do valor do veículo por ano.
    manutencao = valor_veiculo * 0.01

    # Seguro: O custo do seguro pode variar muito, mas uma média pode ser 3% do valor do veículo.
    seguro = valor_veiculo * 0.03

    return ipva + licenciamento + manutencao + seguro

def calcular_valor_investimento_mensal(investimento_mensal, taxa_juros_mensal, periodos):
    """
    Calcula o valor acumulado de um investimento realizado mensalmente, usando a fórmula de juros compostos.

    :param investimento_mensal: Valor a ser investido mensalmente.
    :param taxa_juros_mensal: Taxa de juros mensal (em percentual).
    :param periodos: Número total de meses do investimento.
    :return: Valor acumulado ao final do período.
    """
    taxa_juros_mensal = taxa_juros_mensal / 100  # Convertendo a taxa de juros para forma decimal
    valor_acumulado = 0

    for mes in range(1, periodos + 1):
        valor_acumulado += investimento_mensal * ((1 + taxa_juros_mensal) ** mes)

    return valor_acumulado

def calcular_custo_total_aluguel(valor_mensal, periodos):
    """
    Calcula o custo total de um aluguel de carro com base no valor mensal e no número de meses.

    :param valor_mensal: Valor do aluguel mensal do carro.
    :param periodos: Número total de meses do aluguel.
    :return: Custo total do aluguel.
    """
    custo_total = valor_mensal * periodos
    return custo_total

def calcular_valor_parcela_composto(juro_mensal, valor_total, prazo_meses, valor_entrada):
    # Calculando o valor financiado, subtraindo a entrada do valor total
    valor_financiado = valor_total - valor_entrada

    # Convertendo a taxa de juros para decimal
    juro_mensal_decimal = juro_mensal / 100

    # Utilizando a fórmula de parcela de empréstimo com juros compostos
    if juro_mensal_decimal > 0 and prazo_meses > 0:
        valor_parcela = valor_financiado * (juro_mensal_decimal * (1 + juro_mensal_decimal) ** prazo_meses) / ((1 + juro_mensal_decimal) ** prazo_meses - 1)
    else:
        # Se não há juros, a parcela é simplesmente o valor financiado dividido pelo número de meses
        valor_parcela = valor_financiado / prazo_meses

    return valor_parcela

# Exemplo de uso da função com juros compostos
#parcela_composta = calcular_valor_parcela_composto(juro_mensal, valor_total, prazo_meses, valor_entrada)
#parcela_composta

def calcular_desvalorizacao_veiculo(valor_zero_km, anos):
    """
    Calcula a desvalorização aproximada de um veículo com base no valor zero km e no número de anos.

    :param valor_zero_km: Valor do veículo zero km.
    :param anos: Número de anos desde a compra do veículo.
    :return: Valor estimado do veículo após a desvalorização.
    """
    # Taxa de desvalorização no primeiro ano: cerca de 20%
    # Taxa de desvalorização nos anos subsequentes: aproximadamente 10% ao ano
    if anos > 0:
        desvalorizacao_primeiro_ano = valor_zero_km * 0.20
        valor_apos_primeiro_ano = valor_zero_km - desvalorizacao_primeiro_ano

        for ano in range(1, int(anos)):
            valor_apos_primeiro_ano *= 0.90

        return valor_apos_primeiro_ano
    else:
        return valor_zero_km


retorno_investimento_custos_extras = 0
valor_futuro_entrada = 0
valor_veiculo = float(input('Entre com o valor FIPE do veículo: '))
valor_entrada = float(input('Entre com o valor da entrada no finaciamento do veículo: '))
licenciamento = float(300.0)
valor_mensal_aluguel = float(input('Entre com o valor mensal do aluguel do veículo: '))
periodos = int(input('Entre com o período em meses do aluguel: '))
taxa_juros_mensal = float(input('Entre com a taxa de juros mensal: '))
# Solicitando ao usuário a decisão sobre as taxas
SN = input('Investe valor das taxas?: S/N')
SNE = input('Investe valor da entrada?: S/N')

if SN.lower() == 's':
    print("Incluindo o valor das taxas no cálculo.")
    incluir_taxas = True
    taxa_juros_investimento = float(input('Entre com a taxa de juros do investimento: '))
else:
    print("Não incluindo o valor das taxas no cálculo.")
    incluir_taxas = False

if SNE.lower() == 's':
    print("Incluindo o valor das taxas no cálculo.")
    investir_entrada = True
    taxa_juros_entrada = float(input('Entre com a taxa de juros do investimento da entrada: '))
    valor_futuro_entrada = calcular_valor_futuro(valor_entrada, taxa_juros_entrada, periodos)
else:
    print("Não incluindo o valor das taxas no cálculo.")
    investir_entrada = False



custo_aluguel = calcular_custo_total_aluguel(valor_mensal_aluguel, periodos)
custo_financiamento = calcular_valor_total_financiamento(valor_veiculo - valor_entrada, taxa_juros_mensal, periodos) + valor_entrada
custos_extras_carro_financiado = soma_custos_veiculo(valor_veiculo)
custos_mensais = custos_extras_carro_financiado/12

investimento_mensal = custos_mensais
anos_de_uso = periodos / 12

valor_venda_veiculo = calcular_desvalorizacao_veiculo(valor_veiculo, anos_de_uso)




Valor_total_compra = custo_financiamento + custos_extras_carro_financiado - valor_venda_veiculo

valor_parcela = calcular_valor_parcela_composto(taxa_juros_mensal, valor_veiculo, periodos, valor_entrada)

if(incluir_taxas):
    retorno_investimento_custos_extras = calcular_valor_investimento_mensal(investimento_mensal, taxa_juros_investimento, periodos)
    Valor_total_assinatura = custo_aluguel - retorno_investimento_custos_extras
    custo_financiamento_igualar = custo_aluguel - custos_extras_carro_financiado + valor_venda_veiculo
else:
    Valor_total_assinatura = custo_aluguel
    custo_financiamento_igualar = custo_aluguel -  custos_extras_carro_financiado + valor_venda_veiculo



juros_para_igualar_custos = calcular_taxa_juros_mensal(custo_financiamento_igualar, valor_veiculo, periodos)

juro_mensal_decimal = juros_para_igualar_custos / 100

# Aplicando a fórmula de juro composto
juro_anual_decimal = (1 + juro_mensal_decimal) ** 12 - 1

# Convertendo de volta para porcentagem
juro_anual_para_igualar_custos = juro_anual_decimal * 100


##
## O calculo leva em conta a venda do carro no final do financiamento.
## Assim em ambas as modalidades no final não se tem o veiculo na mão
##

print(""" O calculo abaixo tem o objetivo de comparar financiamento e assinatura de carros
          O valor total da compra finaciada é calculado com a seguinte equacao:

          valor_total_compra = valor_pago_pelo_carro + IPVA + Licenciamento + manutencoes - valor_venda_apos_periodo

          valor_total_assinatura = valor_da_mensalidade x Periodo - investimento do valor das taxas

          O investimento do valor das taxas consiste em pegar o que se pagaria de ipva, licenciamento, manutencoes e investir mensalmente durante o periodo

          """)

print(f"Valor Total Compra Financiada: {Valor_total_compra:.2f}")
print(f"Valor Parcela Financiamento: {valor_parcela:.2f}")

print(f"Valor Total Assinatura sem descontar investimento: {custo_aluguel:.2f}")
print(f"Valor Total Assinatura descontando investimento: {Valor_total_assinatura - valor_futuro_entrada:.2f}")

print(f"Valor Final Investimento Entrada: {valor_futuro_entrada:.2f}")
print(f"Valor Final Investimento Custos extras: {retorno_investimento_custos_extras:.2f}")

print(f"Juros do financiamento para igualar Assinatura: {juros_para_igualar_custos:.2f}")
print(f"Juros ANUAL do financiamento para igualar Assinatura: {juro_anual_para_igualar_custos:.2f}")
