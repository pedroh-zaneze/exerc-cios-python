nome_usuario = input("Digite o seu nome:")
senha = input("Digite a sua senha (APENAS ALFANUMÉRICOS):")
senha_limpa = senha.replace(" ", "").replace(".", "").replace(",", "").replace(";", "").replace(":", "").replace("-", "").replace("_", "").replace("!", "").replace("?", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("|", "").replace("\\", "").replace("/", "").replace("+", "").replace("=", "").replace("<", "").replace(">", "").replace("'", "").replace('"', "").replace("`", "").replace("^", "").replace("~", "").replace("´", "").replace("`", "")
print(f"Senha limpa {senha_limpa}")


