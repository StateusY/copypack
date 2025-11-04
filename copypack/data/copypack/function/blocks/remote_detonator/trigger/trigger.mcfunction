say BOOOOOOOOOOOOOOOOOM!

# delete the thrown eye
execute at @p[tag=copypack.remote_detonator.thrown_eye] run kill @n[type=eye_of_ender]
# remove thrown_eye tag
execute as @p[tag=copypack.remote_detonator.thrown_eye] run tag @s remove copypack.remote_detonator.thrown_eye

# change blockstate
data modify entity @s item set value {id:"minecraft:barrier",count:1,components:{"minecraft:item_model":"copypack:blocks/remote_detonator/remote_detonator_triggered_block"}}
tag @s add copypack.remote_detonator.filled

# redstone pulse
execute at @s run setblock ~ ~ ~ redstone_block
tag @s add copypack.remote_detonator.pulse_triggerer
schedule function copypack:blocks/remote_detonator/trigger/remove_pulse 1t

# explode tnt
tag @s add copypack.remote_detonator.tnt_explode
schedule function copypack:blocks/remote_detonator/trigger/explode_tnt 1t