import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)

    def move(self, direction):
        x, y = self.position
        if direction == 'RIGHT':
            self.position = (x, y + 1)
        elif direction == 'LEFT':
            self.position = (x, y - 1)
        elif direction == 'UP':
            self.position = (x - 1, y)
        elif direction == 'DOWN':
            self.position = (x + 1, y)

class Maze:
    def __init__(self, size):
        self.size = size
        self.player = Player("Player")
        self.exit = (size - 1, size - 1)
        self.obstacles = [(0, 3), (1, 0), (1, 1),(1, 4), (2, 2), (3, 3), (4, 5), (4, 1), (4, 3)]  # Example obstacles

    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.player.position:
                    print('P', end=' ')
                elif (i, j) == self.exit:
                    print('E', end=' ')
                elif (i, j) in self.obstacles:
                    print('X', end=' ')
                else:
                    print('.', end=' ')
            print()

    def check_collision(self):
        return self.player.position in self.obstacles

    def check_win(self):
        return self.player.position == self.exit

def main():
    maze_size = 6
    maze = Maze(maze_size)

    print("Bem-vindo ao Labirinto Game!")
    while True:
        maze.display()

        if maze.check_collision():
            print("Você colidiu com um obstáculo! Game Over.")
            break

        if maze.check_win():
            print("Parabéns! Você chegou à saída. Você venceu!")
            break

        direction = input("Para onde você deseja ir? (UP/DOWN/LEFT/RIGHT): ").upper()
        if direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            maze.player.move(direction)
        else:
            print("Comando inválido. Use UP, DOWN, LEFT ou RIGHT.")

if __name__ == "__main__":
    main()
