execute if score $hit_depot_check copypack.depot.dummy matches 1 run return fail

execute on attacker if entity @s[tag=copypack.hit_depot] run scoreboard players set $hit_depot_check copypack.depot.dummy 1
execute if score $hit_depot_check copypack.depot.dummy matches 1 run data remove entity @s attack
execute if score $hit_depot_check copypack.depot.dummy matches 1 on vehicle run scoreboard players add @s copypack.depot.hit_count 1
execute if score $hit_depot_check copypack.depot.dummy matches 1 on vehicle at @s run playsound block.candle.hit block @a ~ ~ ~ 1 2
execute if score $hit_depot_check copypack.depot.dummy matches 1 on vehicle at @s run particle minecraft:item{item:{id:"minecraft:yellow_concrete"}} ~ ~-0.25 ~ 0.3 0.1 0.3 0.1 5