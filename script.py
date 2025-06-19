from apis import MCData

MCData.clear()

MCData.name("zDark")  # Define o nome do cheat, ativa o sistema de injeção automática

minerios = [
    "minecraft:diamond_ore",
    "minecraft:iron_ore",
    "minecraft:gold_ore",
    "minecraft:coal_ore",
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

# Auto-coleta de itens a até 2 blocos de distância
MCData.cmd(
    'execute as @a at @s if entity @e[type=item,distance=..12] run tp @s @e[type=item,sort=nearest,limit=1,distance=..12]', 
    MCData.Type.loop()
)
