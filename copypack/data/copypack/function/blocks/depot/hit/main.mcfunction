scoreboard players set $hit_depot_check copypack.depot.dummy 0

tag @s add copypack.hit_depot
execute as @e[type=minecraft:interaction,tag=copypack.depot_interaction_base,distance=..20,sort=nearest] run function copypack:blocks/depot/hit/check
tag @s remove copypack.hit_depot