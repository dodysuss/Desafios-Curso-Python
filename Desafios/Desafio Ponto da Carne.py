tem_cel = int(input("Digite a temperatura da carne: "))

if tem_cel < 48:
    print("A carne precisa cozinhar por mais tempo.")
elif tem_cel in range(48, 53):
    print("A carne está selada.")
elif tem_cel in range(54, 59):
    print("A carne está ao ponto para mal passada.")
elif tem_cel in range(60, 64):
    print("A carne está ao ponto.")
elif tem_cel in range(65, 70):
    print("A carne está ao ponto para bem passada.")
else:
    print("A carne está bem passada.")