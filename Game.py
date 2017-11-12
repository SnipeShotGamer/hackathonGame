import pygame

from Clock import Clock
from Inventory import Inventory
from Config import Config
from Display import Display
from Objects import GameObject
from Contracts import InstanceOf
from Objects import Player

class GameState:
  PAUSED = 0
  PLAYING = 1
  INVENTORY = 2
  SCENE = 3

  def __init__(self, mode = PAUSED, keys = []):
    self.__mode = mode
    self.__keys = keys

  def GetKeys(self):
    return self.__keys

  def GetMode(self):
    return self.__mode

  def SetMode(self, mode):
    self.__mode = mode

class Game:
  Game = None

  def __init__(self):
    Game = self

    pygame.init()

    self.__previousState = GameState()

    Config.Init()
    Display.Init()

    self.__screen = Display.GetDisplay()

    Display.SetCaption(Config.Get("GameSettings")["Caption"])

    self.Clock = Clock().SetTick(int(Config.Get("GameSettings")["Fps"]))

    self.__gameObjects = []

  def AddGameObjects(self, *objects):
    for obj in objects:
      InstanceOf(obj, GameObject.GameObject)
      self.__gameObjects.append(obj)

  def Start(self):
    while True:
      previousMode = self.__previousState.GetMode()
      heldKeys = self.__previousState.GetKeys()
      pressedKeys = pygame.key.get_pressed()

      currentState = GameState(previousMode, pressedKeys)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.Quit()

        # Setting different modes
        if (event.type == pygame.KEYDOWN):
          if (previousMode == GameState.PAUSED):
            if (event.key == pygame.K_ESCAPE and not heldKeys[pygame.K_ESCAPE]):
              currentState.SetMode(GameState.PLAYING)

          if (previousMode == GameState.INVENTORY):
            if (event.key == pygame.K_e and not heldKeys[pygame.K_e]):
              Inventory.Close()
              currentState.SetMode(GameState.PLAYING)

          if (previousMode == GameState.PLAYING):
            if (event.key == pygame.K_ESCAPE and not heldKeys[pygame.K_ESCAPE]):
              currentState.SetMode(GameState.PAUSED)
            elif (event.key == pygame.K_e and not heldKeys[pygame.K_e]):
              Inventory.Open()
              currentState.SetMode(GameState.INVENTORY)

      self.CheckCollisions()

      self.Draw()

      self.__previousState = currentState

      self.Clock.Tick()

  def Draw(self):
    for obj in self.__gameObjects:
      obj.Draw()
      Display.Update()

  def CheckCollisions(self):
    objs = self.__gameObjects

    for firstObject in range(len(objs)):
      for secondObject in range(firstObject + 1, len(objs)):
        collisionState = CollisionState()

        if (objs[firstObject].x > objs[secondObject].x and objs[firstObject].x < objs[secondObject].x + objs[secondObject].width):
          collisionState.Left = True
        elif (objs[firstObject].x + objs[firstObject].width > objs[secondObject].x and objs[firstObject].x + objs[firstObject].width < objs[secondObject].x + objs[secondObject].width):
          collisionState.Right = True

        # We must not be colliding on the left or right
        if (collisionState.Left or collisionState.Right):
          continue

        if (objs[firstObject].y > objs[secondObject].y and objs[secondObject].y < objs[secondObject].y + objs[secondObject].height):
          collisionState.Top = True
        elif (objs[firstObject].y + objs[firstObject].height > objs[secondObject].y and objs[firstObject].y + objs[firstObject].height < objs[secondObject].y + objs[secondObject].height):
          collisionState.Bottom = True

        # We must not be colliding on the top or bottom
        if (collisionState.Top or collisionState.Bottom):
          continue

        objs[firstObject].Collides(objs[secondObject], collisionState)

  def GetGameState(self):
    return self.__previousState

  def Quit(self):
    pygame.quit()
    quit()

game = Game()
game.AddGameObjects(Player.PlayerS((0, 0), (0, 0), (16, 16), Player.PlayerStats(100, 0)))
game.Start()