import tkinter as tk
from tkinter import Scrollbar, Text, END
import difflib
import webbrowser

# Dicionário de dicas de segurança da informação
dicas_seguranca = {
    "senha forte": "Use senhas fortes que incluam letras maiúsculas, minúsculas, números e caracteres especiais. Evite senhas óbvias, como '123456' ou 'senha'.",
    "senha":"Use senhas fortes que incluam letras maiúsculas, minúsculas, números e caracteres especiais. Evite senhas óbvias, como '123456' ou 'senha'.",
    "senhas":"Use senhas fortes que incluam letras maiúsculas, minúsculas, números e caracteres especiais. Evite senhas óbvias, como '123456' ou 'senha'.",
    "autenticação de dois fatores":"Ative a autenticação de dois fatores sempre que possível. Isso fornece uma camada adicional de segurança para suas contas online.",
    "dois fatores":"Ative a autenticação de dois fatores sempre que possível. Isso fornece uma camada adicional de segurança para suas contas online.",
    "atualização de software": "Mantenha seu sistema operacional e software atualizados. As atualizações frequentes muitas vezes corrigem vulnerabilidades de segurança.",
    "phishing": "Tenha cuidado com e-mails e mensagens suspeitas. Não clique em links ou baixe anexos de remetentes desconhecidos.",
    "backups regulares": "Faça backups regulares de seus dados importantes. Isso ajuda a proteger seus dados contra perda devido a falhas ou ataques.",
    "backups": "Faça backups regulares de seus dados importantes. Isso ajuda a proteger seus dados contra perda devido a falhas ou ataques.",
    "uso de VPN": "Ao acessar redes Wi-Fi públicas, use uma VPN para criptografar sua conexão e proteger seus dados contra interceptação.",
    "VPN":"Ao acessar redes Wi-Fi públicas, use uma VPN para criptografar sua conexão e proteger seus dados contra interceptação.",
    "vpn":"Ao acessar redes Wi-Fi públicas, use uma VPN para criptografar sua conexão e proteger seus dados contra interceptação.",
    "autenticação de dois fatores por SMS": "Evite a autenticação de dois fatores por SMS, pois mensagens de texto podem ser interceptadas. Prefira aplicativos de autenticação ou chaves de segurança.",
    "dois fatores por SMS":"Evite a autenticação de dois fatores por SMS, pois mensagens de texto podem ser interceptadas. Prefira aplicativos de autenticação ou chaves de segurança.",
    "navegação segura": "Utilize um navegador seguro e evite sites não confiáveis. Verifique se há um cadeado na barra de endereços ao inserir informações pessoais.",
    "navegar": "Utilize um navegador seguro e evite sites não confiáveis. Verifique se há um cadeado na barra de endereços ao inserir informações pessoais.",
    "senhas exclusivas": "Use senhas exclusivas para cada conta online. Um gerenciador de senhas pode ajudar a manter o controle delas.",
    "criptografia de dados": "Sempre que possível, use a criptografia para proteger seus dados. Isso impede que terceiros acessem informações confidenciais.",
    "criptografia": "Sempre que possível, use a criptografia para proteger seus dados. Isso impede que terceiros acessem informações confidenciais.",
    "autenticação biométrica": "A autenticação biométrica, como impressões digitais ou reconhecimento facial, pode adicionar uma camada extra de segurança aos seus dispositivos.",
    "monitoramento de identidade": "Considere usar serviços de monitoramento de identidade para detectar atividades suspeitas relacionadas ao uso de suas informações pessoais.",
    "senhas temporárias": "Use senhas temporárias ou únicas para acessar serviços sensíveis e altere-as regularmente.",
    "atualização de firmware de dispositivos IoT": "Mantenha atualizados o firmware e o software de dispositivos de Internet das Coisas (IoT) para evitar vulnerabilidades de segurança.",
    "rede segura em casa": "Proteja sua rede doméstica com senhas fortes e altere as credenciais padrão de roteadores e dispositivos.",
    "rede residencial":"Proteja sua rede doméstica com senhas fortes e altere as credenciais padrão de roteadores e dispositivos.",
    "casa": "Proteja sua rede doméstica com senhas fortes e altere as credenciais padrão de roteadores e dispositivos.",
    "mínimo de privilégios": "Use a regra do princípio do mínimo de privilégios, concedendo apenas as permissões necessárias para executar uma tarefa.",
    "conscientização de phishing no local de trabalho": "Eduque os funcionários sobre ameaças de phishing e práticas seguras de segurança da informação no local de trabalho.",
    "segurança de e-mails comerciais": "Proteja e-mails comerciais com soluções de segurança, como filtros de spam e antivírus.",
    "e-mails": "Proteja e-mails comerciais com soluções de segurança, como filtros de spam e antivírus.",
    "análise de logs": "Monitore e analise regularmente logs de segurança para identificar atividades suspeitas.",
    "bloqueio de dispositivos móveis perdidos": "Habilite a capacidade de bloquear ou apagar remotamente dados de dispositivos móveis perdidos ou roubados.",
    "politica de segurança da informação": "Estabeleça e mantenha uma política de segurança da informação em sua organização para orientar práticas seguras.",
    "autenticação segura em redes Wi-Fi": "Ao se conectar a redes Wi-Fi públicas, evite redes abertas e use aquelas que exigem autenticação com senha.",
    "proteção contra malware": "Instale um antivírus e software anti-malware em seus dispositivos e mantenha-os atualizados.",
    "malware":"Instale um antivírus e software anti-malware em seus dispositivos e mantenha-os atualizados.",
    "verificação de segurança em redes sociais": "Revise e ajuste as configurações de privacidade em suas contas de redes sociais para controlar o que é compartilhado.",
    "verificação de autenticidade de sites": "Ao inserir informações pessoais em um site, verifique se ele é autêntico e seguro. Evite sites de phishing.",
}


# Função para obter dicas de segurança com base na pergunta
def obter_dica_seguranca(pergunta):
    pergunta = pergunta.lower()
    respostas = []
    for chave, dica in dicas_seguranca.items():
        if chave in pergunta:
            respostas.append(dica)
    if respostas:
        return "\n\n".join(respostas)
    else:
        # Procurar correspondências aproximadas para erros de digitação
        palavras_chave = list(dicas_seguranca.keys())
        sugestoes = difflib.get_close_matches(pergunta, palavras_chave, n=1, cutoff=0.6)
        if sugestoes:
            chave_sugerida = sugestoes[0]
            return f"Você quis dizer '{chave_sugerida}'? Aqui está uma dica de segurança: {dicas_seguranca[chave_sugerida]}"
        else:
            return "Desculpe, não entendi. Posso fornecer dicas de segurança da informação se você fizer uma pergunta específica."

# Função para lidar com a pergunta do usuário
def lidar_com_pergunta(event=None):
    pergunta = entrada.get("1.0", "end-1c")
    resposta_dica = obter_dica_seguranca(pergunta)
    if resposta_dica:
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, f"Você: {pergunta}\nChatBot (Dicas de Segurança): {resposta_dica}\n")
        chat.config(state=tk.DISABLED)
    else:
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, f"Você: {pergunta}\nChatBot: Desculpe, não entendi. Posso fornecer dicas de segurança da informação se você fizer uma pergunta específica.\n")
        chat.config(state=tk.DISABLED)
    entrada.delete("1.0", tk.END)

# Função para excluir as perguntas
def excluir_perguntas():
    chat.config(state=tk.NORMAL)
    chat.delete("1.0", tk.END)  # Limpa todo o texto da área de chat
    chat.config(state=tk.DISABLED)

# Função para buscar ajuda na internet
def buscar_ajuda_na_internet():
    pesquisa = entrada.get("1.0", "end-1c")
    if pesquisa:
        url = f"https://www.google.com/search?q={pesquisa}"
        webbrowser.open(url)

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("ChatBot de Segurança da Informação")

# Estilo personalizado
janela.geometry("600x400")
janela.configure(bg="#f2f2f2")

# Área de exibição do chat
chat = Text(janela, state=tk.DISABLED, wrap=tk.WORD, height=15, width=60, bg="#fff", font=("Arial", 12))
chat.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Barra de rolagem para o chat
scrollbar = Scrollbar(janela, command=chat.yview)
scrollbar.grid(row=0, column=2, sticky="nsew")
chat.config(yscrollcommand=scrollbar.set)

# Entrada de texto
entrada = Text(janela, wrap=tk.WORD, height=2, width=40, font=("Arial", 12))
entrada.grid(row=1, column=0, padx=10, pady=10)
entrada.bind("<Return>", lidar_com_pergunta)  # Associe a tecla "Enter" à função lidar_com_pergunta

# Botões
botao_enviar = tk.Button(janela, text="Enviar", command=lidar_com_pergunta, font=("Arial", 12), bg="#4CAF50", fg="#fff")
botao_enviar.grid(row=1, column=1, padx=10, pady=10, sticky="w")

botao_excluir = tk.Button(janela, text="Excluir Perguntas", command=excluir_perguntas, font=("Arial", 12), bg="#ff5733", fg="#fff")
botao_excluir.grid(row=2, column=0, padx=10, pady=10, sticky="w")

botao_buscar = tk.Button(janela, text="Buscar na Internet", command=buscar_ajuda_na_internet, font=("Arial", 12), bg="#3498db", fg="#fff")
botao_buscar.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Iniciar a interface gráfica
janela.mainloop()
