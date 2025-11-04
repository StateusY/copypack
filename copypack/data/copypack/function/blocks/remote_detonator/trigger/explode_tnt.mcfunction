# detonate neighboring tnt instantly
execute at @n[type=item_display,tag=copypack.remote_detonator.tnt_explode] as @e[type=minecraft:tnt,distance=..10] run data merge entity @s {fuse:0s}

# pretend the block got destroyed
execute as @n[type=item_display,tag=copypack.remote_detonator.tnt_explode] run function copypack:blocks/remote_detonator/break/break
execute as @n[type=item_display,tag=copypack.remote_detonator.tnt_explode] run tag @s add copypack.remote_detonator.tnt_explode