import package_manager

import classes as cl
import combat as co

tripleSlash = cl.move(name="Triple Slash", power=140, pp=5, type="fighting", cat="physical")

forcePalm = cl.move(name="Force Palm", power=60, pp=10, type="fighting", cat="physical")

icePunch = cl.move(name="Ice Punch", power=75, pp=15, type="ice", cat="physical")

boneRush = cl.move(name="Bone Rush", power=25, pp=10, type=cl.pokemon_type.GROUND, cat=cl.category.PHYSICAL)

lucario = cl.pokemon(name="Lucario", moveset=[tripleSlash, forcePalm, icePunch, boneRush], lvl=44, hp=118, atk=129, defe=71, spatk=120, spdef=67, spd=80)

lucario2 = cl.pokemon(name="Lucario 2", moveset=[tripleSlash, forcePalm, icePunch, boneRush], lvl=44, hp=118, atk=129, defe=71, spatk=120, spdef=67, spd=85)

co.fight(lucario, lucario2)