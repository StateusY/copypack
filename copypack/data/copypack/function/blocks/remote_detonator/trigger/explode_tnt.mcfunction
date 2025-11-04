# detonate neighboring tnt instantly
execute at @n[type=item_display,tag=copypack.remote_detonator.tnt_explode] as @e[type=minecraft:tnt,distance=..10] run data merge entity @s {fuse:0s}

# pretend the block got destroyed
execute as @n[type=item_display,tag=copypack.remote_detonator.tnt_explode] at @s if entity @e[type=minecraft:tnt,distance=..10] run setblock ~ ~ ~ minecraft:air replace
execute as @n[type=item_display,tag=copypack.remote_detonator.tnt_explode] at @s if entity @e[type=minecraft:tnt,distance=..10] run function copypack:blocks/remote_detonator/break/break
execute as @n[type=item_display,tag=copypack.remote_detonator.tnt_explode] at @s if entity @e[type=minecraft:tnt,distance=..10] run tag @s remove copypack.remote_detonator.tnt_explode