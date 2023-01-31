import melee

console = melee.Console(path="C:/Users/jacob/AppData/Roaming/Slippi Launcher/netplay")
controller = melee.Controller(console = console, port=1)
controller_human = melee.Controller(console=console, port=2, type=melee.ControllerType.GCN_ADAPTER)

console.run()
console.connect()

controller.connect()
controller_human.connect()

while True:
    gamestate = console.step()
    if gamestate.menu_state in [melee.enums.Menu.IN_GAME, melee.Menu.SUDDEN_DEATH]:
        pass
    else:
        melee.menuhelper.MenuHelper.menu_helper_simple(gamestate=gamestate,controller=controller, character_selected= melee.Character.FOX, stage_selected=melee.Stage.BATTLEFIELD, autostart=False, swag=True)

