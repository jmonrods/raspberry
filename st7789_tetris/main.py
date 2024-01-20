import random
import machine
import utime
import st7789py as st7789


# Joystick code
adc_vrx = machine.ADC(machine.Pin(26))
adc_vry = machine.ADC(machine.Pin(27))
button_sw = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_UP)


def read_joystick():
    """Read values from the PS2 joystick."""
    vrx_value = adc_vrx.read_u16()
    vry_value = adc_vry.read_u16()
    sw_value = button_sw.value()
    return vrx_value, vry_value, sw_value


# Constants for joystick thresholds
JOYSTICK_THRESHOLD = 32768
JOYSTICK_DELAY = 100


# ST7789 Display code
BACKLIGHT_PIN = 10
RESET_PIN = 11
DC_PIN = 12
CS_PIN = 13
CLK_PIN = 14
DIN_PIN = 15  # lower left corner

spi = machine.SPI(1, baudrate=31250000, sck=machine.Pin(CLK_PIN), mosi=machine.Pin(DIN_PIN))

# display is 240x280 but this is unsupported, using 240x320
tft = st7789.ST7789(spi, 240, 320,
                    reset=machine.Pin(RESET_PIN, machine.Pin.OUT),
                    cs=machine.Pin(CS_PIN, machine.Pin.OUT),
                    dc=machine.Pin(DC_PIN, machine.Pin.OUT),
                    backlight=machine.Pin(BACKLIGHT_PIN, machine.Pin.OUT),
                    rotation=3)
tft.fill(st7789.BLACK)
tft.rotation(1)
tft.fill(0)


# Tetris game variables
board_width = 10
board_height = 20
board = [[0] * board_width for _ in range(board_height)]

global current_piece
global current_piece_position


# Tetris piece shapes and their rotations
tetris_shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
]


def new_piece():
    """Generate a new random Tetris piece."""
    shape = random.choice(tetris_shapes)
    return {
        'shape': shape,
        'rotation': 0,
        'position': [board_width // 2 - len(shape[0]) // 2, 0]
    }


def collide(piece, offset):
    """Check if a piece collides with the board or other pieces."""
    for y, row in enumerate(piece['shape']):
        for x, value in enumerate(row):
            if value and (board[y + offset[1]][x + offset[0]] or
                          x + offset[0] < 0 or x + offset[0] >= board_width or
                          y + offset[1] >= board_height):
                return True
    return False


def merge_piece(piece, offset):
    """Merge the piece into the board."""
    for y, row in enumerate(piece['shape']):
        for x, value in enumerate(row):
            if value:
                board[y + offset[1]][x + offset[0]] = 1


def rotate_piece(piece):
    """Rotate the current piece."""
    rotated = list(zip(*reversed(piece['shape'])))
    if not collide({'shape': rotated, 'position': piece['position'], 'rotation': (piece['rotation'] + 1) % 4}, [0, 0]):
        piece['shape'] = rotated
        piece['rotation'] = (piece['rotation'] + 1) % 4


def move_piece(piece, offset):
    """Move the current piece left, right, or down."""
    new_position = [piece['position'][0] + offset[0], piece['position'][1] + offset[1]]
    if not collide({'shape': piece['shape'], 'position': new_position, 'rotation': piece['rotation']}, offset):
        piece['position'] = new_position
        return True
    return False


def clear_lines():
    """Clear completed lines from the board."""
    lines_to_clear = [i for i, row in enumerate(board) if all(row)]
    for i in lines_to_clear:
        del board[i]
        board.insert(0, [0] * board_width)


def update_board():
    """Update the game board."""
    global current_piece
    global current_piece_position
    if not move_piece(current_piece, [0, 1]):
        merge_piece(current_piece, current_piece_position)
        clear_lines()
        current_piece = new_piece()
        current_piece_position = [0, 0]


def draw_board():
    """Draw the Tetris board on the display."""
    for y, row in enumerate(board):
        for x, value in enumerate(row):
            color = st7789.BLUE if value else st7789.BLACK
            tft.pixel(x, y, color)


def draw_piece(piece, offset):
    """Draw the current Tetris piece on the display."""
    for y, row in enumerate(piece['shape']):
        for x, value in enumerate(row):
            if value:
                color = st7789.RED
                tft.pixel(x + piece['position'][0] + offset[0], y + piece['position'][1] + offset[1], color)


def update_display():
    """Update the display with the current game state."""
    tft.fill(st7789.BLACK)
    draw_board()
    draw_piece(current_piece, current_piece_position)
    tft.show()


# Main game loop
def main():
    global current_piece
    global current_piece_position
    current_piece = new_piece()
    current_piece_position = [0, 0]

    while True:
        # Check for button input and update the game state
        vrx, vry, sw = read_joystick()

        if vrx < JOYSTICK_THRESHOLD:
            move_piece(current_piece, [-1, 0])  # Move piece left
        elif vrx > 65535 - JOYSTICK_THRESHOLD:
            move_piece(current_piece, [1, 0])  # Move piece right

        if vry > JOYSTICK_THRESHOLD:
            move_piece(current_piece, [0, 1])  # Move piece down

        if not sw:
            rotate_piece(current_piece)  # Rotate piece on button press

        if not move_piece(current_piece, [0, 1]):
            merge_piece(current_piece, current_piece_position)
            clear_lines()
            current_piece = new_piece()
            current_piece_position = [0, 0]

        # Update the display with the current game state
        update_display()

        # Pause for a short time to control the game speed
        utime.sleep_ms(500)


main()
