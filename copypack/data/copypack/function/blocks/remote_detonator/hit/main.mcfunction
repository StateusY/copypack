scoreboard players set $hit_remote_detonator_check copypack.remote_detonator.dummy 0

tag @s add copypack.hit_remote_detonator
execute as @e[type=minecraft:interaction,tag=copypack.remote_detonator_interaction_base,distance=..20,sort=nearest] run function copypack:blocks/remote_detonator/hit/check
tag @s remove copypack.hit_remote_detonator