scoreboard players set $hit_hard_cheese_check copypack.hard_cheese.dummy 0

tag @s add copypack.hit_hard_cheese
execute as @e[type=minecraft:interaction,tag=copypack.hard_cheese_interaction_base,distance=..20,sort=nearest] run function copypack:blocks/hard_cheese/hit/check
tag @s remove copypack.hit_hard_cheese