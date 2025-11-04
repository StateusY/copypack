execute if score @s copypack.hard_cheese.hit_timer matches 60 run scoreboard players set @s copypack.hard_cheese.hit_count 0
execute if score @s copypack.hard_cheese.hit_timer matches 60 run return run scoreboard players set @s copypack.hard_cheese.hit_timer 0
execute if score @s copypack.hard_cheese.hit_count matches 1..9 run return run scoreboard players add @s copypack.hard_cheese.hit_timer 1

function copypack:blocks/hard_cheese/break/break