tp @s ^ ^ ^0.5

#test
#particle flame ~ ~ ~ 0 0 0 0 1 force

execute if entity @e[tag=copypack.remote_detonator,tag=!copypack.remote_detonator.filled, distance=..1.5] run tag @s add copypack.raycast.hitEntity

#execute unless block ~ ~ ~ #copypack:ray_permeable run tag @s add copypack.raycast.hitBlock

scoreboard players remove @s copypack.raycast.steps 1

execute as @s[tag=!copypack.raycast.hitEntity,tag=!copypack.raycast.hitBlock,scores={copypack.raycast.steps=1..}] at @s run function copypack:ray/move