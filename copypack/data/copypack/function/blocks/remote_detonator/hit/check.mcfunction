execute if score $hit_remote_detonator_check copypack.remote_detonator.dummy matches 1 run return fail

execute on attacker if entity @s[tag=copypack.hit_remote_detonator] run scoreboard players set $hit_remote_detonator_check copypack.remote_detonator.dummy 1
execute if score $hit_remote_detonator_check copypack.remote_detonator.dummy matches 1 run data remove entity @s attack
execute if score $hit_remote_detonator_check copypack.remote_detonator.dummy matches 1 on vehicle run scoreboard players add @s copypack.remote_detonator.hit_count 1
execute if score $hit_remote_detonator_check copypack.remote_detonator.dummy matches 1 on vehicle at @s run playsound minecraft:block.stone.hit block @a ~ ~ ~ 1 2
execute if score $hit_remote_detonator_check copypack.remote_detonator.dummy matches 1 on vehicle at @s run particle minecraft:item{item:{id:"minecraft:sandstone"}} ~ ~-0.25 ~ 0.3 0.1 0.3 0.1 5