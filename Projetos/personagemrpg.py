full_dot = '●'
empty_dot = '○'

def create_character(name, power, smart, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    if not isinstance(power, int) or not isinstance(smart, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    if power < 1 or smart < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if power > 4 or smart > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if power + smart + charisma != 7:
        return "The character should start with 7 points"

    return (
        f"{name}\n"
        f"STR {full_dot * power + empty_dot * (10 - power)}\n"
        f"INT {full_dot * smart + empty_dot * (10 - smart)}\n"
        f"CHA {full_dot * charisma + empty_dot * (10 - charisma)}"

    )

print(create_character("ren", 4, 2, 1))