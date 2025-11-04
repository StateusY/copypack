import json
import shutil
from pathlib import Path

# === CONFIG ===

### Steps:
# 1. Open up the script and find the CONFIG section near the top. (Right here!)
# 2. Change the default_namespace to your desired namespace.
# 3. Duplicate the example sandstone_table to get the desired quantity of blocks (one entry ber block).
# 4. Edit each block entry to your choosing.
#     - Name: this is the display name
#     - ID: this is what the block will be refered to in the datapack. Keep it all lowercase and no spaces or funky characters.
#     - Interact: toggle this to true for the block to be interactable.
#     - Interaction Function: set this to a function you want to trigger when the block is interacted with.
#     - Can Float: set this to true if you want your block to not be able to float.
#     - Hit Count: set this to the number of hits your block can take before it breaks.
#     - Place Block Sound: set this to a sound you want to play when the block is placed.
#     - Hit Block Sound: set this to a sound you want to play when the block is hit.
#     - Hit Block Particle: set this to a particle you want to display when the block is broken.
#     - Break Block Sound: set this to a sound you want to play when the block is hit.
#     - Break Block Particle: set this to a particle you want to display when the block is broken.
#     - Has Recipe: set this to true if you want your block to be craftable.
#     - Recipe Output Quantity: set this to the number of blocks created by the recipe
#     - Recipe Key: give each ingredient in your recipe a symbol or letter to act as a key.
#     - Recipe Pattern: arrange the keys in a pattern to mimic a crafting recipe - spaces are empty slots.
# 5. Now GENERATE! If you input everything above correctly it should work - use the example (sandstone_table) to work off of.
# 6. The final step is to insert your textures and block models into the datapack
#     - Upload the block's textures to NAMESPACE/assets/NAMESPACE/textures/blocks/BLOCKNAME"
#     - If the block has a seperate item textue, upload the block's item texture to NAMESPACE/assets/NAMESPACE/textures/items/BLOCKNAME"
#     - Upload the block's model to NAMESPACE/assets/NAMESPACE/models/item/blocks/BLOCKNAME" - Note: only the block model needs uploading, the item model is pregenerated. Also, don't forget to link the textures in the model to the directories of the textures, use the sandstone_table as example. Also also, I reccomend to set the display settings to the 'block' preset in BlockBench if you don't have a seperate item texture.


NAMESPACE = "copypack" # change me

blocks = [
    {
        "name": "Remote Detonator",
        "id": "remote_detonator",
        "seperate_item_model": False,
        "consumable_component": None,
        "food_component": None,
        "interact": False,
        "interaction_function": None,
        "can_float": True,

        "hit_count": 3,
        
        "place_block_sound": "minecraft:block.stone.place block @a ~ ~ ~ 1 2",
        "hit_block_sound": "minecraft:block.stone.hit block @a ~ ~ ~ 1 2",
        "hit_block_particle": "minecraft:item{item:{id:\"minecraft:sandstone\"}} ~ ~-0.25 ~ 0.3 0.1 0.3 0.1 5",
        "break_block_sound": "minecraft:block.stone.break block @a ~ ~ ~ 1 2",
        "break_block_particle": "minecraft:item{item:{id:\"minecraft:sandstone\"}} ~ ~-0.25 ~ 0.3 0.1 0.3 0.1 20",

        "has_recipe": True,
        "recipe_output_quantity": 1,
        "recipe_key": {"#": "minecraft:iron_chain",
                       "X": "minecraft:sandstone",
                       "$": "minecraft:stripped_dark_oak_log"
                       },
        "recipe_pattern": [
            "XXX",
            "$X%",
            "$ $"
        ]
    },
    {
        "name": "Block of Hard Cheese",
        "id": "hard_cheese",
        "seperate_item_model": False,
        "consumable_component": {
                                    "consume_seconds": 3,
                                    "animation": "eat",
                                    "sound": "minecraft:entity.generic.eat",
                                    "has_consume_particles": True,
                                    "on_consume_effects": [
                                    {
                                        "type": "minecraft:apply_effects",
                                        "effects": [
                                        {
                                            "id": "minecraft:haste",
                                            "duration": 30,
                                            "ambient": False,
                                            "show_particles": False,
                                            "show_icon": False
                                        }
                                        ]
                                    }
                                    ]
                                },
        "food_component": {
                            "nutrition": 6,
                            "saturation": 6,
                            "can_always_eat": True
                        },
        "interact": False,
        "interaction_function": None,
        "can_float": True,

        "hit_count": 10,
        
        "place_block_sound": "minecraft:block.candle.place block @a ~ ~ ~ 1 2",
        "hit_block_sound": "block.candle.hit block @a ~ ~ ~ 1 2",
        "hit_block_particle": "minecraft:item{item:{id:\"minecraft:yellow_concrete\"}} ~ ~-0.25 ~ 0.3 0.1 0.3 0.1 5",
        "break_block_sound": "block.candle.hit block @a ~ ~ ~ 1 2",
        "break_block_particle": "minecraft:item{item:{id:\"minecraft:yellow_concrete\"}} ~ ~-0.25 ~ 0.3 0.1 0.3 0.1 20",

        "has_recipe": True,
        "recipe_output_quantity": 9,
        "recipe_key": {"#": "minecraft:milk_bucket"
                       },
        "recipe_pattern": [
            "###",
            "###",
            "###"
        ]
    }
]



# === TECHNICAL === 

# Base output folder relative to script location
LOG_FILE = Path(__file__).parent / "log.txt"

def log_debug(msg):
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "bb-output"
BLOCK_FUNCTION_DIR = OUTPUT_DIR / "data" / NAMESPACE / "function" / "blocks"

# === CLEAR OUTPUT FOLDER ===
def clear_output_dir():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# === MAIN ===
def main():
    if LOG_FILE.exists():
        LOG_FILE.unlink()
    clear_output_dir()  # clear folder first

    # mcmeta
    meta = create_mcmeta()
    save_generic_mcmeta("pack", OUTPUT_DIR, meta)

    # lang
    translation = create_lang_en(blocks)
    save_generic_json("en_us", OUTPUT_DIR / "assets" / NAMESPACE / "lang", translation)

    # tags
    tag = create_blocks_tag()
    save_generic_json("blocks", OUTPUT_DIR / "data" / NAMESPACE / "tags" / "block", tag)
    tag = create_minecraft_load_tag()
    save_generic_json("load", OUTPUT_DIR / "data" / "minecraft" / "tags" / "function", tag)
    tag = create_minecraft_tick_tag()
    save_generic_json("tick", OUTPUT_DIR / "data" / "minecraft" / "tags" / "function", tag)

    # item_frame detection
    adv = item_frame_adv_entry()
    save_generic_json("item_frame", OUTPUT_DIR / "data" / NAMESPACE / "advancement" / "blocks", adv)
    create_item_frame_functions(blocks)

    # global functions
    function = create_load_master_entry(blocks)
    save_generic_mcfunction("load", OUTPUT_DIR / "data" / NAMESPACE / "function", function)
    function = create_tick_master_entry(blocks)
    save_generic_mcfunction("tick", OUTPUT_DIR / "data" / NAMESPACE / "function", function)
    function = create_tick_2_master_entry()
    save_generic_mcfunction("tick_2", OUTPUT_DIR / "data" / NAMESPACE / "function", function)
    function = create_blocks_master_entry(blocks)
    save_generic_mcfunction("blocks", BLOCK_FUNCTION_DIR, function)

    for block in blocks:
        # loot table
        loot = create_loot_entry(block)
        save_generic_json(block['id'], OUTPUT_DIR / "data" / NAMESPACE / "loot_table" / "blocks", loot)

        # recipe
        if block['has_recipe']:
            recipe = create_recipe_entry(block)
            save_generic_json(block['id'], OUTPUT_DIR / "data" / NAMESPACE / "recipe" / "blocks", recipe)

        # advancements
        adv = create_adv_hit_block(block)
        save_generic_json(f"hit_{block['id']}", OUTPUT_DIR / "data" / NAMESPACE / "advancement" / "blocks" / block['id'], adv)
        if block['interact']:
            adv = create_adv_interact_block(block)
            save_generic_json(f"interact_{block['id']}", OUTPUT_DIR / "data" / NAMESPACE / "advancement" / "blocks" / block['id'], adv)
        
        # items, models, and textures
        item = create_item_item_entry(block)
        save_generic_json(f"{block['id']}_item", OUTPUT_DIR / "assets" / NAMESPACE / "items" / "blocks" / block['id'], item)
        item = create_block_item_entry(block)
        save_generic_json(f"{block['id']}_block", OUTPUT_DIR / "assets" / NAMESPACE / "items" / "blocks" / block['id'], item)

        item = create_item_model_entry(block)
        save_generic_json(f"{block['id']}_item", OUTPUT_DIR / "assets" / NAMESPACE / "models" / "item" / "blocks" / block['id'], item)
        item = create_block_model_entry(block)
        save_generic_json(f"{block['id']}_block", OUTPUT_DIR / "assets" / NAMESPACE / "models" / "item" / "blocks" / block['id'], item)
        if block['seperate_item_model']: (OUTPUT_DIR / "assets" / NAMESPACE / "textures" / "item" / block['id']).mkdir(parents=True, exist_ok=True)
        (OUTPUT_DIR / "assets" / NAMESPACE / "textures" / "block" / block['id']).mkdir(parents=True, exist_ok=True)

        # functions
            # basic functions
        function = create_tick_entry(block)
        save_generic_mcfunction("tick", BLOCK_FUNCTION_DIR / block['id'], function)
        function = create_place_entry(block)
        save_generic_mcfunction("place", BLOCK_FUNCTION_DIR / block['id'], function)
        function = create_macro_entry(block)
        save_generic_mcfunction("macro", BLOCK_FUNCTION_DIR / block['id'], function)
        if block['interact']:
            function = create_interaction_entry(block)
            save_generic_mcfunction("block_interaction", BLOCK_FUNCTION_DIR / block['id'], function)

            # hit block functions
        function = create_hit_hit_entry(block)
        save_generic_mcfunction("hit", BLOCK_FUNCTION_DIR / block['id'] / "hit", function)
        function = create_hit_main_entry(block)
        save_generic_mcfunction("main", BLOCK_FUNCTION_DIR / block['id'] / "hit", function)
        function = create_hit_check_entry(block)
        save_generic_mcfunction("check", BLOCK_FUNCTION_DIR / block['id'] / "hit", function)

            # block break functions
        function = create_break_check_entry(block)
        save_generic_mcfunction("check", BLOCK_FUNCTION_DIR / block['id'] / "break", function)
        function = create_break_break_entry(block)
        save_generic_mcfunction("break", BLOCK_FUNCTION_DIR / block['id'] / "break", function)

    print("Blocks regenerated in the script folder!")
    print("------------")
    print("There are a few more steps:")
    print("     >Upload the block's textures to NAMESPACE/assets/NAMESPACE/textures/blocks/BLOCKNAME")
    print("     >Upload the block's item texture to NAMESPACE/assets/NAMESPACE/textures/items/BLOCKNAME")
    print("     >Upload the block's model to NAMESPACE/assets/NAMESPACE/models/item/blocks/BLOCKNAME")
    print("Once you have completed that for every generated block, you are done! Enjoy the custom blocks!")

# === FILE ENTRY CREATION ===
def create_loot_entry(block):
    item_name = "minecraft:item_frame"
    name_component = [
        # The translations are found in the translation file en_us.json
        {"translate": f"item.{NAMESPACE}.block.{block['id'].lower()}",
         "fallback": f"{block['name']}"},
    ]

    # Core components
    components = {
        "minecraft:item_name": {"translate": f"item.{NAMESPACE}.block.{block['id'].lower()}", "fallback": f"{block['name']}"},
        "minecraft:item_model": f"{NAMESPACE}:blocks/{block['id']}/{block['id']}_item",
        "minecraft:custom_data": {f"{NAMESPACE}":{f"{block['id']}":True},"smithed":{"ignore":{"functionality":True,"crafting":True}}},
        "minecraft:entity_data": {"id":"minecraft:item_frame","Tags":[f"{NAMESPACE}.{block['id']}_setup"],"Silent":True,"Invisible":True}
    }
    if block['consumable_component'] != None: components["minecraft:consumable"] = block['consumable_component']
    if block['food_component'] != None: components["minecraft:food"] = block['food_component']

    return {
        "pools": [{
            "rolls": 1,
            "entries": [{
                "type": "minecraft:item",
                "name": item_name,
                "functions": [
                    {"function": "minecraft:set_components", "components": components}
                ]
            }]
        }]
    }

def create_recipe_entry(block):
    item_name = "minecraft:item_frame"
    item_count = block['recipe_output_quantity']
    name_component = [
        # The translations are found in the translation file en_us.json
        {"translate": f"item.{NAMESPACE}.block.{block['id'].lower()}",
         "fallback": f"{block['name']}"},
    ]

    # Core components
    components = {
        "minecraft:item_name": {"translate": f"item.{NAMESPACE}.block.{block['id'].lower()}", "fallback": f"{block['name']}"},
        "minecraft:item_model": f"{NAMESPACE}:blocks/{block['id']}/{block['id']}_item",
        "minecraft:custom_data": {f"{NAMESPACE}":{f"{block['id']}":True},"smithed":{"ignore":{"functionality":True,"crafting":True}}},
        "minecraft:entity_data": {"id":"minecraft:item_frame","Tags":[f"{NAMESPACE}.{block['id']}_setup"],"Silent":True,"Invisible":True}
    }
    if block['consumable_component'] != None: components["minecraft:consumable"] = block['consumable_component']
    if block['food_component'] != None: components["minecraft:food"] = block['food_component']

    return {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "key": block['recipe_key'],
            "pattern": block['recipe_pattern'],
            "result": {
                "count": item_count,
                "id": item_name,
                "components": components
            }
        }

def item_frame_adv_entry():
    return {
        "criteria": {
            "requirement": {
            "trigger": "minecraft:item_used_on_block",
            "conditions": {
                "location": [
                {
                    "condition": "minecraft:match_tool",
                    "predicate": {
                    "items": "minecraft:item_frame"
                    }
                }
                ]
            }
            }
        },
        "rewards": {
            "function": f"{NAMESPACE}:item_frame/main"
        }
    }

def create_adv_hit_block(block):
    return {
        "criteria": {
            "requirement": {
            "trigger": "minecraft:player_hurt_entity",
            "conditions": {
                "entity": {
                "type": "minecraft:interaction",
                "nbt": f"{{Tags:[\"{NAMESPACE}.{block['id']}_interaction_base\"]}}"
                }
            }
            }
        },
        "rewards": {
            "function": f"{NAMESPACE}:blocks/{block['id']}/hit/hit"
        }
    }

def create_adv_interact_block(block):
    return {
            "criteria": {
                "requirement": {
                "trigger": "minecraft:player_interacted_with_entity",
                "conditions": {
                    "entity": {
                    "type": "minecraft:interaction",
                    "nbt": f"{{Tags:[\"{NAMESPACE}.{block['id']}_interaction_base\"]}}"
                    }
                }
                }
            },
            "rewards": {
                "function": f"{NAMESPACE}:blocks/{block['id']}/block_interaction"
            }
        }

def create_mcmeta():
    return {
            "pack": {
                "description": "This pack was made with Block-Builder-MC",
                "pack_format": 88
            }
        }

def create_lang_en(blocks):
    lang = {}

    for block in blocks:
        lang[f"block.{NAMESPACE}.{block['id']}"] = block['name']

    return lang

def create_blocks_tag():
    return {"replace":False,"values":[
            "#minecraft:air",
            "minecraft:lava",
            "minecraft:water",
            "#minecraft:saplings",
            "#minecraft:pressure_plates",
            "minecraft:redstone_wire",
            "minecraft:brown_mushroom",
            "minecraft:red_mushroom",
            "minecraft:crimson_fungus",
            "minecraft:warped_fungus",
            "minecraft:short_grass",
            "minecraft:fern",
            "minecraft:dead_bush",
            "minecraft:dandelion",
            "minecraft:poppy",
            "minecraft:blue_orchid",
            "minecraft:allium",
            "minecraft:azure_bluet",
            "minecraft:red_tulip",
            "minecraft:orange_tulip",
            "minecraft:white_tulip",
            "minecraft:pink_tulip",
            "minecraft:oxeye_daisy",
            "minecraft:cornflower",
            "minecraft:lily_of_the_valley",
            "minecraft:spore_blossom",
            "minecraft:sugar_cane",
            "minecraft:wither_rose",
            "minecraft:crimson_roots",
            "minecraft:warped_roots",
            "minecraft:nether_sprouts",
            "minecraft:weeping_vines",
            "minecraft:twisting_vines",
            "minecraft:vine",
            "minecraft:tall_grass",
            "minecraft:large_fern",
            "minecraft:sunflower",
            "minecraft:lilac",
            "minecraft:rose_bush",
            "minecraft:peony",
            "minecraft:glow_lichen",
            "minecraft:hanging_roots",
            "minecraft:frogspawn",
            "minecraft:seagrass",
            "minecraft:sculk_vein",
            "minecraft:cobweb",
            "minecraft:cave_vines",
            "minecraft:cave_vines_plant",
            "#minecraft:wall_signs",
            "#minecraft:rails",
            "#minecraft:fire",
            "minecraft:snow",
            "minecraft:redstone_torch",
            "minecraft:torch",
            "minecraft:soul_torch",
            "minecraft:redstone_wall_torch",
            "minecraft:wall_torch",
            "minecraft:soul_wall_torch",
            "#minecraft:buttons",
            "minecraft:lever",
            "#minecraft:inside_step_sound_blocks",
            "minecraft:firefly_bush",
            "minecraft:bush",
            "minecraft:cactus_flower",
            "minecraft:short_dry_grass",
            "minecraft:tall_dry_grass",
            "minecraft:light",
            "#minecraft:wool_carpets"
        ]}

def create_minecraft_load_tag():
    return {
        "values": [
            f"{NAMESPACE}:load",
            f"{NAMESPACE}:tick_2"
        ]
    }

def create_minecraft_tick_tag():
    return {
        "values": [
            f"{NAMESPACE}:tick"
        ]
    }

def create_item_item_entry(block):
    return {
        "model": {
            "type": "minecraft:model",
            "model": f"{NAMESPACE}:item/blocks/{block['id']}/{block['id']}_item"
        }
    }

def create_block_item_entry(block):
    return {
        "model": {
            "type": "minecraft:model",
            "model": f"{NAMESPACE}:item/blocks/{block['id']}/{block['id']}_block"
        }
    }

def create_item_model_entry(block):
    if block['seperate_item_model']:
        model = {
            "parent": "minecraft:item/generated",
            "textures": {
                "layer0": f"{NAMESPACE}:item/{block['id']}/{block['id']}_item"
            }
        }
    else:   
        model = {
            "parent": f"{NAMESPACE}:item/blocks/{block['id']}/{block['id']}_block"
            }

    return model

def create_block_model_entry(block):
    return {}

def create_item_frame_functions(blocks):
    check = []
    for block in blocks:
        check.append(f"execute if entity @s[tag={NAMESPACE}.{block['id']}_setup] run return run function {NAMESPACE}:blocks/{block['id']}/place")
    main = [f"execute at @s as @e[type=minecraft:item_frame,distance=..30] at @s run function {NAMESPACE}:item_frame/check",f"advancement revoke @s only {NAMESPACE}:blocks/item_frame"]

    save_generic_mcfunction("check", OUTPUT_DIR / "data" / NAMESPACE / "function" / "item_frame", check)
    save_generic_mcfunction("main", OUTPUT_DIR / "data" / NAMESPACE / "function" / "item_frame", main)

def create_load_master_entry(blocks):
    function = []
    for block in blocks:
        function.extend([f"# {block['id']}", f"scoreboard objectives add {NAMESPACE}.{block['id']}.dummy dummy", f"scoreboard objectives add {NAMESPACE}.{block['id']}.hit_count dummy", f"scoreboard objectives add {NAMESPACE}.{block['id']}.hit_timer dummy", f"scoreboard objectives add {NAMESPACE}.{block['id']}.rotation dummy", ""])
    return function

def create_tick_master_entry(blocks):
    function = []
    for block in blocks:
        function.append(f"function {NAMESPACE}:blocks/{block['id']}/tick")
    return function

def create_tick_2_master_entry():
    return [f"schedule function {NAMESPACE}:tick_2 2t replace", "", f"execute as @e[type=minecraft:item_display,tag={NAMESPACE}.block] at @s run function {NAMESPACE}:blocks/blocks"]

def create_blocks_master_entry(blocks):
    function = []
    for block in blocks:
        function.append(f"execute if entity @s[tag={NAMESPACE}.{block['id']}] run function {NAMESPACE}:blocks/{block['id']}/tick")
    return function

def create_tick_entry(block):
    function = []
    function.append(f"execute if score @s {NAMESPACE}.{block['id']}.hit_count matches 1.. run function {NAMESPACE}:blocks/{block['id']}/break/check")
    if block['can_float'] == False: function.append("","# The block cannot float, so check if air is below it and break if true", f"execute unless block ~ ~ ~ minecraft:barrier run function {NAMESPACE}:blocks/{block['id']}/break/break", f"execute if block ~ ~-1 ~ #{NAMESPACE}:blocks run function {NAMESPACE}:blocks/{block['id']}/break/break")
    return function

def create_place_entry(block):
    return ["# remove setup item frame", "kill @s", "", "# play place block sound", f"playsound {block['place_block_sound']}", "", "# spawn the block's item display", f"execute unless block ~ ~ ~ #minecraft:air run return run loot spawn ~ ~ ~ loot {NAMESPACE}:blocks/{block['id']}", f"execute align xyz positioned ~0.5 ~0.5 ~0.5 as @n[tag=smithed.block,distance=..0.1] at @s run return run loot spawn ~ ~ ~ loot {NAMESPACE}:blocks/{block['id']}", "", "setblock ~ ~ ~ minecraft:barrier", "", "# rotate to player orientation", f"data modify storage {NAMESPACE}:temp rotation set value 0", f"execute store result score $player_rotation {NAMESPACE}.{block['id']}.dummy run data get entity @p[advancements={{{NAMESPACE}:blocks/item_frame=true}}] Rotation[0]", f"execute if score $player_rotation {NAMESPACE}.{block['id']}.dummy matches 135..180 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage {NAMESPACE}:temp rotation set value 90", f"execute if score $player_rotation {NAMESPACE}.{block['id']}.dummy matches -180..-135 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage {NAMESPACE}:temp rotation set value 90", f"execute if score $player_rotation {NAMESPACE}.{block['id']}.dummy matches -135..-45 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage {NAMESPACE}:temp rotation set value 180", f"execute if score $player_rotation {NAMESPACE}.{block['id']}.dummy matches -45..45 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage {NAMESPACE}:temp rotation set value -90", f"execute if score $player_rotation {NAMESPACE}.{block['id']}.dummy matches 45..135 align xyz positioned ~0.5 ~0.5 ~0.5 run data modify storage {NAMESPACE}:temp rotation set value 0", "", "# run data to macro", f"function {NAMESPACE}:blocks/{block['id']}/macro with storage {NAMESPACE}:temp", f"scoreboard players set @n[type=minecraft:item_display,tag={NAMESPACE}.{block['id']}] {NAMESPACE}.{block['id']}.hit_count 0", f"scoreboard players set @n[type=minecraft:item_display,tag={NAMESPACE}.{block['id']}] {NAMESPACE}.{block['id']}.hit_timer 0"]

def create_macro_entry(block):
    if block['interact'] == True:
        macro = f"$execute align xyz run summon item_display ~0.5 ~0.5 ~0.5 {{Tags:[\"{NAMESPACE}.{block['id']}\",\"{NAMESPACE}.block\",\"smithed.block\",\"smithed.entity\",\"smithed.strict\"],transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1f,1f,1f],translation:[0.0f,0.0f,0.0f]}},item:{{id:\"minecraft:barrier\",count:1,components:{{\"minecraft:item_model\":\"{NAMESPACE}:blocks/{block['id']}/{block['id']}_block\"}}}},Rotation:[$(rotation),0.0],Passengers:[{{id:\"minecraft:interaction\",Tags:[\"{NAMESPACE}.{block['id']}_interaction\",\"{NAMESPACE}.{block['id']}_interaction_base\",\"smithed.block\",\"smithed.entity\",\"smithed.strict\"],height:-0.501,width:1.01,response:true}}, {{id:\"minecraft:interaction\",Tags:[\"{NAMESPACE}.{block['id']}_interaction\",\"{NAMESPACE}.{block['id']}_interaction_base\",\"smithed.block\",\"smithed.entity\",\"smithed.strict\"],height:0.501,width:1.01,response:true}}]}}"
    else:
        macro = f"$execute align xyz run summon item_display ~0.5 ~0.5 ~0.5 {{Tags:[\"{NAMESPACE}.{block['id']}\",\"{NAMESPACE}.block\",\"smithed.block\",\"smithed.entity\",\"smithed.strict\"],transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1f,1f,1f],translation:[0.0f,0.0f,0.0f]}},item:{{id:\"minecraft:barrier\",count:1,components:{{\"minecraft:item_model\":\"{NAMESPACE}:blocks/{block['id']}/{block['id']}_block\"}}}},Rotation:[$(rotation),0.0],Passengers:[{{id:\"minecraft:interaction\",Tags:[\"{NAMESPACE}.{block['id']}_interaction\",\"{NAMESPACE}.{block['id']}_interaction_base\",\"smithed.block\",\"smithed.entity\",\"smithed.strict\"],height:-0.501,width:1.01,response:false}}, {{id:\"minecraft:interaction\",Tags:[\"{NAMESPACE}.{block['id']}_interaction\",\"{NAMESPACE}.{block['id']}_interaction_base\",\"smithed.block\",\"smithed.entity\",\"smithed.strict\"],height:0.501,width:1.01,response:false}}]}}"

    return macro

def create_interaction_entry(block):
    return [f"advancement revoke @s only {NAMESPACE}:blocks/{block['id']}/hit_{block['id']}", f"function {block['interaction_function']}"]

def create_hit_hit_entry(block):
    return [f"advancement revoke @s only {NAMESPACE}:blocks/{block['id']}/hit_{block['id']}", f"function {NAMESPACE}:blocks/{block['id']}/hit/main"]

def create_hit_main_entry(block):
    return [f"scoreboard players set $hit_{block['id']}_check {NAMESPACE}.{block['id']}.dummy 0", "", f"tag @s add {NAMESPACE}.hit_{block['id']}", f"execute as @e[type=minecraft:interaction,tag={NAMESPACE}.{block['id']}_interaction_base,distance=..20,sort=nearest] run function {NAMESPACE}:blocks/{block['id']}/hit/check", f"tag @s remove {NAMESPACE}.hit_{block['id']}"]

def create_hit_check_entry(block):
    return [f"execute if score $hit_{block['id']}_check {NAMESPACE}.{block['id']}.dummy matches 1 run return fail", "", f"execute on attacker if entity @s[tag={NAMESPACE}.hit_{block['id']}] run scoreboard players set $hit_{block['id']}_check {NAMESPACE}.{block['id']}.dummy 1", f"execute if score $hit_{block['id']}_check {NAMESPACE}.{block['id']}.dummy matches 1 run data remove entity @s attack", f"execute if score $hit_{block['id']}_check {NAMESPACE}.{block['id']}.dummy matches 1 on vehicle run scoreboard players add @s {NAMESPACE}.{block['id']}.hit_count 1", f"execute if score $hit_{block['id']}_check {NAMESPACE}.{block['id']}.dummy matches 1 on vehicle at @s run playsound {block['hit_block_sound']}", f"execute if score $hit_{block['id']}_check {NAMESPACE}.{block['id']}.dummy matches 1 on vehicle at @s run particle {block['hit_block_particle']}"]

def create_break_check_entry(block):
    return [f"execute if score @s {NAMESPACE}.{block['id']}.hit_timer matches 60 run scoreboard players set @s {NAMESPACE}.{block['id']}.hit_count 0", f"execute if score @s {NAMESPACE}.{block['id']}.hit_timer matches 60 run return run scoreboard players set @s {NAMESPACE}.{block['id']}.hit_timer 0", f"execute if score @s {NAMESPACE}.{block['id']}.hit_count matches 1..{block['hit_count'] - 1} run return run scoreboard players add @s {NAMESPACE}.{block['id']}.hit_timer 1", "", f"function {NAMESPACE}:blocks/{block['id']}/break/break"]

def create_break_break_entry(block):
    return ["execute on passengers run kill @s", f"execute as @e[type=interaction,distance=..0.65,tag={NAMESPACE}.{block['id']}_interaction] run kill @s", "kill @s", "", "setblock ~ ~ ~ minecraft:air replace", f"playsound {block['break_block_sound']}", f"particle {block['break_block_particle']}", "", f"loot spawn ~ ~ ~ loot {NAMESPACE}:blocks/{block['id']}"]

# === FILE WRITERS ===
def save_generic_json(name, folder, file):

    folder.mkdir(parents=True, exist_ok=True)
    filename = folder / f"{name.lower()}.json"
    with open(filename, "w") as f:
        json.dump(file, f, indent=2)

def save_generic_mcmeta(name, folder, file):
    # lazy ik but i dont want to add a new parameter soooooo
    folder.mkdir(parents=True, exist_ok=True)
    filename = folder / f"{name.lower()}.mcmeta"
    with open(filename, "w") as f:
        json.dump(file, f, indent=2)

def save_generic_mcfunction(name, folder, function):

    folder.mkdir(parents=True, exist_ok=True)
    filename = folder / f"{name.lower()}.mcfunction"
    with open(filename, "w") as f:
        if isinstance(function, list):
            f.write("\n".join(function)) # multiline
        else:
            f.write(function) # single line

if __name__ == "__main__":
    main()
