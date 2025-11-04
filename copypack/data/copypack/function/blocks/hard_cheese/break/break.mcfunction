execute on passengers run kill @s
execute as @e[type=interaction,distance=..0.65,tag=copypack.hard_cheese_interaction] run kill @s
kill @s

setblock ~ ~ ~ minecraft:air replace
playsound block.candle.hit block @a ~ ~ ~ 1 2
particle minecraft:item{item:{id:"minecraft:yellow_concrete"}} ~ ~-0.25 ~ 0.3 0.1 0.3 0.1 20

loot spawn ~ ~ ~ loot copypack:blocks/hard_cheese