#programme qui retourne si deux nombres entiers donnés sont de même signe ou non.
n1=int(input("Entrer le premier nombre :"))
n2=int(input("Entrer le deuxieme nombre :"))
if(n1>0 and n2>0 or n1<0 and n2<0):
    print(f"Les deux nombres {n1} et {n2} sont de meme signe")
else:
    print(f"Les deux nombres {n1} et {n2} non't pas le meme signe")

    
