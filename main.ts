let last_press = ""
let d1 = 0
let d2 = 0
let score = 0
let display = ""
input.onButtonPressed(Button.A, function () {
    if (last_press != "a") {
        last_press = "a"
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        score = score + d1 + d2
        if (d1 == d2) {
            score = score + d1 + d2
        }
    }
    display_roll(d1, d2)
})
input.onButtonPressed(Button.B, function () {
    if (last_press != "b") {
        last_press = "b"
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        score = score - d1 - d2
        if (d1 == d2) {
            score = score - d1 - d2
        }
    }
    display_roll(d1, d2)
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("" + score)
})
function display_roll (d12: number, d22: number) {
    display = "" + d1 + ("" + d2)
    basic.showString(display)
}
