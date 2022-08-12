import package_manager

import classes as cl
import combat as co

tripleSlash = cl.move("Triple Slash", 140, 5, cl.pokemon_type.FIGHTING, cl.category.PHYSICAL)

forcePalm = cl.move("Force Palm", 60, 10, cl.pokemon_type.FIGHTING, cl.category.PHYSICAL)

icePunch = cl.move("Ice Punch", 75, 15, cl.pokemon_type.ICE, cl.category.PHYSICAL)

boneRush = cl.move("Bone Rush", 25, 10, cl.pokemon_type.GROUND, cl.category.PHYSICAL)

lucario = cl.pokemon("Lucario", [tripleSlash, forcePalm, icePunch, boneRush], 44, 118, 129, 71, 120, 67, 80)

lucario2 = cl.pokemon("Lucario 2", [tripleSlash, forcePalm, icePunch, boneRush], 44, 118, 129, 71, 120, 67, 85)

co.fight(lucario, lucario2, cl.environment.GRASS)