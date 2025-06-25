import customtkinter as ctk
from tkinter import messagebox 

#configuração Inicial
ctk.set_appearance_mode("black")
ctk.set_default_color_theme("green") 

#Criar janela principal
janela = ctk.CTk() #Função de criar a tela
janela.title("r") 
janela.geometry("400x300") 

#Código em si
def verificar_habilitacao():   
    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if not nome or not idade:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return
    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "A idade precisa ser um número inteiro.")
        return

    if idade >= 18:
        resultado.configure(text=f"{nome}, você está apto(a) a dirigir!")
        
    else:
        resultado.configure(text=f"{nome}, você NÃO está apto(a) a dirigir.")
        
        
    
 #Label digite seu nome
label_nome = ctk.CTkLabel(janela, text="Digite seu nome ")
label_nome.pack(pady=(20, 5))
entrada_nome = ctk.CTkEntry(janela,width=250)
entrada_nome.pack(pady=(5, 5))
#Label de Digite sua idade
label_idade = ctk.CTkLabel(janela, text="Digite sua idade")
label_idade.pack(pady=(5, 20))

entrada_idade = ctk.CTkEntry(janela,width=250)
entrada_idade.pack(pady=(5, 5))


#Botão de Verificar
botao_verificar = ctk.CTkButton(janela, text="Verificar Habilitação", command=verificar_habilitacao)
botao_verificar.pack(pady=(20, 10))

#Label do resultado
resultado = ctk.CTkLabel(janela, text="")
resultado.pack(pady=(20, 10))

# Executa a função
janela.mainloop()  # Mantém a janela aberta





