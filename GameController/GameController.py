import time
import threading
import pygame
import json
import numpy as np

from GameComponents.Renderer import Renderer
from GameComponents.Cell import *
from datetime import datetime


class GameController():

    def __init__(self, game_settings, game_builder):
        self.renderer = Renderer()
        self.game_settings = game_settings
        self.game_builder = game_builder

        self.thread = None
        self.tick_rate = self.game_settings.tick_rate
        self.real_time_run_state = False

    def init_game(self):
        pygame.init()

        self.renderer.draw_buttons(self.game_builder)
        self.renderer.draw_cells(self.game_settings, self.game_builder)
        self.renderer.draw_grid(self.game_settings,self.game_builder)

        self.update_display()

    def __real_time_run(self, ticks):
        while self.real_time_run_state:
            self.next_generation()
            self.update_game()
            time.sleep(ticks)

    def next_generation(self):
        new_generation = []
        for cell in self.game_builder.cells:
            alive_neighbors = cell.get_alive_neighbors()
            if cell.state == CellState.Dead:
                if alive_neighbors == 3:
                    new_generation.append(Cell(CellState.Alive, cell.size, cell.index_x, cell.index_y))
                else:
                    new_generation.append(Cell(CellState.Dead, cell.size, cell.index_x, cell.index_y))
            elif cell.state == CellState.Alive:
                if alive_neighbors < 2:
                    new_generation.append(Cell(CellState.Dead, cell.size, cell.index_x, cell.index_y))
                elif alive_neighbors > 3:
                    new_generation.append(Cell(CellState.Dead, cell.size, cell.index_x, cell.index_y))
                elif alive_neighbors == 3 or alive_neighbors == 2:
                    new_generation.append(Cell(CellState.Alive, cell.size, cell.index_x, cell.index_y))

        for cell in new_generation:
            cell.set_neighbors(new_generation, self.game_settings.n_cells_x, self.game_settings.n_cells_y)

        self.game_builder.set_cells(new_generation)
        self.update_game()

    def start_stop(self):
        self.real_time_run_state = not self.real_time_run_state
        if self.real_time_run_state:
            self.thread = threading.Thread(target=self.__real_time_run, args=(self.game_settings.tick_rate,))
            self.thread.start()
        else:
            self.thread.join()

    def update_game(self):
        self.game_builder.update()
        self.renderer.draw_cells(self.game_settings, self.game_builder)
        self.renderer.draw_grid(self.game_settings,self.game_builder)
        self.update_display()

    def toggle_cell_event(self, cell):
        cell.state = not cell.state
        self.update_game()

    def clear_board(self):
        if not self.real_time_run_state:
            self.game_builder.set_cells(self.game_builder.cells_factory.create_empty_board(self.game_settings))
            self.update_game()

    def new_random_board(self):
        self.game_builder.set_cells(self.game_builder.cells_factory.create_cells(self.game_settings))
        self.update_game()

    def load_from_file(self, path="./saved/saved_board.txt"):
        if not self.real_time_run_state:
            try:
                with open(path, 'r') as file:
                    data = json.load(file)
                    n_cells_x = int(data["n_cells_x"])
                    n_cells_y = int(data["n_cells_y"])
                    cell_size = int(data["cell_size"])
                    cells = np.array(data["cells"], dtype=np.int32)
                    print(f"Loaded file from {path}")
                    converted_cells = self.game_builder.cells_factory.create_custom_board(n_cells_x, n_cells_y,
                                                                                          cell_size, cells)
                    self.clear_board()
                    self.game_builder.set_cells(converted_cells)
                    self.game_settings.n_cells_x = n_cells_x
                    self.game_settings.n_cells_y = n_cells_y
                    self.game_settings.cell_size = cell_size
                    self.update_game()
            except Exception as e:
                print(f"Cannot load file: {e}")

    def save_to_file(self):
        current_date = self.get_current_date_as_string()
        path = f"./saved/board-{current_date}"
        if not self.real_time_run_state:
            data_to_save = self.get_json_save(self.game_settings, self.game_builder)
            try:
                with open(path, 'w') as file:
                    json.dump(data_to_save, file, indent=2)
                    print(f"Saved in file {path}")
            except Exception as e:
                print(f"Cannot save file : {e}")
        else:
            print("Stop the game after saving.")

    @staticmethod
    def get_json_save(game_settings, game_builder):
        n_cells_x = game_settings.n_cells_x
        n_cells_y = game_settings.n_cells_y
        cell_size = game_settings.cell_size
        cells = game_builder.cells

        result_cells_arr = [[0] * n_cells_y for _ in range(n_cells_x)]

        for y in range(n_cells_y):
            for x in range(n_cells_x):
                for cell in cells:
                    if cell.index_x == x and cell.index_y == y:
                        result_cells_arr[y][x] = int(cell.state)
                        break

        result = {
            "n_cells_x": n_cells_x,
            "n_cells_y": n_cells_y,
            "cell_size": cell_size,
            "cells": result_cells_arr
        }
        return result

    @staticmethod
    def update_display():
        pygame.display.flip()
    @staticmethod
    def get_current_date_as_string():
        current_date = datetime.now()
        return current_date.strftime("%d-%m-%Y--%H-%M-%S")

