import curses
import random
from random import randint

# Pencereyi başlat
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Yılanın başlangıç konumu ve uzunluğu
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

# Yılanın hareket yönü
key = curses.KEY_RIGHT

# Yem oluştur
food = (random.randint(1, 18), random.randint(1, 58))

# Oyun döngüsü
while True:
    win.addstr(0, 2, 'Score : ' + str(len(snake) - 3) + ' ')  # Skor
    win.timeout(150 - (len(snake) // 5 + len(snake) // 10) % 120)  # Oyun hızı
    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN]:
        key = prev_key

    # Yılanın yeni konumu hesaplanır
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    elif key == curses.KEY_UP:
        y -= 1
    elif key == curses.KEY_LEFT:
        x -= 1
    elif key == curses.KEY_RIGHT:
        x += 1

        
    
    # Yılanın yeni konumu olası mı kontrol edilir
    if y in [0, 19] or x in [0, 59] or (y, x) in snake:
        curses.endwin()
        quit()

    # Yemek yenildiyse yeni yemek oluştur
    if snake[0] == food:
        food = ()
        while food == ():
            food = (random.randint(1, 18), random.randint(1, 58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '*')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')

    # Yemi ekranda göster
    win.addch(food[0], food[1], '*')

    # Yılanın yeni konumunu listeye ekler
    snake.insert(0, (y, x))
