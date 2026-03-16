'''
Senior project rpg game
Atreyu Blum 
2026

'''
def main():
    print("Welcome to the RPG game!")
    # Initialize game variables and start the game loop here

def get_character_info():
    enter_name = input("Enter your character's name: ")
    character_class = input("Choose your character class (Warrior, Mage, Rogue): ")
    print(f"Welcome, {enter_name} the {character_class}! Your adventure begins now.")
    return enter_name, character_class

def game_loop():
    character_name, character_class = get_character_info()
    experience_points = 0
    skill_points = 0
    skills = []
    inventory = []

    while True:
        print("You wake up in small village and see a path leading into the forest. Do you want to go into the forest? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            print("You venture into the forest...")
            print("You enconter a goblin! Do you want to fight it? (yes/no)")
            fight_choice = input().lower()
            if fight_choice == "yes":
                print("You decide to fight the goblin!")
                if character_class == "Warrior":
                    print("As a Warrior, you swing your sword and defeat the goblin!")
                elif character_class == "Mage":
                    print("As a Mage, you cast a powerful spell and defeat the goblin!")
                elif character_class == "Rogue":
                    print("As a Rogue, you sneak up and strike the goblin from behind, defeating it!")
                else:
                    print("You fight bravely but are unsure of your class's abilities, and you manage to defeat the goblin!")\
                
                if character_class == "Warrior" or character_class == "Mage" or character_class == "Rogue":
                    print("You gain 10 experience points for defeating the goblin!")
                    experience_points += 10
                    if experience_points >= 10:
                        print("Congratulations! You've leveled up!")

                        

            elif fight_choice == "no":
                print("You decide to avoid the goblin.")
                # Add more game logic here
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
            
        elif choice == "no":
            print("You decide to stay in the village.")
            # Add more game logic here
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
    get_character_info()
    game_loop()



