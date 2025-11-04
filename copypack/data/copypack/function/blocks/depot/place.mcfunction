# remove setup item frame
kill @s

# play place block sound
playsound minecraft:block.candle.place block @a ~ ~ ~ 1 2

# spawn the block's item display
execute unless block ~ ~ ~ #minecraft:air run return run loot spawn ~ ~ ~ loot copypack:blocks/depot
execute align xyz positioned ~0.5 ~0.5 ~0.5 as @n[tag=smithed.block,distance=..0.1] at @s run return run loot spawn ~ ~ ~ loot copypack:blocks/depot

setblock ~ ~ ~ minecraft:barrier

# rotate to player orientation
data modify storage copypack:temp rotation set value 0
execute store result score $player_rotation copypack.depot.dummy run data get entity @p[advancements={copypack:blocks/item_frame=true}] Rotation[0]
execute if score $player_rotation copypack.depot.dummy matches 135..180 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage copypack:temp rotation set value 90
execute if score $player_rotation copypack.depot.dummy matches -180..-135 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage copypack:temp rotation set value 90
execute if score $player_rotation copypack.depot.dummy matches -135..-45 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage copypack:temp rotation set value 180
execute if score $player_rotation copypack.depot.dummy matches -45..45 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage copypack:temp rotation set value -90
execute if score $player_rotation copypack.depot.dummy matches 45..135 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage copypack:temp rotation set value 0

# run data to macro
function copypack:blocks/depot/macro with storage copypack:temp
scoreboard players set @n[type=minecraft:item_display,tag=copypack.depot] copypack.depot.hit_count 0
scoreboard players set @n[type=minecraft:item_display,tag=copypack.depot] copypack.depot.hit_timer 0