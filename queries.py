from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
# How many total Characters are there?
    characters = Character.objects.all()
    print(len(characters)) #302

# How many of each specific subclass?
    fighter = Fighter.objects.all()
    mage = Mage.objects.all()
    cleric = Cleric.objects.all()
    thief = Thief.objects.all()
    necromancer = Necromancer.objects.all()
    print(len(fighter)) #68
    print(len(mage)) #108
    print(len(cleric)) #75
    print(len(thief)) #51
    print(len(necromancer)) #11
# How many total Items?
    from armory.models import Item
    items = Item.objects.all()
    print(len(items)) #174    
# How many of the Items are weapons? How many are not?
    from armory.models import Weapon
    weapons = Weapon.objects.all()
    print(len(weapons)) #37, #137
# On average, how many Items does each Character have?
    print(len(items) / len(character)) #0.57
# On average, how many Weapons does each character have?
    print(len(weapons) / len(character)) #0.122