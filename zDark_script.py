from apis import MCData

scoreboards = MCData.scoreboards
Type = MCData.Type
execute = MCData.execute
Entity = MCData.Entity

MCData.name("zDark_script")

MCData.clear()

scoreboards.create("godmode", "dummy", Type.start())
#/execute as @a[scores={godmode=1}] at @s run gamemode creative @s
execute(
    [
        f"as {Entity.all_players()}[scores={{godmode=1}}]",
        "at @s"
    ],
    "gamemode creative @s",
    Type.loop()
)
#/execute as @a[scores={godmode=0}] at @s run gamemode survival @s
execute(
    [
        f"as {Entity.all_players()}[scores={{godmode=0}}]",
        "at @s"
    ],
    "gamemode survival @s",
    Type.loop()
)

MCData.extra_inject()
