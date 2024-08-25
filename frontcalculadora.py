import customtkinter as CTk
def entradadedados():
    global n1, n2, eopcao
    n1 = int(en1.get())
    n2 = int(en2.get())
    eopcao = str(opcao.get())
    calculo()
    return n1, n2, eopcao, calculo
def adicao():
    resultado = n1 + n2
    Label_resultado.configure(text = f'A soma é {resultado}')
def subtração():
    resultado = n1 - n2
    Label_resultado.configure(text = f'A diferença é {resultado}')
def mutiplicação():
    resultado = n1 * n2
    Label_resultado.configure(text = f'O produto é {resultado}')
def divisao():
    resultado = n1/n2
    Label_resultado.configure(text = f'O quociente é {resultado}')
def calculo():
    if eopcao == '+':
        adicao()
    elif eopcao == '-':
        subtração()
    elif eopcao == '*':
        mutiplicação()
    elif eopcao == '/':
        divisao()
menu_inicial = CTk.CTk()
menu_inicial.title("Calculadora de 2 entradas")
CTk.set_appearance_mode("dark")
menu_inicial.geometry("500x500")
menu_inicial.resizable(False, False)
Label_en1 = CTk.CTkLabel(menu_inicial, text= "Digite o número 1", width= 115, height= 15, text_color="#F2F2F2",)
Label_en1.place(x = 181, y = 50)  
en1 = CTk.CTkEntry(master = menu_inicial,
                    placeholder_text= "Número 1",
                    width= 115,
                    height= 40,
                    fg_color="#05AFF2", text_color="#F2F2F2", placeholder_text_color="#FFFFFF", border_color= "#F2F2F2"
)
en1.place(x = 181, y = 70)
en2 = CTk.CTkEntry(master = menu_inicial,
                    placeholder_text= "Número 2",
                    width= 115,
                    height= 40,
                    fg_color="#05AFF2", text_color="#F2F2F2", placeholder_text_color="#FFFFFF", border_color= "#F2F2F2"

)
en2.place(x = 181, y = 144)
Label_en2 = CTk.CTkLabel(menu_inicial, text= "Digite o número 2", width= 115, height= 15, text_color="#F2F2F2",)
Label_en2.place(x = 181, y = 124)  
opcao = CTk.CTkEntry(master = menu_inicial,
                    placeholder_text= "Operação escolhida + - * /",
                    width= 130,
                    height= 40,
                    fg_color="#05AFF2", text_color="#F2F2F2", placeholder_text_color="#FFFFFF", border_color= "#F2F2F2"
)
opcao.place(x = 181, y = 218)
Label_opcao = CTk.CTkLabel(menu_inicial, text= "Digite a operação +, -, *, /", width= 115, height= 15, text_color="#F2F2F2",)
Label_opcao.place(x = 181, y = 198)  
ent = CTk.CTkButton(menu_inicial, text= "Calcular", command= entradadedados, width= 115, height = 40, 
                    fg_color="#05AFF2", text_color="#F2F2F2", border_color= "#F2F2F2")
ent.place(x = 181, y = 292)
Label = CTk.CTkLabel(menu_inicial, text= 'Calculadora',
                    fg_color="#05AFF2", text_color="#F2F2F2",
                    width= 115,
                    height = 30,)
Label.place(x = 181, y = 0)
Label_resultado = CTk.CTkLabel(menu_inicial, text= "Resultado", width= 140, height= 40, fg_color="#05AFF2", text_color="#F2F2F2",)
Label_resultado.place(x = 181, y = 350)
menu_inicial.mainloop()