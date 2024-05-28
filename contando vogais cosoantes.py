vogais = "aeiou"
soma_vogais = 0
texto = int(input("digit uma frase:  "))

for palavra in texto:
    if palavra in vogais:
        soma_vogais  +=1
    elif  palavra ==' ':
        espaco = espaco + 1
 
        print(f'vogais:  {soma_vogais}/n  ')
               
        

       