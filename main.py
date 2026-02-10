from machine import Pin, UART, I2C, Timer
from machine_i2c_lcd import I2cLcd
import time

# -----------------------------
# LCD Setup
# -----------------------------
i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.backlight_on()
lcd.clear()

# -----------------------------
# RS-485 / Feuchtigkeitssensor Setup
# -----------------------------
uart_rs485 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
de_re = Pin(10, Pin.OUT)
de_re.value(0)  # Empfangsmodus

SENSOR_IDS = [1, 2, 3, 4]
UPDATE_INTERVAL_MS = 3000
REGISTER_MOISTURE = 0x0000   # ggf. anpassen!
MAX_RETRIES = 3

# -----------------------------
# Timer / Flag Setup
# -----------------------------
update_needed = False

def timer_callback(timer):
    global update_needed
    update_needed = True

timer = Timer()
timer.init(period=UPDATE_INTERVAL_MS, mode=Timer.PERIODIC, callback=timer_callback)

# -----------------------------
# Modbus CRC
# -----------------------------
def modbus_crc(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return crc & 0xFFFF

# -----------------------------
# RS-485 Anfrage
# -----------------------------
def rs485_request(slave_id, register):
    uart_rs485.read()  # RX leeren

    frame = bytes([
        slave_id,
        0x03,
        (register >> 8) & 0xFF,
        register & 0xFF,
        0x00,
        0x01
    ])

    crc = modbus_crc(frame)
    frame += crc.to_bytes(2, "little")

    # Senden
    de_re.value(1)
    time.sleep_ms(3)
    uart_rs485.write(frame)
    uart_rs485.flush()

    # WICHTIG: DE noch NICHT sofort ausschalten
    time.sleep_ms(3)
    de_re.value(0)

    # Antwort einsammeln (max 200 ms)
    start = time.ticks_ms()
    resp = b""

    while time.ticks_diff(time.ticks_ms(), start) < 200:
        if uart_rs485.any():
            resp += uart_rs485.read()
            if len(resp) >= 7:
                return resp[:7]
        time.sleep_ms(2)

    return None

# -----------------------------
# Antwort auswerten
# -----------------------------
def parse_moisture(resp):
    if not resp or len(resp) != 7:
        return None

    if resp[1] != 0x03 or resp[2] != 0x02:
        return None

    value = (resp[3] << 8) | resp[4]
    return value / 10.0
# -----------------------------
# Hauptloop
# -----------------------------
last_moisture = {sid: None for sid in SENSOR_IDS}

while True:
    if update_needed:
        update_needed = False

        for sid in SENSOR_IDS:
            for _ in range(MAX_RETRIES):
                resp = rs485_request(sid, REGISTER_MOISTURE)
                moisture = parse_moisture(resp)
                if moisture is not None:
                    last_moisture[sid] = moisture
                    break
                time.sleep_ms(50)
            time.sleep_ms(50)


        # LCD Anzeige
        lcd.clear()
        lcd.putstr(
        f"S1:{last_moisture[1]:.1f} S2:{last_moisture[2]:.1f}\n"
        f" S3:{last_moisture[3]:.1f} S4:{last_moisture[4]:.1f}"
        )

    time.sleep_ms(100)
