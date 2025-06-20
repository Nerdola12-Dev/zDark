from apis import MCData


MCData.clear()


MCData.name("zDark")  # Define o nome do cheat, ativa o sistema de injeção automática


minerios = [
    "minecraft:deepslate_diamond_ore",
    "minecraft:deepslate_iron_ore",
    "minecraft:deepslate_gold_ore",
    "minecraft:deepslate_coal_ore",
]


x_range = range(-2, 3)
y_range = range(-1, 2)
z_range = range(-2, 3)


# Detecta minérios próximos e teleporta o jogador para dentro do bloco
for bloco in minerios:
    for y in y_range:
        for x in x_range:
            for z in z_range:
                MCData.cmd(
                    f'execute as @a at @s if block ~{x} ~{y} ~{z} {bloco} run tp @s ~{x} ~{y} ~{z}',
                    MCData.Type.loop()
                )
                MCData.cmd(
                    f'execute as @a at @s if block ~{x} ~{y} ~{z} {bloco} run setblock ~{x} ~{y} ~{z} air destroy',
                    MCData.Type.loop()
                )
                MCData.cmd(
                    f'execute as @a at @s run effect give @a minecraft:regeneration 1 255 false',
                    MCData.Type.loop()
                )


MCData.cmd(
    f'execute as @a at @s run tp @s ~0.5 -58 ~',
    MCData.Type.loop()
)
MCData.cmd(
    f'execute as @a at @s run setblock ~ ~1 ~ air destroy',
    MCData.Type.loop()
)
MCData.cmd(
    f'execute as @a at @s run fill ~1 ~1 ~1 ~-1 ~-1 ~-1 air destroy',
    MCData.Type.loop()
)
MCData.cmd(
    f'execute as @a at @s run kill @e[type=item,distance=..100,nbt={{Item:{{id:"minecraft:cobbled_deepslate"}}}}]',
    MCData.Type.loop()
)

# Auto-coleta de itens a até 2 blocos de distância
MCData.cmd(
    'execute as @a at @s if entity @e[type=item,distance=..100] run tp @e[type=item,sort=nearest,limit=1,distance=..100] ~ ~ ~', 
    MCData.Type.loop()
)
