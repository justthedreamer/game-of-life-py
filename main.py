from GameManager.GameManager import GameManager
from GameComponents.Enum.Color import Color

## Create Game Manager Instance
game_manager = GameManager()
## Set custom cell color
game_manager.game_settings.set_cell_color(Color.ROSE_QUARTZ)
## Define path to load saved cells configuration
## To load configuracion, click LOAD button in running app
game_manager.game_controller.load_from_file(path="./saved/board-14-12-2023--17-11-01")
## Run game
game_manager.run()
