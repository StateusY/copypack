execute if score @s copypack.remote_detonator.hit_timer matches 60 run scoreboard players set @s copypack.remote_detonator.hit_count 0
execute if score @s copypack.remote_detonator.hit_timer matches 60 run return run scoreboard players set @s copypack.remote_detonator.hit_timer 0
execute if score @s copypack.remote_detonator.hit_count matches 1..2 run return run scoreboard players add @s copypack.remote_detonator.hit_timer 1

function copypack:blocks/remote_detonator/break/break