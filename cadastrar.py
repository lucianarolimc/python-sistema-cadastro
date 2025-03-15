import tkinter as tk
from tkinter import ttk
import datetime as dt
from functools import partial


def obter_dados_janela(lista_linha_dados, entrada_dados_descricao,
                       combobox_selecionar_tipo, entrada_dados_quantidade):

    """
    Obtém os dados de entrada informados na janela de cadastro.
    : lista_linha_dados: lista para armazenar os dados cadastrados
    : entrada_dados_descricao: entrada de dados da descrição dos materiais
    : combobox_selecionar_tipo: entrada de dados dos tipos de unidades dos materiais
    : entrada_dados_quantidade: entrada de dados da quantidade dos materiais
    """

    descricao = entrada_dados_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quantidade = entrada_dados_quantidade.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H: %M")
    codigo_id_ = len(lista_linha_dados)+1
    codigo_id_str = "COD-{}".format(codigo_id_)

    lista_linha_dados.append((codigo_id_str, descricao, tipo, quantidade, data_criacao))


def criar_janela_cadastro(lista_linha_dados):

    """
    Cria a janela de cadastro com os rótulos e
    espaços para entradas de dados.
    : lista_linha_dados: lista para armazenar os dados cadastrados
    """

    # lista com opções de unidade
    lista_tipos = ["Galão", "Caixa", "Saco", "Unidade"]
    
    # criar janela
    janela = tk.Tk()

    # título da janela
    janela.title("Ferramenta de cadastro de materiais")

    # criar um rótulo de descrição
    rotulo_descricao = tk.Label(text="Descrição do Material")

    # posicionar o rótulo dentro da janela
    rotulo_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

    # criar a entrada de dados para inserir a descrição do material
    entrada_dados_descricao = tk.Entry()

    # adicionar a entrada de dados à janela
    entrada_dados_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

    # criar a rótulo de tipo de unidade
    rotulo_tipo_unidade = tk.Label(text="Tipo da unidade do material")

    # adicionar o rótulo à janela
    rotulo_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # criar uma caixa com uma lista de opções
    combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)

    # adicionar o combobox à janela
    combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

    # criar o rótulo da quantidade
    rotulo_qtd = tk.Label(text="Quantidade da unidade de material")

    # adicionar o rótulo de quantidade à janela
    rotulo_qtd.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # criar uma entrada de dados de quantidade
    entrada_dados_quantidade = tk.Entry()

    # adicionar a entrada de quantidade à janela
    entrada_dados_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

    # usar a função 'partial' para passar a função com argumentos
    obter_dados_janela_arg = partial(obter_dados_janela, lista_linha_dados, entrada_dados_descricao,
                       combobox_selecionar_tipo, entrada_dados_quantidade)

    # criar um botão para submeter as informações
    botao_ok = tk.Button(text="Enviar dados", command=obter_dados_janela_arg)
    # botao_ok = tk.Button(text="Enviar dados")

    # adicionar o botão ok à janela
    botao_ok.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

    janela.mainloop()

    print(lista_linha_dados)
    
def main():

    # inicializar lista que armazenará as linhas de dados
    lista_linha_dados = []

    # criar janela de cadastro
    criar_janela_cadastro(lista_linha_dados)

if __name__ == "__main__":
    main()



