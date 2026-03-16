def level_up():
    
      if character_class == "Warrior" or character_class == "Mage" or character_class == "Rogue":
                    print("You gain 10 experience points for defeating the goblin!")
                    experience_points += 10
                    if experience_points >= 10:
                        print("Congratulations! You've leveled up!")
                        skill_points += 2
                        print(f"You have {skill_points} skill points to spend.")
                        if character_class == "Warrior":
                            print("Choose a skill lightning strike, sheild bash, flame slash, or whirlwind attack: ")    
                            skill_choice = input().lower()
                            if skill_choice == "lightning strike":
                                print("You have learned Lightning Strike! This skill allows you to strike your enemy with a powerful lightning attack.")
                                skills.append("Lightning Strike")
                            elif skill_choice == "shield bash":
                                print("You have learned Shield Bash! This skill allows you to bash your enemy with your shield, stunning them for a short time.")
                                skills.append("Shield Bash")
                            elif skill_choice == "flame slash":
                                print("You have learned Flame Slash! This skill allows you to slash your enemy with a fiery attack, dealing extra damage.")
                                skills.append("Flame Slash")
                            elif skill_choice == "whirlwind attack":
                                print("You have learned Whirlwind Attack! This skill allows you to spin around and attack all nearby enemies with your weapon.")
                                skills.append("Whirlwind Attack")
                            else:
                                print("Invalid skill choice. Please choose a valid skill.")
                        elif character_class == "Mage":
                            print("Choose a skill arcane blast, frost nova, chain lightning, or meteor strike: ")    
                            skill_choice = input().lower()
                            if skill_choice == "arcane blast":
                                print("You have learned Arcane Blast! This skill allows you to blast your enemy with arcane energy, dealing damage and silencing them for a short time.")
                                skills.append("Arcane Blast")
                            elif skill_choice == "frost nova":
                                print("You have learned Frost Nova! This skill allows you to freeze your enemies in place, dealing damage and slowing them for a short time.")
                                skills.append("Frost Nova")
                            elif skill_choice == "chain lightning":
                                print("You have learned Chain Lightning! This skill allows you to strike multiple enemies with a powerful lightning attack, dealing damage to each enemy hit.")
                                skills.append("Chain Lightning")
                            elif skill_choice == "meteor strike":
                                print("You have learned Meteor Strike! This skill allows you to call down a meteor from the sky, dealing massive damage to all enemies in the area.")
                                skills.append("Meteor Strike")
                            else:
                                print("Invalid skill choice. Please choose a valid skill.")
                        elif character_class == "Rogue":
                            print("Choose a skill shadow step, poison blade, evasion, or smoke screen: ")    
                            skill_choice = input().lower()
                            if skill_choice == "shadow step":
                                print("You have learned Shadow Step! This skill allows you to teleport behind your enemy, dealing damage and stunning them for a short time.")
                                skills.append("Shadow Step")
                            elif skill_choice == "poison blade":
                                print("You have learned Poison Blade! This skill allows you to coat your weapon with poison, dealing damage over time to your enemy.")
                                skills.append("Poison Blade")
                            elif skill_choice == "evasion":
                                print("You have learned Evasion! This skill allows you to dodge incoming attacks, increasing your chance to avoid damage for a short time.")
                                skills.append("Evasion")
                            elif skill_choice == "smoke screen":
                                print("You have learned Smoke Screen! This skill allows you to create a cloud of smoke, reducing the accuracy of your enemies and allowing you to escape or reposition.")
                                skills.append("Smoke Screen")
                            else:
                                print("Invalid skill choice. Please choose a valid skill.")
