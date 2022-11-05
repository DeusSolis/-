dict_1 = {
    "Дублін": "Ірландія",
    "Рейк'явік": "Ісландія",
    "Мадрид": "Іспанія",
    "Рим": "Італія",
    "Відень": "Австрія",
    "Брюссель": "Бельгія",
    "Софія": "Болгарія"
}

while True:
    player_choise = str(input("Enter capital: "))
    if player_choise in dict_1:
        print(f"Так це столиця такої країни {dict_1.get(player_choise)}")
    elif player_choise == "Stop":
        break
    else:
        print("Ні на жаль це не столиця")


