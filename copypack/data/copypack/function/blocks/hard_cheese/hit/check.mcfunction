execute if score $hit_hard_cheese_check copypack.hard_cheese.dummy matches 1 run return fail

execute on attacker if entity @s[tag=copypack.hit_hard_cheese] run scoreboard players set $hit_hard_cheese_check copypack.hard_cheese.dummy 1
execute if score $hit_hard_cheese_check copypack.hard_cheese.dummy matches 1 run data remove entity @s attack
execute if score $hit_hard_cheese_check copypack.hard_cheese.dummy matches 1 on vehicle run scoreboard players add @s copypack.hard_cheese.hit_count 1
execute if score $hit_hard_cheese_check copypack.hard_cheese.dummy matches 1 on vehicle at @s run playsound block.candle.hit block @a ~ ~ ~ 1 2
execute if score $hit_hard_cheese_check copypack.hard_cheese.dummy matches 1 on vehicle at @s run particle minecraft:item{item:{id:"minecraft:yellow_concrete"}} ~ ~-0.25 ~ 0.3 0.1 0.3 0.1 5