scoreboard players set @s copypack.raycast.steps 64

execute at @s run function copypack:ray/move

execute as @s[tag=copypack.raycast.hitEntity] at @s run function copypack:ray/hit

kill @s