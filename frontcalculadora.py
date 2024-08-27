#Essa aplicação recebe 2 valores e uma operação (/*-+), executa o calculo e mostra o resultado em uma interface
import customtkinter as CTk # Importação do modulo custom tkinter
def entradadedados():
    "Função que recebe os dados n1, n2 e a função calculo e retorna na interface o que foi digitado pelo usuario"
    global n1, n2, eopcao #Declara as variaveis n1 = numero 1, n2 = numero2 e eopcao= opcao digitada pelo usuario como globais
    n1 = int(en1.get()) #Captura a variavel n1 do tipo inteiro com o metodo get
    n2 = int(en2.get()) #Captura a variavel n2 do tipo inteiro com o metodo get
    eopcao = str(opcao.get()) #Captura a variavel eopcao do tipo string com o metodo get
    calculo() #Função calculo define o calculo a ser feito atraves da condicional if com base no que foi digitado pelo usuario
    return n1, n2, eopcao, calculo # A função entrada de dados retorna o que foi digitado nas entradas n1, n2, eopcao e na saida calculo
def adicao(): 
    "Quando acionada pela função calculo, essa função calcula a soma de n1 e n2"
    resultado = n1 + n2 #A variavel resultado armazena a soma de n1 e n2
    Label_resultado.configure(text = f'A soma é {resultado}') #Label que exibe o resultado da soma interface
def subtração(): 
    "Quando acionada pela função calculo, essa função calcula a subtração de n1 e n2"
    resultado = n1 - n2 #A variavel resultado armazena a subtração de n1 e n2
    Label_resultado.configure(text = f'A diferença é {resultado}') #Label que exibe o resultado da subtração na interface
def mutiplicação():
    "Quando acionada pela função calculo, essa função calcula o produto de n1 e n2"
    resultado = n1 * n2  #A variavel resultado armazena  o produto de n1 e n2
    Label_resultado.configure(text = f'O produto é {resultado}')  #Label que exibe o resultado da mutiplicação na interface
def divisao():
    resultado = n1/n2
    Label_resultado.configure(text = f'O quociente é {resultado}')
def calculo():
    "Define o calculo a ser feito atraves da condicional if com base no que foi digitado pelo usuario"
    if eopcao == '+': 
        adicao() #se a variavel eopcao receber o caractere +, a função adição é acionada
    elif eopcao == '-':
        subtração() #se a variavel eopcao receber o caractere -, a função subtração é acionada
    elif eopcao == '*':
        mutiplicação() #se a variavel eopcao receber o caractere *, a função mutiplicação é acionada
    elif eopcao == '/':
        divisao() #se a variavel eopcao receber o caractere /, a função adição é acionada
menu_inicial = CTk.CTk() #Inicialização da variavel menu inicial recebendo a função interface
menu_inicial.title("Calculadora de 2 entradas") #Titulo da interface menu_inicial
CTk.set_appearance_mode("dark") #Aparencia da interface menu_inicial
menu_inicial.geometry("500x500")  #Geometria da interface menu_inicial
menu_inicial.resizable(False, False)  #Apenas função pop up
Label_en1 = CTk.CTkLabel(menu_inicial, text= "Digite o número 1", width= 115, height= 15, text_color="#F2F2F2",) #Label instruindo o usuario a digitar o numero 1
Label_en1.place(x = 181, y = 50)  #Posicionamento da Label_en1
en1 = CTk.CTkEntry(master = menu_inicial,
                    placeholder_text= "Número 1",
                    width= 115,
                    height= 40,
                    fg_color="#05AFF2", text_color="#F2F2F2", placeholder_text_color="#FFFFFF", border_color= "#F2F2F2"
) #Entrada da variavel n1
en1.place(x = 181, y = 70) #posicionamento da entrada variavel n1
en2 = CTk.CTkEntry(master = menu_inicial,
                    placeholder_text= "Número 2",
                    width= 115,
                    height= 40,
                    fg_color="#05AFF2", text_color="#F2F2F2", placeholder_text_color="#FFFFFF", border_color= "#F2F2F2"

) #Entrada da variavel n2
en2.place(x = 181, y = 144) #posicionamento da entrada variavel n2
Label_en2 = CTk.CTkLabel(menu_inicial, text= "Digite o número 2", width= 115, height= 15, text_color="#F2F2F2",)  #Label instruindo o usuario a digitar o numero 2
Label_en2.place(x = 181, y = 124)  #Posicionamento da Label_en2
opcao = CTk.CTkEntry(master = menu_inicial,
                    placeholder_text= "Operação escolhida + - * /",
                    width= 130,
                    height= 40,
                    fg_color="#05AFF2", text_color="#F2F2F2", placeholder_text_color="#FFFFFF", border_color= "#F2F2F2"
) #Entrada da variavel opcao
opcao.place(x = 181, y = 218) #Posicionamento da entrada variavel opcao
Label_opcao = CTk.CTkLabel(menu_inicial, text= "Digite a operação +, -, *, /", width= 115, height= 15, text_color="#F2F2F2",)  #Label instruindo o usuario a digitar a operação
Label_opcao.place(x = 181, y = 198)   #Posicionamento da Label_opcao
ent = CTk.CTkButton(menu_inicial, text= "Calcular", command= entradadedados, width= 115, height = 40, 
                    fg_color="#05AFF2", text_color="#F2F2F2", border_color= "#F2F2F2") #Botao para executar a operação a partir do comando entrada de dados
ent.place(x = 181, y = 292)  #Posicionamento do botão
Label = CTk.CTkLabel(menu_inicial, text= 'Calculadora',
                    fg_color="#05AFF2", text_color="#F2F2F2",
                    width= 115,
                    height = 30,)#Label titulo
Label.place(x = 181, y = 0)#Posicionamento da label titulo
Label_resultado = CTk.CTkLabel(menu_inicial, text= "Resultado", width= 140, height= 40, fg_color="#05AFF2", text_color="#F2F2F2",)#Label para mostrar resultado
Label_resultado.place(x = 181, y = 350) #Posicionamento da label resultado
menu_inicial.mainloop() #comando para exibir a interface