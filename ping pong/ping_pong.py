#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as timer


#шрифты и надписи
font.init()
font1 = font.SysFont("Arial", 36)
font2 = font.SysFont("Arial", 36)

lose1 = font1.render("Player 1 lose!", True, (255, 255, 255))
lose2 = font1.render("Player 2 lose!", True, (255, 255, 255))

#нам нужны такие картинки:
img_back = "galaxy.jpg" #фон игры
img_hero = "rocket.png" #герой
img_enemy = "ufo.png"
img_bullet = "bullet.png"
img_ast = "asteroid.png"
   
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -10)
        bullets.add(bullet)

    

#Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


#создаем спрайты
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)


#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна

while run:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
           run = False


    if not finish:
       #обновляем фон
       window.blit(background,(0,0))


       #производим движения спрайтов
       ship.update()
       #обновляем их в новом местоположении при каждой итерации цикла
       ship.reset()



       display.update()
   #цикл срабатывает каждые 0.05 секунд
    time.delay(50)
