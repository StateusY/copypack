summon marker ~ ~ ~ {Tags:[copypack.raycast.isRay]}

execute anchored eyes rotated as @s run tp @e[tag=copypack.raycast.isRay,limit=1,sort=nearest] ^ ^ ^ ~ ~

execute as @e[tag=copypack.raycast.isRay,limit=1,sort=nearest] run function copypack:ray/process