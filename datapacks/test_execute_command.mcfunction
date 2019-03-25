#these function will give you grass if two blocks under you is stone else stone (in order to replace it)

execute if block ~ ~-2 ~ minecraft:stone run give @s grass
execute unless block ~ ~-2 ~ minecraft:stone run give @s stone