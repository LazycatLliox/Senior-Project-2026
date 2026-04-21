'''
Senior project rpg game
Atreyu Blum 
2026

'''

skill_effects = {
    "Sword Mastery": {"damage_dealt": 5, "cost": {"stamina": 5}},
    "Shield Block": {"damage_taken": -5, "cost": {"stamina": 5}},
    "Berserk": {"damage_dealt": 10, "damage_taken": 5, "cost": {"stamina": 10}},
    "Fireball": {"damage_dealt": 10, "cost": {"mana": 10}},
    "Ice Shard": {"damage_dealt": 5, "damage_taken": -5, "cost": {"mana": 5}},
    "Lightning Bolt": {"damage_dealt": 15, "cost": {"mana": 15}},
    "Stealth": {"damage_dealt": 10, "cost": {"stamina": 5}},
    "Backstab": {"damage_dealt": 15, "cost": {"stamina": 10}},
    "Poison": {"damage_dealt": 5, "cost": {"stamina": 5}},
    "Lightning Strike": {"damage_dealt": 20, "cost": {"stamina": 15}},
    "Shield Bash": {"damage_dealt": 10, "damage_taken": -10, "cost": {"stamina": 10}},
    "Flame Slash": {"damage_dealt": 15, "cost": {"stamina": 10}},
    "Whirlwind Attack": {"damage_dealt": 25, "cost": {"stamina": 20}},
    "Arcane Blast": {"damage_dealt": 20, "cost": {"mana": 15}},
    "Frost Nova": {"damage_dealt": 10, "damage_taken": -10, "cost": {"mana": 10}},
    "Chain Lightning": {"damage_dealt": 25, "cost": {"mana": 20}},
    "Meteor Strike": {"damage_dealt": 30, "cost": {"mana": 25}},
    "Shadow Step": {"damage_dealt": 15, "cost": {"stamina": 10}},
    "Poison Blade": {"damage_dealt": 10, "cost": {"stamina": 5}},
    "Evasion": {"damage_taken": -15, "cost": {"stamina": 10}},
    "Smoke Screen": {"damage_taken": -10, "cost": {"stamina": 5}},
    "Earthquake": {"damage_dealt": 30, "cost": {"stamina": 20}},
    "Time Warp": {"damage_taken": -20, "cost": {"mana": 20}},
    "Shadow Clone": {"damage_dealt": 20, "cost": {"stamina": 15}},
    "Vampiric Bite": {"damage_dealt": 25, "cost": {"health": 10}},
    "Divine Smite": {"damage_dealt": 30, "cost": {"stamina": 20}},
    "Sunlight Slash": {"damage_dealt": 25, "cost": {"mana": 15}},
    "Field of Flowers": {"damage_dealt": 0, "cost": {"mana": 20}},
    "Iron Skin": {"stats": {"health": 20}, "cost": {"stamina": 15}},
}

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

    max_health = stats["health"]
    max_mana = stats["mana"]
    print(f"Welcome, {enter_name} the {character_class.title()}! Your adventure begins now.")
    return enter_name, character_class, level, experience_points, skill_points, skills, inventory, stats, max_health, max_mana


def use_health_potion(stats, inventory, max_health):
    if "Health Potion" in inventory:
        restore = 50
        old_health = stats["health"]
        stats["health"] = min(stats["health"] + restore, max_health)
        inventory.remove("Health Potion")
        print(f"You drink a health potion and restore {stats['health'] - old_health} health! Current health: {stats['health']}/{max_health}")
    else:
        print("You have no health potions!")


def check_status(stats, max_health, max_mana, skills, inventory):
    print(f"\n--- Character Status ---")
    print(f"Health: {stats['health']}/{max_health}")
    print(f"Mana: {stats['mana']}/{max_mana}")
    print(f"Stamina: {stats['stamina']}")
    print(f"Skills: {', '.join(skills) if skills else 'None'}")
    print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}")
    print("--- End Status ---\n")

    # Option to use item
    if inventory:
        print("Do you want to use an item? (yes/no)")
        use = input().lower().strip()
        if use == "yes":
            print(f"Choose an item to use: {', '.join(inventory)}")
            item = input().strip()
            if item in inventory:
                if item == "Health Potion":
                    use_health_potion(stats, inventory, max_health)
                elif item == "Mana Potion":
                    if "Mana Potion" in inventory:
                        restore = 50
                        old_mana = stats["mana"]
                        stats["mana"] = min(stats["mana"] + restore, max_mana)
                        inventory.remove("Mana Potion")
                        print(f"You drink a mana potion and restore {stats['mana'] - old_mana} mana! Current mana: {stats['mana']}/{max_mana}")
                    else:
                        print("You have no mana potions!")
                else:
                    print(f"You can't use {item} right now.")
            else:
                print("Invalid item.")
    else:
        print("Your inventory is empty.")


def prompt_yes_no_status(prompt, check_status_callback):
    while True:
        choice = input(prompt).lower().strip()
        if choice == "status":
            check_status_callback()
            continue
        if choice in ["yes", "no"]:
            return choice
        print("Please enter yes, no, or status.")


def apply_vampire_sunlight(is_vampire, stats, max_health, period):
    if not is_vampire:
        return False

    if period == "day":
        damage = 8
        print("Vampire weakness: daylight burns you for 8 health.")
        stats["health"] -= damage
    else:
        heal = min(5, max_health - stats["health"])
        if heal > 0:
            stats["health"] += heal
            print(f"Night comfort restores {heal} health to your vampire body.")
        else:
            print("You are already at full health at night.")

    if stats["health"] <= 0:
        print("The sunlight has killed you. You have died!")
        return True

    print(f"Current health: {stats['health']}/{max_health}")
    return False


def use_skill_in_combat(skills, stats, skill_effects):
    if not skills:
        return 0, 0
    
    print("Available skills:")
    for i, skill in enumerate(skills, 1):
        effect = skill_effects.get(skill, {})
        cost_str = ", ".join([f"{k}: {v}" for k, v in effect.get("cost", {}).items()])
        print(f"{i}. {skill} (Cost: {cost_str})")
    print("0. Don't use a skill")
    
    while True:
        try:
            choice = int(input("Choose a skill to use (number): "))
            if choice == 0:
                return 0, 0
            elif 1 <= choice <= len(skills):
                selected_skill = skills[choice - 1]
                effect = skill_effects.get(selected_skill, {})
                
                # Check if player has enough resources
                can_use = True
                for resource, cost in effect.get("cost", {}).items():
                    if stats.get(resource, 0) < cost:
                        print(f"Not enough {resource} to use {selected_skill}!")
                        can_use = False
                        break
                
                if can_use:
                    # Deduct costs
                    for resource, cost in effect.get("cost", {}).items():
                        stats[resource] -= cost
                    
                    damage_dealt_bonus = effect.get("damage_dealt", 0)
                    damage_taken_modifier = effect.get("damage_taken", 0)
                    print(f"You used {selected_skill}!")
                    return damage_dealt_bonus, damage_taken_modifier
                else:
                    print("Choose another skill or 0 to skip.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")


def perform_fight(enemy_name, base_damage_taken, base_stamina_cost, exp_reward, character_class, stats, skills, experience_points, max_health, inventory):
    damage_dealt_bonus, damage_taken_modifier = use_skill_in_combat(skills, stats, skill_effects)

    
    if character_class == "warrior":
        damage_taken = base_damage_taken + damage_taken_modifier
        stamina_cost = base_stamina_cost
        print(f"As a Warrior, you swing your sword and defeat the {enemy_name}, but not without taking some damage!")
    elif character_class == "mage":
        damage_taken = base_damage_taken + damage_taken_modifier
        mana_cost = base_stamina_cost
        print(f"As a Mage, you cast a powerful spell and defeat the {enemy_name}!")
    elif character_class == "rogue":
        damage_taken = base_damage_taken + damage_taken_modifier
        stamina_cost = base_stamina_cost
        print(f"As a Rogue, you sneak up and strike the {enemy_name} from behind, defeating it!")
    else:
        damage_taken = base_damage_taken * 2 + damage_taken_modifier
        stamina_cost = base_stamina_cost * 2
        print(f"You fight bravely and defeat the {enemy_name}!")

    if damage_dealt_bonus > 0:
        print(f"Your skill dealt extra {damage_dealt_bonus} damage!")

    stats["health"] -= max(0, damage_taken)
    if character_class == "mage":
        stats["mana"] -= mana_cost
    else:
        stats["stamina"] -= stamina_cost
    experience_points += exp_reward
    print(f"You gain {exp_reward} experience points for defeating the {enemy_name}!")

    if stats["health"] <= 0:
        print("Your health has dropped to zero. You have died!")
        return True
    if stats["health"] < max_health and "Health Potion" in inventory:
        print(f"Your current health: {stats['health']}/{max_health}. Do you want to drink a health potion? (yes/no)")
        potion_choice = input().lower()
        if potion_choice == "yes":
            use_health_potion(stats, inventory, max_health)
    return False


def level_up(experience_points, skill_points, character_class, skills, level, stats, max_health, max_mana, secondary_class):
    mage_skills = ["Arcane Blast", "Frost Nova", "Chain Lightning", "Meteor Strike"]
    warrior_skills = ["Lightning Strike", "Shield Bash", "Flame Slash", "Whirlwind Attack"]
    rogue_skills = ["Shadow Step", "Poison Blade", "Evasion", "Smoke Screen"]

    if experience_points >= 10 * level:
        print("Congratulations! You've leveled up!")
        level += 1
        skill_points += 1
        experience_points -= 10 * level
        print(f"You are now level {level} and have {skill_points} skill points.")

        # Stat increases
        print("Your stats have increased!")
        max_health += 10
        max_mana += 10
        stats["stamina"] += 5
        print(f"Max health +10 (now {max_health})")
        print(f"Max mana +10 (now {max_mana})")
        print("Stamina +5")
        print("You feel refreshed!")
        old_health = stats["health"]
        old_mana = stats["mana"]
        old_stamina = stats["stamina"]
        stats["health"] = min(stats["health"] + 20, max_health)
        stats["mana"] = min(stats["mana"] + 20, max_mana)
        stats["stamina"] += 10
        print(f"Health restored by {stats['health'] - old_health} (now {stats['health']}/{max_health})")
        print(f"Mana restored by {stats['mana'] - old_mana} (now {stats['mana']}/{max_mana})")
        print(f"Stamina restored by {stats['stamina'] - old_stamina}")

        primary_skills = {"warrior": warrior_skills, "mage": mage_skills, "rogue": rogue_skills}[character_class]
        available = [s for s in primary_skills if s not in skills]

        if not available and secondary_class is None:
            print("You have learned all skills from your primary class! Choose a secondary class to learn skills from: warrior, mage, rogue")
            while True:
                sec_choice = input().lower().strip()
                if sec_choice in ["warrior", "mage", "rogue"] and sec_choice != character_class:
                    secondary_class = sec_choice
                    if secondary_class == "warrior":
                        max_health += 20
                    elif secondary_class == "mage":
                        max_mana += 20
                    elif secondary_class == "rogue":
                        stats["stamina"] += 20
                    print(f"You have chosen {sec_choice.title()} as your secondary class!")
                    
                    break
                else:
                    print("Invalid choice or same as primary class.")

        if secondary_class:
            sec_skills = {"warrior": warrior_skills, "mage": mage_skills, "rogue": rogue_skills}[secondary_class]
            available.extend([s for s in sec_skills if s not in skills])

        if available:
            print(f"Choose a skill: {', '.join(s.lower() for s in available)}:")
            choice = input().lower().strip()
            matching = [s for s in available if s.lower() == choice]
            if matching:
                skill = matching[0]
                skills.append(skill)
                skill_points -= 1
                print(f"You have used 1 skill point to learn {skill}.")
            else:
                print("Invalid skill choice.")
        else:
            print("No new skills available.")

    return experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class


def game_loop():
    character_name, character_class, level, experience_points, skill_points, skills, inventory, stats, max_health, max_mana = main()
    secondary_class = None
    is_vampire = False
    time_of_day = 10  # 0-23 hour clock

    def time_period(hour):
        if 6 <= hour < 18:
            return "day"
        return "night"

    def advance_time(hours=1):
        nonlocal time_of_day
        time_of_day = (time_of_day + hours) % 24
        period = time_period(time_of_day)
        print(f"Time advances to {time_of_day:02d}:00 ({period})")
        return period

    while True:
        current_period = time_period(time_of_day)
        print(f"Current time: {time_of_day:02d}:00 ({current_period})")
        choice = prompt_yes_no_status("You wake up in a small village and see a path leading into the forest. Do you want to go into the forest? (yes/no/status) ",
                                     lambda: check_status(stats, max_health, max_mana, skills, inventory))
        if choice == "yes":
            print("You venture into the forest...")
            period = advance_time(1)
            if apply_vampire_sunlight(is_vampire, stats, max_health, period):
                return
            fight_choice = prompt_yes_no_status("You encounter a goblin! Do you want to fight it? (yes/no/status) ",
                                              lambda: check_status(stats, max_health, max_mana, skills, inventory))
            if fight_choice == "yes":
                if perform_fight("goblin", 5, 3, 10, character_class, stats, skills, experience_points, max_health, inventory):
                    return


                experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                    experience_points,
                    skill_points,
                    character_class,
                    skills,
                    level,
                    stats,
                    max_health,
                    max_mana,
                    secondary_class,
                )
                
                print("After defeating the goblin, you continue walking through the forest and find a treasure chest! Do you want to open it? (yes/no/status)")
                while True:
                    chest_choice = input().lower().strip()
                    if chest_choice == "status":
                        check_status(stats, max_health, max_mana, skills, inventory)
                        print("Do you want to open the treasure chest? (yes/no/status)")
                    elif chest_choice in ["yes", "no"]:
                        break
                    else:
                        print("Please enter yes, no, or status.")
                if chest_choice == "yes":
                    print("You open the treasure chest and find some gold!")
                    inventory.append("Gold")
                    experience_points += 20
                    print("You gain 20 experience points for finding the treasure!")
                    experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                        experience_points,
                        skill_points,
                        character_class,
                        skills,
                        level,
                        stats,
                        max_health,
                        max_mana,
                        secondary_class,
                    )
                    print(f"Your current inventory: {', '.join(inventory)}")

                    print(f"Your current skills: {', '.join(skills)}")
                    
                    print("You continue your adventure through the forest..")
                    period = advance_time(1)
                    if is_vampire:
                        if period == "day":
                            print("The sun beats down on you as you travel. Your vampire skin burns! You take 5 damage.")
                            stats["health"] -= 5
                        else:
                            heal = min(5, max_health - stats["health"])
                            if heal > 0:
                                stats["health"] += heal
                                print(f"The night soothes your vampire body, healing {heal} health.")
                            else:
                                print("You are already at full health.")
                        if stats["health"] <= 0:
                            print("The sunlight has overwhelmed you. You have died!")
                            return
                        print(f"Your current health: {stats['health']}/{max_health}")
                    boar_choice = prompt_yes_no_status("You encounter a wild boar! Do you want to fight it? (yes/no/status) ",
                                                   lambda: check_status(stats, max_health, max_mana, skills, inventory))
                    if boar_choice == "yes":
                        if perform_fight("wild boar", 10, 5, 15, character_class, stats, skills, experience_points, max_health, inventory):
                            return

                        experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                            experience_points,
                            skill_points,
                            character_class,
                            skills,
                            level,
                            stats,
                            max_health,
                            max_mana,
                            secondary_class,
                        )
                        print("You continue your adventure through the forest..")
                        period = advance_time(1)
                        if is_vampire:
                            if period == "day":
                                print("The forest sunlight continues to weaken you. You take 5 damage.")
                                stats["health"] -= 5
                            else:
                                heal = min(5, max_health - stats["health"])
                                if heal > 0:
                                    stats["health"] += heal
                                    print(f"The night soothes your vampire body, healing {heal} health.")
                                else:
                                    print("You are already at full health.")
                            if stats["health"] <= 0:
                                print("The prolonged sun exposure has killed you. You have died!")
                                return
                            print(f"Your current health: {stats['health']}/{max_health}")
                        print("You enconter a bard playing music! Do you want to listen to the bard? (yes/no/status)")
                        while True:
                            bard_choice = input().lower().strip()
                            if bard_choice == "status":
                                check_status(stats, max_health, max_mana, skills, inventory)
                                print("Do you want to listen to the bard? (yes/no/status)")
                            elif bard_choice in ["yes", "no"]:
                                break
                            else:
                                print("Please enter yes, no, or status.")
                        if bard_choice == "yes":
                            print("You listen to the bard's music and feel inspired! You gain 10 experience points!")
                            experience_points += 10
                            experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                experience_points,
                                skill_points,
                                character_class,
                                skills,
                                level,
                                stats,
                                max_health,
                                max_mana,
                                secondary_class,
                            )
                            print("You continue your adventure through the forest..")
                            print("You encounter a group of bandits! Do you want to fight them? (yes/no/status)")
                            while True:
                                bandit_choice = input().lower().strip()
                                if bandit_choice == "status":
                                    check_status(stats, max_health, max_mana, skills, inventory)
                                    print("Do you want to fight the bandits? (yes/no/status)")
                                elif bandit_choice in ["yes", "no"]:
                                    break
                                else:
                                    print("Please enter yes, no, or status.")
                            if bandit_choice == "yes":
                                if perform_fight("bandits", 20, 10, 30, character_class, stats, skills, experience_points, max_health, inventory):
                                    return

                                experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                    experience_points,
                                    skill_points,
                                    character_class,
                                    skills,
                                    level,
                                    stats,
                                    max_health,
                                    max_mana,
                                    secondary_class,
                                )
                                print("You continue your adventure through the forest..")
                                period = advance_time(1)
                                if is_vampire:
                                    if period == "day":
                                        print("The sun's rays pierce through the canopy, burning your vampire flesh! You take 5 damage.")
                                        stats["health"] -= 5
                                    else:
                                        heal = min(5, max_health - stats["health"])
                                        if heal > 0:
                                            stats["health"] += heal
                                            print(f"The night soothes your vampire body, healing {heal} health.")
                                        else:
                                            print("You are already at full health.")
                                    if stats["health"] <= 0:
                                        print("The sunlight has proven fatal. You have died!")
                                        return
                                    print(f"Your current health: {stats['health']}/{max_health}")
                                print("You find a hidden cave! Do you want to explore it? (yes/no/status)")
                                while True:
                                    cave_choice = input().lower().strip()
                                    if cave_choice == "status":
                                        check_status(stats, max_health, max_mana, skills, inventory)
                                        print("Do you want to explore the hidden cave? (yes/no/status)")
                                    elif cave_choice in ["yes", "no"]:
                                        break
                                    else:
                                        print("Please enter yes, no, or status.")
                                if cave_choice == "yes":
                                    print("You explore the hidden cave and find a rare artifact! You gain 50 experience points!")
                                    inventory.append("Rare Artifact")
                                    experience_points += 50
                                    experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                        experience_points,
                                        skill_points,
                                        character_class,
                                        skills,
                                        level,
                                        stats,
                                        max_health,
                                        max_mana,
                                        secondary_class,
                                    )
                                    print("Do you want to use the rare artifact? (yes/no/status)")
                                    while True:
                                        rare_artifact_choice = input().lower().strip()
                                        if rare_artifact_choice == "status":
                                            check_status(stats, max_health, max_mana, skills, inventory)
                                            print("Do you want to use the rare artifact? (yes/no/status)")
                                        elif rare_artifact_choice in ["yes", "no"]:
                                            break
                                        else:
                                            print("Please enter yes, no, or status.")
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
                                        if is_vampire:
                                            print("Emerging from the cave into the sunlight, you feel intense burning! You take 10 damage.")
                                            stats["health"] -= 10
                                            if stats["health"] <= 0:
                                                print("The sudden sunlight exposure has killed you. You have died!")
                                                return
                                            print(f"Your current health: {stats['health']}/{max_health}")
                                        print("You encounter a vampire! Do you want to fight it? (yes/no)")
                                        vampire_choice = input().lower()
                                        if vampire_choice == "yes":
                                            if perform_fight("vampire", 30, 20, 50, character_class, stats, skills, experience_points, max_health, inventory):
                                                return

                                            experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                experience_points,
                                                skill_points,
                                                character_class,
                                                skills,
                                                level,
                                                stats,
                                                max_health,
                                                max_mana,
                                                secondary_class,
                                            )
                                            print("when you defeat the vampire, you find a stone mask in its lair! Do you want to take the stone mask? (yes/no/status)")
                                            while True:
                                                stone_mask_choice = input().lower().strip()
                                                if stone_mask_choice == "status":
                                                    check_status(stats, max_health, max_mana, skills, inventory)
                                                    print("Do you want to take the stone mask? (yes/no/status)")
                                                elif stone_mask_choice in ["yes", "no"]:
                                                    break
                                                else:
                                                    print("Please enter yes, no, or status.")
                                            if stone_mask_choice == "yes":
                                                print("An enscription on the mask tells you that to gain the power of the stone mask you need to wear it on your face and soke the mask in blood. Do you want to wear the stone mask? (yes/no/status)")
                                                while True:
                                                    wear_stone_mask_choice = input().lower().strip()
                                                    if wear_stone_mask_choice == "status":
                                                        check_status(stats, max_health, max_mana, skills, inventory)
                                                        print("Do you want to wear the stone mask? (yes/no/status)")
                                                    elif wear_stone_mask_choice in ["yes", "no"]:
                                                        break
                                                    else:
                                                        print("Please enter yes, no, or status.")
                                                if wear_stone_mask_choice == "yes":
                                                    print("You wear the stone mask and soak it in blood, gaining the power of the stone mask! You gain 100 experience points but you become a vampire! You have also gained the skill 'Vampiric Bite'!")
                                                    print("As a vampire, you are now weak to sunlight. Exposure to the sun will burn your skin and cause damage!")
                                                    inventory.append("Stone Mask")
                                                    experience_points += 100
                                                    skills.append("Vampiric Bite")
                                                    max_health += 20
                                                    max_mana += 20
                                                    
                                                    is_vampire = True

                                                    experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                        experience_points,
                                                        skill_points,
                                                        character_class,
                                                        skills,
                                                        level,
                                                        stats,
                                                        max_health,
                                                        max_mana,
                                                        secondary_class,
                                                    )
                                                    print("You continue your adventure through the forest as a vampire...")
                                                    print("You come across a traveling merchant! Do you want to talk to the merchant? (yes/no/status)")
                                                    while True:
                                                        merchant_choice = input().lower().strip()
                                                        if merchant_choice == "status":
                                                            check_status(stats, max_health, max_mana, skills, inventory)
                                                            print("Do you want to talk to the merchant? (yes/no/status)")
                                                        elif merchant_choice in ["yes", "no"]:
                                                            break
                                                        else:
                                                            print("Please enter yes, no, or status.")
                                                    if merchant_choice == "yes":
                                                        print("The merchant offers to sell you a special item that can protect you from sunlight for a short time. Do you want to buy the Sunlight Amulet for 50 gold? (yes/no/status)")
                                                        while True:
                                                            amulet_choice = input().lower().strip()
                                                            if amulet_choice == "status":
                                                                check_status(stats, max_health, max_mana, skills, inventory)
                                                                print("Do you want to buy the Sunlight Amulet for 50 gold? (yes/no/status)")
                                                            elif amulet_choice in ["yes", "no"]:
                                                                break
                                                            else:
                                                                print("Please enter yes, no, or status.")
                                                        if amulet_choice == "yes":
                                                            if "Gold" in inventory:
                                                                inventory.remove("Gold")
                                                                inventory.append("Sunlight Amulet")
                                                                print("You buy the Sunlight Amulet and add it to your inventory! The Sunlight Amulet will protect you from sunlight damage for 3 turns when equipped!")
                                                            else:
                                                                print("You don't have enough gold to buy the Sunlight Amulet!")
                                                        elif amulet_choice == "no":
                                                            print("You decide not to buy the Sunlight Amulet.")
                                                        
                                                        print("You continue on your adventure after talking to the merchant...")
                                                        print("You encounter a group of vampire hunters! Do you want to fight them? (yes/no/status)")
                                                        while True:
                                                            hunters_choice = input().lower().strip()
                                                            if hunters_choice == "status":
                                                                check_status(stats, max_health, max_mana, skills, inventory)
                                                                print("Do you want to fight the vampire hunters? (yes/no/status)")
                                                            elif hunters_choice in ["yes", "no"]:
                                                                break
                                                            else:
                                                                print("Please enter yes, no, or status.")
                                                        if hunters_choice == "yes":
                                                            if perform_fight("vampire hunters", 40, 20, 60, character_class, stats, skills, experience_points, max_health, inventory):
                                                                return

                                                            experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                                experience_points,
                                                                skill_points,
                                                                character_class,
                                                                skills,
                                                                level,
                                                                stats,
                                                                max_health,
                                                                max_mana,
                                                                secondary_class,
                                                            )
                                                        
                                                            print("After defeating the vampire hunters, you continue your adventure through the forest as a powerful vampire!")
                                                            print("You have the power of the stone mask and the skills you have learned, making you a very formidable foe to any who cross your path!")
                                                            print("You come across a group of villagers who are terrified of you and beg you to leave them alone. Do you want to attack the villagers or let them be? (attack/let be/status)")
                                                            while True:
                                                                villagers_choice = input().lower().strip()
                                                                if villagers_choice == "status":
                                                                    check_status(stats, max_health, max_mana, skills, inventory)
                                                                    print("Do you want to attack the villagers or let them be? (attack/let be/status)")
                                                                elif villagers_choice in ["attack", "let be"]:
                                                                    break
                                                                else:
                                                                    print("Please enter attack, let be, or status.")
                                                            if villagers_choice == "attack":
                                                                print("You attack the villagers, causing chaos and destruction! You gain 20 experience points for attacking the villagers but you lose the respect of the nearby towns and villages!")
                                                                experience_points += 20
                                                                experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                                    experience_points,
                                                                    skill_points,
                                                                    character_class,
                                                                    skills,
                                                                    level,
                                                                    stats,
                                                                    max_health,
                                                                    max_mana,
                                                                    secondary_class,
                                                                )
                                                                print("You continue your adventure through the forest as a powerful vampire, but the nearby towns and villages are now hostile towards you due to your attack on the villagers.")
                                                                print("You run in to a man who is hear to hunt you down. Do to your attack on the villagers")
                                                                print("he has found you and is trying to kill you. Do you want to fight the vampire hunter or run away? (fight/run/status)")
                                                                hunters_choice = input("> ").lower().strip()

                                                                if hunters_choice == "fight":
                                                                    print("You decide to fight the vampire hunter!")
                                                                elif hunters_choice == "run":
                                                                    print("You decide to run away from the vampire hunter!")
                                                                elif hunters_choice == "status":
                                                                    print("Your status:")
                                                                    print(f"Experience Points: {experience_points}")
                                                                    print(f"Skill Points: {skill_points}")
                                                                    print(f"Level: {level}")
                                                                    print(f"Skills: {skills}")
                                                                    print(f"Stats: {stats}")
                                                                    print(f"Max Health: {max_health}")
                                                                    print(f"Max Mana: {max_mana}")
                                                                else:
                                                                    print("Please enter fight, run, or status.")
                                                                if hunters_choice == "fight":
                                                                    if perform_fight("vampire hunter", 40, 20, 60, character_class, stats, skills, experience_points, max_health, inventory):
                                                                        return

                                                                    experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                                        experience_points,
                                                                        skill_points,
                                                                        character_class,
                                                                        skills,
                                                                        level,
                                                                        stats,
                                                                        max_health,
                                                                        max_mana,
                                                                        secondary_class,
                                                                    )
                                                                    print("After defeating the vampire hunter you evolve into a vampire lord!")
                                                                    print("This is the end of the game, You Got the vampire lord ending congratulations!")
                                                                    return
                                                                if hunters_choice == "run":
                                                                    print("When you try to run away you are stabbed in the back by the vampire hunter and you die!")
                                                                    return
                                                            elif villagers_choice == "let be":
                                                                print("You decide to let the villagers be, showing mercy and restraint. The villagers are grateful and spread word of your kindness, improving your reputation in nearby towns and villages!")
                                                                print("You continue your adventure through the forest as a powerful vampire, and the nearby towns and villages are now more friendly towards you due to your mercy towards the villagers.")
                                                                print("This is the end of the game, You Got the merciful vampire ending congratulations!")
                                                                return
                                                        if hunters_choice == "no":
                                                            print("You avoid the vampire hunters and continue your adventure through the forest as a powerful vampire!")
                                                            print("You come across a group of villagers who are terrified of you and beg you to leave them alone. Do you want to attack the villagers or let them be? (attack/let be/status)")
                                                            while True:
                                                                villagers_choice = input().lower().strip()
                                                                if villagers_choice == "status":
                                                                    check_status(stats, max_health, max_mana, skills, inventory)
                                                                    print("Do you want to attack the villagers or let them be? (attack/let be/status)")
                                                                elif villagers_choice in ["attack", "let be"]:
                                                                    break
                                                                else:                                                                    
                                                                    print("Please enter attack, let be, or status.")
                                                            if villagers_choice == "attack":
                                                                print("You attack the villagers, causing chaos and destruction! You gain 20 experience points for attacking the villagers but you lose the respect of the nearby towns and villages!")
                                                                experience_points += 20
                                                                experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                                    experience_points,
                                                                    skill_points,
                                                                    character_class,
                                                                    skills,
                                                                    level,
                                                                    stats,
                                                                    max_health,
                                                                    max_mana,
                                                                    secondary_class,
                                                                )
                                                                print("You continue your adventure through the forest as a powerful vampire, but the nearby towns and villages are now hostile towards you due to your attack on the villagers.")
                                                                print("You run in to a man who is hear to hunt you down. Do to your attack on the villagers")
                                                                print("he has found you and is trying to kill you. Do you want to fight the vampire hunter or run away? (fight/run/status)")
                                                                if hunters_choice == "fight":
                                                                    print("You decide to fight the vampire hunter!")
                                                                    if perform_fight("vampire hunter", 40, 20, 60, character_class, stats, skills, experience_points, max_health, inventory):
                                                                        return

                                                                    experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                                        experience_points,
                                                                        skill_points,
                                                                        character_class,
                                                                        skills,
                                                                        level,
                                                                        stats,
                                                                        max_health,
                                                                        max_mana,
                                                                        secondary_class,
                                                                    )
                                                                    print("After defeating the vampire hunter you evolve into a vampire lord!")
                                                                    print("This is the end of the game, You Got the vampire lord ending congratulations!")
                                                                    return
                                                                
                                                                elif hunters_choice == "run":
                                                                    print("When you try to run away you are stabbed in the back by the vampire hunter and you die!")
                                                                    return

                                                elif wear_stone_mask_choice == "no":
                                                    print("You decide not to wear the stone mask.")
                                                    print("You come accross a group of vampire hunters! they tell you how dangerous the stone mask is and they urge you to get rid of it. Do you want to give the stone mask to the vampire hunters? (yes/no/status)")
                                                    while True:
                                                        give_stone_mask_choice = input().lower().strip()
                                                        if give_stone_mask_choice == "status":
                                                            check_status(stats, max_health, max_mana, skills, inventory)
                                                            print("Do you want to give the stone mask to the vampire hunters? (yes/no/status)")
                                                        elif give_stone_mask_choice in ["yes", "no"]:
                                                            break
                                                        else:
                                                            print("Please enter yes, no, or status.")
                                                    if give_stone_mask_choice == "yes":
                                                        inventory.remove("Stone Mask")
                                                        print("You give the stone mask to the vampire hunters. They thank you for getting rid of such a dangerous artifact and they reward you with 50 gold! You gain 50 experience points for giving the stone mask to the vampire hunters!")
                                                        inventory.append("Gold")
                                                        experience_points += 50
                                                        experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                            experience_points,
                                                            skill_points,
                                                            character_class,
                                                            skills,
                                                            level,
                                                            stats,
                                                            max_health,
                                                            max_mana,
                                                            secondary_class,
                                                        )
                                                        print("They offer you a job to help them hunt down other dangerous creatures like vampires and werewolves. Do you want to join the vampire hunters? (yes/no/status)")
                                                        while True:
                                                            join_hunters_choice = input().lower().strip()
                                                            if join_hunters_choice == "status":
                                                                check_status(stats, max_health, max_mana, skills, inventory)
                                                                print("Do you want to join the vampire hunters? (yes/no/status)")
                                                            elif join_hunters_choice in ["yes", "no"]:
                                                                break
                                                            else:
                                                                print("Please enter yes, no, or status.")
                                                        if join_hunters_choice == "yes":
                                                            print("You join the vampire hunters and become a powerful hunter of supernatural creatures! You gain 20 experience points plus the skill divine smite for joining the vampire hunters!")
                                                            experience_points += 20
                                                            skills.append("Divine Smite")
                                                            experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                                experience_points,
                                                                skill_points,
                                                                character_class,
                                                                skills,
                                                                level,
                                                                stats,
                                                                max_health,
                                                                max_mana,
                                                                secondary_class,
                                                            )
                                                            
                                                            print("You and the and the vampire hunters hear rumors of a powerful vampire lord terrorizing a nearby village and you decide to head there to investigate. When you arrive you find out that the rumors are true and the vampire lord is indeed terrorizing the village! Do you want to help the villagers fight the vampire lord? (yes/no/status)")
                                                            while True:
                                                                help_villagers_choice = input().lower().strip()
                                                                if help_villagers_choice == "status":
                                                                    check_status(stats, max_health, max_mana, skills, inventory)
                                                                    print("Do you want to help the villagers fight the vampire lord? (yes/no/status)")
                                                                elif help_villagers_choice in ["yes", "no"]:
                                                                    break
                                                                else:
                                                                    print("Please enter yes, no, or status.")
                                                            if help_villagers_choice == "yes":
                                                                print("You help the villagers fight the vampire lord and after a tough battle you defeat the vampire lord and save the village! You gain 50 experience points for defeating the vampire lord!")
                                                                experience_points += 50
                                                                experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                                    experience_points,
                                                                    skill_points,
                                                                    character_class,
                                                                    skills,
                                                                    level,
                                                                    stats,
                                                                    max_health,
                                                                    max_mana,
                                                                    secondary_class,
                                                                )
                                                                print("This is the end of the game, You Got the hunter ending congratulations!")
                                                                return
                                                            if help_villagers_choice == "no":
                                                                print("You run away like a coward and the vampire lord continues to terrorize the village. The vampire hunters are disappointed in you for not helping the villagers and they kick you out of their group. You continue on your adventure through the forest wondering if you made the right choice or not...")
                                                                print("This is the end of the game, You Got the coward ending congratulations!")
                                                                return
                                                        elif join_hunters_choice == "no":
                                                            print("You continue alone through the forest wondering not knowing where to go but you see a village in the distance and you decide to head towards it...")
                                                            print("You arrive at the village and find out that they are being terrorized by a powerful vampire lord! Do you want to help the villagers fight the vampire lord? (yes/no/status)")
                                                            while True:
                                                                help_villagers_choice = input().lower().strip()
                                                                if help_villagers_choice == "status":
                                                                    check_status(stats, max_health, max_mana, skills, inventory)
                                                                    print("Do you want to help the villagers fight the vampire lord? (yes/no/status)")
                                                                elif help_villagers_choice in ["yes", "no"]:
                                                                    break
                                                                else:
                                                                    print("Please enter yes, no, or status.")
                                                            if help_villagers_choice == "yes":
                                                                print("You help the villagers fight the vampire lord and after a tough battle you defeat the vampire lord and save the village! You gain 50 experience points for defeating the vampire lord!")
                                                                experience_points += 50
                                                                experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                                    experience_points,
                                                                    skill_points,
                                                                    character_class,
                                                                    skills,
                                                                    level,
                                                                    stats,
                                                                    max_health,
                                                                    max_mana,
                                                                    secondary_class,
                                                                )
                                                                print("This is the end of the game, You Got the lone hero ending congratulations!")
                                                                return
                                                            if help_villagers_choice == "no":
                                                                print("You decide not to help the villagers fight the vampire lord. The vampire lord continues to terrorize the village and you continue on your adventure through the forest, wondering if you made the right choice or not...")
                                                                print("This is the end of the game, You Got the lone wanderer ending congratulations!")
                                                                return
                                                            
                                                    if stone_mask_choice == "no":
                                                        print("You decide not to give the stone mask to the vampire hunters.")
                                                        print("They all attack you at once for not giving up the stone mask you are killed in the fight!")
                                                        return    
                                        
                                elif cave_choice == "no":
                                    print("You decide not to explore the hidden cave.")
                                    print("You continue walking throught the forest and come across a vampire and you walked right into it! Do you want to fight the vampire or bargin for mercy? (fight/bargin/status)")
                                    while True: 
                                        fight_choice = input().lower().strip()
                                        if fight_choice == "status":
                                            check_status(stats, max_health, max_mana, skills, inventory)
                                            print("Do you want to fight the vampire or bargin for mercy? (fight/bargin/status)")
                                        elif fight_choice in ["fight", "bargin"]:
                                            break
                                        else:
                                            print("Please enter fight, bargin, or status.")
                                    if fight_choice == "fight":
                                        print("You decide to fight the vampire!")
                                        print("The vampire overpowers you and you are killed in the fight!")
                                        return
                                    if fight_choice == "bargin":
                                        print("You decide to bargin for mercy with the vampire.")
                                        print("The vampire is impressed by your bravery and offers to make you a vampire like him! Do you want to become a vampire? (yes/no/status)")
                                        while True:
                                            vampire_choice = input().lower().strip()
                                            if vampire_choice == "status":
                                                check_status(stats, max_health, max_mana, skills, inventory)
                                                print("Do you want to become a vampire? (yes/no/status)")
                                            elif vampire_choice in ["yes", "no"]:
                                                break
                                            else:
                                                print("Please enter yes, no, or status.")
                                        if vampire_choice == "yes":
                                            print("You decide to become a vampire and the vampire bites you and turns you into a powerful vampire! You gain 50 experience points for becoming a vampire!")
                                            experience_points += 50
                                            experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                experience_points,
                                                skill_points,
                                                character_class,
                                                skills,
                                                level,
                                                stats,
                                                max_health,
                                                max_mana,
                                                secondary_class,
                                            )
                                            print("You continue your adventure through the forest as a powerful vampire!")
                                            print("You come across a group of villagers who are terrified of you and beg you to leave them alone. Do you want to attack the villagers or let them be? (attack/let be/status)")
                                            while True:
                                                villagers_choice = input().lower().strip()
                                                if villagers_choice == "status":
                                                    check_status(stats, max_health, max_mana, skills, inventory)
                                                    print("Do you want to attack the villagers or let them be? (attack/let be/status)")
                                                elif villagers_choice in ["attack", "let be"]:
                                                    break
                                                else:
                                                    print("Please enter attack, let be, or status.")
                                            if villagers_choice == "attack":
                                                print("You are spotted by a group of vampire hunters while attacking the village and you are killed!")
                                                return
                                            elif villagers_choice == "let be":
                                                print("You decide to let the villagers be, showing mercy and restraint. The villagers are grateful and spread word of your kindness, improving your reputation in nearby towns and villages!")
                                                print("You continue your adventure through the forest as a powerful vampire, and the nearby towns and villages are now more friendly towards you due to your mercy towards the villagers.")
                                                print("This is the end of the game, You Got the merciful vampire ending congratulations!")
                                                return
                                        elif vampire_choice == "no":
                                            print("You decide not to become a vampire and the vampire is offended by your decision and kills you!")
                        
                                            return
                        elif bard_choice == "no":
                            print("You decide not listen to the bard's music this makes the bard mad and he hits you with his lute you take 10 damage because you didn't expect it")
                            stats["Health"] -= 10
                            if stats["Health"] <= 0:
                                print("You have been killed by the bard's lute attack!")
                                return

                            print("You continue wandering through the forest and come across a man in top hat who asks you if you want to learn how to fight vampires. Do you want to learn how to fight vampires from the man? (yes/no/status)")
                            while True:
                                fight_vampires_choice = input().lower().strip()
                                if fight_vampires_choice == "status":
                                    check_status(stats, max_health, max_mana, skills, inventory)
                                    print("Do you want to learn how to fight vampires from the man? (yes/no/status)")
                                elif fight_vampires_choice in ["yes", "no"]:
                                    break
                                else:
                                    print("Please enter yes, no, or status.")
                            if fight_vampires_choice == "yes":
                                print("You decide to learn how to fight vampires from the man in the top hat. You gain a new skill called Sunlight Blast and you gain 20 experience points!")
                                skills.append("Sunlight Blast")
                                experience_points += 20
                                experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                    experience_points,
                                    skill_points,
                                    character_class,
                                    skills,
                                    level,
                                    stats,
                                    max_health,
                                    max_mana,
                                    secondary_class,
                                )
                                print("You start wandering around the forest and you come across a house it looks abandoned do you wish to explore inside? (yes/no /status)")
                                while True:
                                    explore_house_choice = input().lower().strip()
                                    if explore_house_choice == "status":
                                        check_status(stats, max_health, max_mana, skills, inventory)
                                        print("Do you wish to explore inside? (yes/no/status)")
                                    elif explore_house_choice in ["yes", "no"]:
                                        break
                                    else:
                                        print("Please enter yes, no, or status.")
                                if explore_house_choice == "yes":
                                    print("You decide to explore the house and you find a old grimoire that contains a werid spell in it. Do you wish to read the grimoire? (yes/no/status)")
                                    while True:
                                        read_grimoire_choice = input().lower().strip()
                                        if read_grimoire_choice == "status":
                                            check_status(stats, max_health, max_mana, skills, inventory)
                                            print("Do you wish to read the grimoire? (yes/no/status)")
                                        elif read_grimoire_choice in ["yes", "no"]:
                                            break
                                        else:
                                            print("Please enter yes, no, or status.")
                                    if read_grimoire_choice == "yes":
                                        print("You gain a new spell called Field of Flowers and you gain 20 experience points for reading the grimoire!")
                                        skills.append("Field of Flowers")
                                        experience_points += 20
                                        experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                            experience_points,
                                            skill_points,
                                            character_class,
                                            skills,
                                            level,
                                            stats,
                                            max_health,
                                            max_mana,
                                            secondary_class,
                                        )
                                        print("You continue exploring the house and you find set of armor that is walking around own it's own! Do you wish to fight it! (yes/no/status)")
                                        while True:
                                            fight_armor_choice = input().lower().strip()
                                            if fight_armor_choice == "status":
                                                check_status(stats, max_health, max_mana, skills, inventory)
                                                print("Do you wish to fight the living armor? (yes/no/status)")
                                            elif fight_armor_choice in ["yes", "no"]:
                                                break
                                            else:
                                                print("Please enter yes, no, or status.")
                                            if fight_armor_choice == "yes":
                                                print("You decide to fight the living armor.")
                                                if perform_fight("Living Armor", 30, 10, 50, character_class, stats, skills, experience_points, max_health, inventory):
                                                    return
                                                experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                    experience_points,
                                                    skill_points,
                                                    character_class,
                                                    skills,
                                                    level,
                                                    stats,
                                                    max_health,
                                                    max_mana,
                                                    secondary_class,
                                                )
                                                print("After defeating the living armor the chestplate of the armor fused to your chest and you gain 30 experience points for defeating the living armor you also gain the skill iron skin!")
                                                skills.append("Iron Skin")
                                                experience_points += 30
                                                experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                    experience_points,
                                                    skill_points,
                                                    character_class,
                                                    skills,
                                                    level,
                                                    stats,
                                                    max_health,
                                                    max_mana,
                                                    secondary_class,
                                                )
                                                print("You finsh exploring the house and you leave to continue your adventure through the forest and you come across a vampire and you walked right into it! Do you want to fight the vampire or bargin for mercy? (fight/bargin/status)")
                                                while True:
                                                    fight_choice = input().lower().strip()
                                                    if fight_choice == "status":
                                                        check_status(stats, max_health, max_mana, skills, inventory)
                                                        print("Do you want to fight the vampire or bargin for mercy? (fight/bargin/status)")
                                                    elif fight_choice in ["fight", "bargin"]:
                                                        break
                                                    else:
                                                        print("Please enter fight, bargin, or status.")
                                                if fight_choice == "fight":
                                                    print("You decide to fight the vampire!")
                                                    if perform_fight("vampire", 40, 20, 60, character_class, stats, skills, experience_points, max_health, inventory):
                                                        return
                                                    experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                                                        experience_points,
                                                        skill_points,
                                                        character_class,
                                                        skills,
                                                        level,
                                                        stats,
                                                        max_health,
                                                        max_mana,
                                                        secondary_class,
                                                    )
                                                    


                            if fight_vampires_choice == "no":
                                print("You decide not to learn how to fight vampires from the man with the top hat")


                elif chest_choice == "no":
                    print("You decide not to open the treasure chest.")

            elif fight_choice == "no":
                print("You avoid the goblin.")

                print("You continue walking through the forest and find a treasure chest! Do you want to open it? (yes/no/status)")
                while True:
                    chest_choice = input().lower().strip()
                    if chest_choice == "status":
                        check_status(stats, max_health, max_mana, skills, inventory)
                        print("Do you want to open the treasure chest? (yes/no/status)")
                    elif chest_choice in ["yes", "no"]:
                        break
                    else:
                        print("Please enter yes, no, or status.")
                if chest_choice == "yes":
                    print("You open the treasure chest and find some gold!")
                    inventory.append("Gold")
                    experience_points += 20
                    print("You gain 20 experience points for finding the treasure!")
                    experience_points, skill_points, level, skills, stats, max_health, max_mana, secondary_class = level_up(
                        experience_points,
                        skill_points,
                        character_class,
                        skills,
                        level,
                        stats,
                        max_health,
                        max_mana,
                        secondary_class,
                    )

                    
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
