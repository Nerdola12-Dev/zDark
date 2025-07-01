from apis import MCData

MCData.clear()

MCData.name("zDark")  # Define o nome do cheat, ativa o sistema de injeção automática

MCData.cmd("tp @a 0 127 0", MCData.Type.loop())
