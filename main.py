from GameManager.GameManager import GameManager
from GameComponents.Enum.Color import Color

game_manager = GameManager()
game_manager.game_settings.set_cell_color(Color.ROSE_QUARTZ)
game_manager.game_settings.off_grid()
game_manager.game_controller.load_from_file(path="./saved/board-14-12-2023--17-11-01")
game_manager.run()