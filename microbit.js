let gyro_y = 0
let gyro_x = 0
let tem = 0
let ult = 0
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate115200
)
basic.forever(function () {
    ult = randint(0, 10)
    tem = randint(0, 10)
    gyro_x = input.acceleration(Dimension.X)
    gyro_y = input.acceleration(Dimension.Y)
    serial.writeString("" + ult + "%%" + tem + "%%" + gyro_x + "." + gyro_y)
    basic.pause(1000)
})
