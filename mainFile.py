'''
Senior project rpg game
Atreyu Blum 
2026

'''

def main():
    print("Welcome to the RPG game!")
    enter_name = input("Enter your character's name: ")
    character_class = input("Choose your character class (warrior, mage, rogue): ").strip().lower()

    experience_points = 0
    skill_points = 0
    level = 1
    skills = []
    inventory = []
    stats = {
        "health": 100,
        "mana": 50,
        "stamina": 50,
        "strength": 10,
        "intelligence": 10,
        "agility": 10,
    }
    if character_class == "warrior":
        skills = ["Sword Mastery", "Shield Block", "Berserk"]
        inventory = ["Sword", "Shield", "Health Potion"]
        stats["health"] += 50
        stats["strength"] += 5
        stats["stamina"] += 5
        stats["mana"] -= 20
        stats["intelligence"] -= 2
        stats["agility"] -= 2
    elif character_class == "mage":
        skills = ["Fireball", "Ice Shard", "Lightning Bolt"]
        inventory = ["Staff", "Spellbook", "Mana Potion"]
        stats["health"] -= 20
        stats["mana"] += 50
        stats["stamina"] -= 10
        stats["strength"] -= 2
        stats["intelligence"] += 5
        stats["agility"] -= 2
    elif character_class == "rogue":
        skills = ["Stealth", "Backstab", "Poison"]
        inventory = ["Dagger", "Lockpick", "Smoke Bomb"]
        stats["health"] -= 10
        stats["mana"] -= 10
        stats["stamina"] += 10
        stats["strength"] += 2
        stats["intelligence"] -= 2
        stats["agility"] += 5
    else:
        skills = []
        inventory = []

    print(f"Welcome, {enter_name} the {character_class.title()}! Your adventure begins now.")
    return enter_name, character_class, level, experience_points, skill_points, skills, inventory


def level_up(experience_points, skill_points, character_class, skills, level):
    mage_skills = ["Arcane Blast", "Frost Nova", "Chain Lightning", "Meteor Strike"]
    warrior_skills = ["Lightning Strike", "Shield Bash", "Flame Slash", "Whirlwind Attack"]
    rogue_skills = ["Shadow Step", "Poison Blade", "Evasion", "Smoke Screen"]

    if experience_points >= 10 * level:
        print("Congratulations! You've leveled up!")
        level += 1
        skill_points += 1
        experience_points -= 10 * level
        print(f"You are now level {level} and have {skill_points} skill points.")


        if character_class == "warrior":
            print(f"Choose a skill: {', '.join(warrior_skills)}:")
            choice = input().lower()
            if choice == "lightning strike":
                skills.append("Lightning Strike")
                skill_points -= 1
                warrior_skills.remove("Lightning Strike")
                print("You have used 1 skill point to learn Lightning Strike.")
            elif choice == "shield bash":
                skills.append("Shield Bash")
                skill_points -= 1
                warrior_skills.remove("Shield Bash")
                print("You have used 1 skill point to learn Shield Bash.")
            elif choice == "flame slash":
                skills.append("Flame Slash")
                skill_points -= 1
                print("You have used 1 skill point to learn Flame Slash.")
            elif choice == "whirlwind attack":
                skills.append("Whirlwind Attack")
                skill_points -= 1
                warrior_skills.remove("Whirlwind Attack")
                print("You have used 1 skill point to learn Whirlwind Attack.")
            else:
                print("Invalid skill choice.")
        elif character_class == "mage":
            print(f"Choose a skill: {', '.join(mage_skills)}:")
            choice = input().lower()
            if choice == "arcane blast":
                skills.append("Arcane Blast")
                skill_points -= 1
                mage_skills.remove("Arcane Blast")
                print("You have used 1 skill point to learn Arcane Blast.")
            elif choice == "frost nova":
                skills.append("Frost Nova")
                skill_points -= 1
                mage_skills.remove("Frost Nova")
                print("You have used 1 skill point to learn Frost Nova.")
            elif choice == "chain lightning":
                skills.append("Chain Lightning")
                skill_points -= 1
                mage_skills.remove("Chain Lightning")
                print("You have used 1 skill point to learn Chain Lightning.")
            elif choice == "meteor strike":
                skills.append("Meteor Strike")
                skill_points -= 1
                mage_skills.remove("Meteor Strike")
                print("You have used 1 skill point to learn Meteor Strike.")
            else:
                print("Invalid skill choice.")
        elif character_class == "rogue":
            print(f"Choose a skill: {', '.join(rogue_skills)}:")
            choice = input().lower()
            if choice == "shadow step":
                skills.append("Shadow Step")
                skill_points -= 1
                rogue_skills.remove("Shadow Step")
                print("You have used 1 skill point to learn Shadow Step.")
            elif choice == "poison blade":
                skills.append("Poison Blade")
                skill_points -= 1
                rogue_skills.remove("Poison Blade")
                print("You have used 1 skill point to learn Poison Blade.")
            elif choice == "evasion":
                skills.append("Evasion")
                skill_points -= 1
                rogue_skills.remove("Evasion")
                print("You have used 1 skill point to learn Evasion.")
            elif choice == "smoke screen":
                skills.append("Smoke Screen")
                skill_points -= 1
                rogue_skills.remove("Smoke Screen")
                print("You have used 1 skill point to learn Smoke Screen.")
            else:
                print("Invalid skill choice.")

    return experience_points, skill_points, level, skills


def game_loop():
    character_name, character_class, level, experience_points, skill_points, skills, inventory, stats = main()

    while True:
        print("You wake up in a small village and see a path leading into the forest. Do you want to go into the forest? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            print("You venture into the forest...")
            print("You encounter a goblin! Do you want to fight it? (yes/no/)")
            fight_choice = input().lower()
            if fight_choice == "yes":
                print("You decide to fight the goblin!")
                if character_class == "warrior":
                    print("As a Warrior, you swing your sword and defeat the goblin, but not without taking some damage!")
                    stats["health"] -= 5
                    stats["stamina"] -= 5
                    experience_points += 10
                    print("You gain 10 experience points for defeating the goblin!")
                elif character_class == "mage":
                    print("As a Mage, you cast a powerful spell and defeat the goblin!")
                    stats["health"] -= 5
                    stats["mana"] -= 5
                    experience_points += 10
                    print("You gain 10 experience points for defeating the goblin!")
                elif character_class == "rogue":
                    print("As a Rogue, you sneak up and strike the goblin from behind, defeating it!")
                    stats["health"] -= 5
                    stats["stamina"] -= 5
                    experience_points += 10
                    print("You gain 10 experience points for defeating the goblin!")
                else:
                    print("You fight bravely and defeat the goblin!")
                    stats["health"] -= 20
                    stats["stamina"] -= 10
                    experience_points += 10
                    print("You gain 10 experience points for defeating the goblin!")


                experience_points, skill_points, level, skills = level_up(
                    experience_points,
                    skill_points,
                    character_class,
                    skills,
                    level,
                )
                
                print("After defeating the goblin, you continue walking through the forest and find a treasure chest! Do you want to open it? (yes/no)")
                chest_choice = input().lower()
                if chest_choice == "yes":
                    print("You open the treasure chest and find some gold!")
                    inventory.append("Gold")
                    experience_points += 20
                    print("You gain 20 experience points for finding the treasure!")
                    experience_points, skill_points, level, skills = level_up(
                        experience_points,
                        skill_points,
                        character_class,
                        skills,
                        level,
                    )
                    print(f"Your current inventory: {', '.join(inventory)}")

                    print(f"Your current skills: {', '.join(skills)}")
                    
                    print("You continue your adventure through the forest..")
                    print("You encounter a wild boar! Do you want to fight it? (yes/no)")
                    boar_choice = input().lower()
                    if boar_choice == "yes":
                        print("You decide to fight the wild boar!")
                        if character_class == "warrior":
                            print("As a Warrior, you charge at the boar and defeat it, but not without taking some damage!")
                            stats["health"] -= 10
                            stats["stamina"] -= 5
                            experience_points += 15
                            print("You gain 15 experience points for defeating the wild boar!")
                        elif character_class == "mage":
                            print("As a Mage, you cast a powerful spell and defeat the wild boar!")
                            stats["health"] -= 10
                            stats["mana"] -= 5
                            experience_points += 15
                            print("You gain 15 experience points for defeating the wild boar!")
                        elif character_class == "rogue":
                            print("As a Rogue, you sneak up and strike the wild boar from behind, defeating it!")
                            stats["health"] -= 10
                            stats["stamina"] -= 5
                            experience_points += 15
                            print("You gain 15 experience points for defeating the wild boar!")
                        else:
                            print("You fight bravely and defeat the wild boar!")
                            stats["health"] -= 20
                            stats["stamina"] -= 10
                            experience_points += 15
                            print("You gain 15 experience points for defeating the wild boar!")

                        experience_points, skill_points, level, skills = level_up(
                            experience_points,
                            skill_points,
                            character_class,
                            skills,
                            level,
                        )
                        print("You continue your adventure through the forest..")
                        print("You enconter a bard playing music! Do you want to listen to the bard? (yes/no)")
                        bard_choice = input().lower()
                        if bard_choice == "yes":
                            print("You listen to the bard's music and feel inspired! You gain 10 experience points!")
                            experience_points += 10
                            experience_points, skill_points, level, skills = level_up(
                                experience_points,
                                skill_points,
                                character_class,
                                skills,
                                level,
                            )
                            print("You continue your adventure through the forest..")
                            print("You encounter a group of bandits! Do you want to fight them? (yes/no)")
                            bandit_choice = input().lower()
                            if bandit_choice == "yes":
                                print("You decide to fight the bandits!")
                                if character_class == "warrior":
                                    print("As a Warrior, you charge at the bandits and defeat them, but not without taking some damage!")
                                    stats["health"] -= 20
                                    stats["stamina"] -= 10
                                    experience_points += 30
                                    print("You gain 30 experience points for defeating the bandits!")
                                elif character_class == "mage":
                                    print("As a Mage, you cast powerful spells and defeat the bandits!")
                                    stats["health"] -= 20
                                    stats["mana"] -= 10
                                    experience_points += 30
                                    print("You gain 30 experience points for defeating the bandits!")
                                elif character_class == "rogue":
                                    print("As a Rogue, you sneak up and strike the bandits from behind, defeating them!")
                                    stats["health"] -= 20
                                    stats["stamina"] -= 10
                                    experience_points += 30
                                    print("You gain 30 experience points for defeating the bandits!")
                                else:
                                    print("You fight bravely and defeat the bandits!")
                                    stats["health"] -= 40
                                    stats["stamina"] -= 20
                                    experience_points += 30
                                    print("You gain 30 experience points for defeating the bandits!")

                                experience_points, skill_points, level, skills = level_up(
                                    experience_points,
                                    skill_points,
                                    character_class,
                                    skills,
                                    level,
                                )
                                print("You continue your adventure through the forest..")
                                print("You find a hidden cave! Do you want to explore it? (yes/no)")
                                cave_choice = input().lower()
                                if cave_choice == "yes":
                                    print("You explore the hidden cave and find a rare artifact! You gain 50 experience points!")
                                    inventory.append("Rare Artifact")
                                    experience_points += 50
                                    experience_points, skill_points, level, skills = level_up(
                                        experience_points,
                                        skill_points,
                                        character_class,
                                        skills,
                                        level,
                                    )
                                    print("Do you want to use the rare artifact? (yes/no)")
                                    rare_artifact_choice = input().lower()
                                    if rare_artifact_choice == "yes":
                                        print("You decide to use the rare artifact and gain a powerful new skill!")
                                        if character_class == "warrior":
                                            skills.append("Earthquake")
                                            print("You have learned Earthquake!")
                                        elif character_class == "mage":
                                            skills.append("Time Warp")
                                            print("You have learned Time Warp!")
                                        elif character_class == "rogue":
                                            skills.append("Shadow Clone")
                                            print("You have learned Shadow Clone!")
                                        print(f"Your current skills: {', '.join(skills)}")
                                        print("You continue your adventure through the forest..")
                                        print("You encounter a vampire! Do you want to fight it? (yes/no)")
                                        vampire_choice = input().lower()
                                        if vampire_choice == "yes":
                                            print("You decide to fight the vampire!")
                                            if character_class == "warrior":
                                                print("As a Warrior, you charge at the vampire and defeat it, but not without taking some damage!")
                                                stats["health"] -= 30
                                                stats["stamina"] -= 20
                                                experience_points += 50
                                                print("You gain 50 experience points for defeating the vampire!")
                                            elif character_class == "mage":
                                                print("As a Mage, you cast powerful spells and defeat the vampire!")
                                                stats["health"] -= 30
                                                stats["mana"] -= 20
                                                experience_points += 50
                                                print("You gain 50 experience points for defeating the vampire!")
                                            elif character_class == "rogue":
                                                print("As a Rogue, you sneak up and strike the vampire from behind, defeating it!")
                                                stats["health"] -= 30
                                                stats["stamina"] -= 20
                                                experience_points += 50
                                                print("You gain 50 experience points for defeating the vampire!")
                                            else:
                                                print("You fight bravely and defeat the vampire!")
                                                stats["health"] -= 60
                                                stats["stamina"] -= 40
                                                experience_points += 50
                                                print("You gain 50 experience points for defeating the vampire!")

                                            experience_points, skill_points, level, skills = level_up(
                                                experience_points,
                                                skill_points,
                                                character_class,
                                                skills,
                                                level,
                                            )
                                            print("when you defeat the vampire, you find a stone mask in its lair! Do you want to take the stone mask? (yes/no)")
                                            stone_mask_choice = input().lower()
                                            if stone_mask_choice == "yes":
                                                print("An enscription on the mask tells you that to gain the power of the stone mask you need to wear it on your face and soke the mask in blood. Do you want to wear the stone mask? (yes/no)")
                                                wear_stone_mask_choice = input().lower()
                                                if wear_stone_mask_choice == "yes":
                                                    print("You wear the stone mask and soak it in blood, gaining the power of the stone mask! You gain 100 experience points but you become a vampire! You have also gained the skill 'Vampiric Bite'!")
                                                    inventory.append("Stone Mask")
                                                    experience_points += 100
                                                    skills.append("Vampiric Bite")

                                                    experience_points, skill_points, level, skills = level_up(
                                                        experience_points,
                                                        skill_points,
                                                        character_class,
                                                        skills,
                                                        level,
                                                    )

                                                elif wear_stone_mask_choice == "no":
                                                    print("You decide not to wear the stone mask.")

                                        


                                elif cave_choice == "no":
                                    print("You decide not to explore the hidden cave.")

                elif chest_choice == "no":
                    print("You decide not to open the treasure chest.")

            elif fight_choice == "no":
                print("You avoid the goblin.")

                print("You continue walking through the forest and find a treasure chest! Do you want to open it? (yes/no)")
                chest_choice = input().lower()
                if chest_choice == "yes":
                    print("You open the treasure chest and find some gold!")
                    inventory.append("Gold")
                    experience_points += 20
                    print("You gain 20 experience points for finding the treasure!")
                    level_up(experience_points, skill_points, character_class, skills, level)

                    
                elif chest_choice == "no":
                    print("You decide not to open the treasure chest.")

                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
        elif choice == "no":
            print("You decide to stay in the village.")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    game_loop()
