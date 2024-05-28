#lista de nomes das pessouas 
import random
import tkinter as tk

nomes = ["Alice", "Bob", "Carlos", "Diana", "Eva", "Fernando", "Gisele", "Hugo", "Igor", "Julia", "Klaus","davi","natanael","marquinho","jhonata","luan"]

#embaralha a lista de pessoas aleatorias
random.shuffle(nomes)

equipe1 = nomes[:4]
equipe2= nomes[4:8]
equipe3= nomes[8:12]
equipe4 = nomes[12:16]

print(f"equipe-1:\n ", equipe1)
print(f"equipe_2:\n ", equipe2)
print(f"equipe_3:\n ", equipe3)
print(f"equipe_4:\n ", equipe4)

random.shuffle(equipe1)
random.shuffle(equipe2)
random.shuffle(equipe3)
random.shuffle(equipe4)

print(f"equipe-1:\n ", equipe1)
print(f"equipe_2:\n ", equipe2)
print(f"equipe_3:\n ", equipe3)
print(f"equipe_4:\n ", equipe4)

#print(f"equipe-1:\n ", equipe1)
#print(f"equipe_2:\n ", equipe2)
#print(f"equipe_3:\n ", equipe3)
#print(f"equipe_4:\n ", equipe4)

# janela no tkinter para mostrar os resultados
janela = tk.Tk()
janela.title("Resultado")
janela.geometry("600x400")

#label para mostrar o resultado
tk.Label(janela, text="Resultado", font=("Arial", 20)).pack()

#label para mostrar o resultado
tk.Label(janela, text=f"Equipe 1 {equipe1}", font=("Arial", 20)).pack()

#label para mostrar o resultado
tk.Label(janela, text="Equipe 2", font=("Arial", 20)).pack()

#label para mostrar o resultado
tk.Label(janela, text="Equipe 3", font=("Arial", 20)).pack()

#label para mostrar o resultado
tk.Label(janela, text="Equipe 4", font=("Arial", 20)).pack()

janela.mainloop()
