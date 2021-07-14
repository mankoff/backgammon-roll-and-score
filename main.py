last_press = ""
d1 = 0
d2 = 0
score = 0
display = ""

def on_button_pressed_a():
    global last_press, d1, d2, score
    if last_press != "a":
        last_press = "a"
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        score = score + d1 + d2
        if d1 == d2:
            score = score + d1 + d2
    display_roll(d1, d2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global last_press, d1, d2, score
    if last_press != "b":
        last_press = "b"
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        score = score - d1 - d2
        if d1 == d2:
            score = score - d1 - d2
    display_roll(d1, d2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("" + str((score)))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def display_roll(d12: number, d22: number):
    global display
    display = "" + str(d1) + str(d2)
    basic.show_string(display)