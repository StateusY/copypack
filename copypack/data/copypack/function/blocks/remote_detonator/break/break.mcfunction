execute on passengers run kill @s
execute as @e[type=interaction,distance=..0.65,tag=copypack.remote_detonator_interaction] run kill @s
kill @s

setblock ~ ~ ~ minecraft:air replace
playsound minecraft:block.stone.break block @a ~ ~ ~ 1 2
particle minecraft:block{block_state:{Name:"minecraft:sandstone"}} ~ ~-0.25 ~ 0.3 0.1 0.3 0.1 20

loot spawn ~ ~ ~ loot copypack:blocks/remote_detonator
execute if entity @s[tag=copypack.remote_detonator.filled] run loot spawn ~ ~ ~ loot copypack:blocks/eye_of_ender