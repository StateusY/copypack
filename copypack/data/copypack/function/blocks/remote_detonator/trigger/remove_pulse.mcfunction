# reset power pulse
execute as @n[type=item_display,tag=copypack.remote_detonator.pulse_triggerer] at @s run setblock ~ ~ ~ barrier

execute as @n[type=item_display,tag=copypack.remote_detonator.pulse_triggerer] run tag @s add copypack.remote_detonator.pulse_triggerer