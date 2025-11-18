import marimo

__generated_with = "0.12.2"
app = marimo.App(width="medium")


@app.cell
def _(
    aztecDiamond,
    first_button,
    get_count2,
    mo,
    plot_aztec_diamond2,
    random,
    set_count2,
    slider,
):
    my_text2 = mo.md(
        "# Random Tilings of the Aztec Diamod \n The Aztec Diamond is diamond shape made of squares that can be tiled by dominos. Use the up/down arrows or enter a number to create larger and larger diamonds. Can you see any pattern in the tilings? "
    )


    random.seed(get_count2())
    bd = aztecDiamond("nn\nss")  # Create the variable if it does not exist

    m = slider.value  # int(input('Aztec Diamond size? '))
    for x in range(m - 1):
        bd = bd.removeBadBlocks().shuffle().fillGoodBlocks()
    # print(str(bd))
    # print(bd.tile)

    if first_button.value:
        set_count2(lambda value: value + 1)

    # Use the function to plot the tiles of the Aztec Diamond
    mo.vstack([my_text2, slider, plot_aztec_diamond2(bd.tile), first_button])
    return bd, m, my_text2, x


@app.cell
def _(mo):
    options = {
        "Step 1: Remove some tiles": 0,
        "Step 2: Slide tiles up/down/left/right to make room": 1,
        "Step 3: Fill In empty squares": 2,
    }
    radio = mo.ui.radio(options=options)
    return options, radio


@app.cell
def create_tiling(
    aztecDiamond,
    get_count,
    get_count3,
    mo,
    plot_aztec_diamond2,
    radio,
    random,
    randomize_button,
    reset_button,
    set_count,
    set_count3,
):
    my_text = mo.md(
        "# How is a random tiling made? \n There is a 3 step process to grow the tiling up from a small tiling to a bigger one. This was discovered by mathematicians researching this problem in 1992 (about 30 years ago). \n Click on the 3 steps in order to see the tiling grow. "
    )


    random.seed(get_count3())
    my_bd = aztecDiamond("nn\nss")  # Create the variable if it does not exist

    my_m = get_count()
    for i in range(my_m - 1):
        my_bd = my_bd.removeBadBlocks().shuffle().fillGoodBlocks()

    if radio.value == 0:
        my_bd = my_bd.removeBadBlocks()
    if radio.value == 1:
        my_bd = my_bd.removeBadBlocks().shuffle()
    if radio.value == 2:
        my_bd = my_bd.removeBadBlocks().shuffle().fillGoodBlocks()
        set_count(lambda value: value + 1)


    if reset_button.value:
        set_count(0)

    if randomize_button.value:
        set_count3(lambda value: value + 1)


    mo.vstack(
        [
            my_text,
            radio,
            plot_aztec_diamond2(my_bd.tile),
            reset_button,
            randomize_button,
        ]
    )


    #    my_bd = my_bd.removeBadBlocks()


    # for x in range(m-1):
    #  bd = bd.removeBadBlocks().shuffle().fillGoodBlocks()
    # print(str(bd))
    # print(bd.tile)

    # Use the function to plot the tiles of the Aztec Diamond
    # mo.vstack([slider, first_button, plot_aztec_diamond2(bd.tile)])
    return i, my_bd, my_m, my_text


@app.cell
def aztecdiamond():
    import random


    class aztecDiamond:
        def __init__(self, x):
            if type(x) == type(0):
                n = int(x)
                board = dict()
                for k in range(1, 2 * n + 1):
                    l = min(2 * k, 4 * n - 2 * k + 2)
                    for j in range(l):
                        board[(j + 0.5 - l / 2, k - n - 0.5)] = "x"
                board["size"] = n
                self.tile = board
            elif type(x) == type(""):
                b = x
                sq = b.split("\n")
                board = dict()
                n = int(len(sq) / 2)
                for k in range(1, 2 * n + 1):
                    l = min(2 * k, 4 * n - 2 * k + 2)
                    row = sq[k - 1].replace(".", "")
                    for j in range(l):
                        board[(j + 0.5 - l / 2, k - n - 0.5)] = row[j]
                board["size"] = int(len(sq) / 2)
                self.tile = board

        def removeBadBlocks(self):
            bd = self.tile
            n = int(bd["size"])
            for k in range(1, 2 * n + 1):
                l = min(2 * k, 4 * n - 2 * k + 2)
                for j in range(l):
                    a, b = j + 0.5 - l / 2, k - n - 0.5
                    try:
                        if (
                            bd[(a, b)].lower().startswith("s")
                            and bd[(a + 1, b)].lower().startswith("s")
                            and bd[(a, b + 1)].lower().startswith("n")
                            and bd[(a + 1, b + 1)].lower().startswith("n")
                        ) or (
                            bd[(a, b)].lower().startswith("e")
                            and bd[(a + 1, b)].lower().startswith("w")
                            and bd[(a, b + 1)].lower().startswith("e")
                            and bd[(a + 1, b + 1)].lower().startswith("w")
                        ):
                            bd[(a, b)] = "x"
                            bd[(a + 1, b)] = "x"
                            bd[(a, b + 1)] = "x"
                            bd[(a + 1, b + 1)] = "x"
                    except:
                        pass
            self.tile = bd
            return self

        def fillGoodBlocks(self):
            bd = self.tile
            n = int(bd["size"])
            for k in range(1, 2 * n + 1 - 1):
                l = min(2 * k, 4 * n - 2 * k + 2)
                for j in range(l - 1):
                    a, b = j + 0.5 - l / 2, k - n - 0.5
                    if (
                        bd[(a, b)] == "x"
                        and bd[(a + 1, b)] == "x"
                        and bd[(a, b + 1)] == "x"
                        and bd[(a + 1, b + 1)] == "x"
                    ):
                        if random.random() > 0.5:
                            bd[(a, b)] = "n" + str(a) + str(b)
                            bd[(a + 1, b)] = "n" + str(a) + str(b)
                            bd[(a, b + 1)] = "s" + str(a) + str(b)
                            bd[(a + 1, b + 1)] = "s" + str(a) + str(b)
                        else:
                            bd[(a, b)] = "w" + str(a) + str(b)
                            bd[(a + 1, b)] = "e" + str(a) + str(b)
                            bd[(a, b + 1)] = "w" + str(a) + str(b)
                            bd[(a + 1, b + 1)] = "e" + str(a) + str(b)
            self.tile = bd
            return self

        def shuffle(self):
            bd = self.tile
            x = aztecDiamond(int(bd["size"] + 1))
            board = x.tile
            n = int(bd["size"])
            for k in range(1, 2 * n + 1):
                l = min(2 * k, 4 * n - 2 * k + 2)
                for j in range(l):
                    if bd[(j + 0.5 - l / 2, k - n - 0.5)].lower().startswith("n"):
                        board[(j + 0.5 - l / 2, k - n - 0.5 - 1)] = bd[
                            (j + 0.5 - l / 2, k - n - 0.5)
                        ]
                    if bd[(j + 0.5 - l / 2, k - n - 0.5)].lower().startswith("e"):
                        board[(j + 0.5 - l / 2 + 1, k - n - 0.5)] = bd[
                            (j + 0.5 - l / 2, k - n - 0.5)
                        ]
                    if bd[(j + 0.5 - l / 2, k - n - 0.5)].lower().startswith("s"):
                        board[(j + 0.5 - l / 2, k - n - 0.5 + 1)] = bd[
                            (j + 0.5 - l / 2, k - n - 0.5)
                        ]
                    if bd[(j + 0.5 - l / 2, k - n - 0.5)].lower().startswith("w"):
                        board[(j + 0.5 - l / 2 - 1, k - n - 0.5)] = bd[
                            (j + 0.5 - l / 2, k - n - 0.5)
                        ]
            return x

        def __str__(self):
            bd = self.tile
            n = bd["size"]
            s = ""
            for k in range(1, 2 * n + 1):
                l = min(2 * k, 4 * n - 2 * k + 2)
                s += (
                    (int((2 * n - l) / 2) * ".")
                    + "".join(
                        [bd[(j + 0.5 - l / 2, k - n - 0.5)][0] for j in range(l)]
                    )
                    + (int((2 * n - l) / 2) * ".")
                    + "\n"
                )
            return s.replace("x", " ")


    # bd.toSVG('out.html')
    return aztecDiamond, random


@app.cell
def _(math, plt):
    def plot_aztec_diamond2(tile_dict):
        # Remove the item 0:2 if it exists
        # n = tile_dict.pop(0, None)  # Using pop with a default value to avoid KeyError

        color_map = {
            "n": "greenyellow",
            "s": "#CC0000",
            "e": "#3366FF",
            "w": "orange",
        }

        color_map = {
            "n": "#51D7D0",
            "s": "#FBEA5E",
            "e": "#FA7B52",
            "w": "#8551A8",
        }

        fig, ax = plt.subplots()

        # To store drawn rectangles and avoid drawing duplicates
        # drawn_rects = set()

        n = tile_dict[
            "size"
        ]  # this gets the size of the aztec diamond from the dictionary. stored with a spec

        for dict_entry in tile_dict.items():
            # print(dict_entry)
            if dict_entry[0] == "size":
                pass  # n = dict_entry[1]
            else:
                (x, y), tile_string = dict_entry
                tile_type = tile_string[0]
                if tile_type in color_map:
                    # Check if the current tile is part of a domino

                    # draw the color of the square
                    rect = plt.Rectangle((x, y), 1, 1, color=color_map[tile_type])
                    ax.add_patch(rect)

                    # this is to draw the outline
                    # if (x, y) not in drawn_rects:
                    # Look for adjacent tiles that share the same string identifier
                    domino_tiles = [(x, y)]

                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        # Check right neighbor
                        if (x + dx, y + dy) in tile_dict and tile_dict[
                            (x + dx, y + dy)
                        ] == tile_string:
                            domino_tiles.append((x + dx, y + dy))
                        # drawn_rects.add((x + dx, y+dy))

                    # Get the bounding box for the domino
                    min_x = min(tile[0] for tile in domino_tiles)
                    max_x = (
                        max(tile[0] for tile in domino_tiles) + 1
                    )  # Width of domino (1 unit)
                    min_y = min(tile[1] for tile in domino_tiles)
                    max_y = (
                        max(tile[1] for tile in domino_tiles) + 1
                    )  # Height of domino (1 unit)

                    # Draw the domino rectangle
                    rect_edge = plt.Rectangle(
                        (min_x, min_y),
                        max_x - min_x,
                        max_y - min_y,
                        edgecolor="black",
                        facecolor="none",
                        linewidth=int(5 / math.sqrt(n)),
                    )
                    ax.add_patch(rect_edge)

                    # Mark each part of domino as drawn
                    # drawn_rects.add((x, y))

        ax.set_aspect("equal")
        # n = bd.tile[0]
        ax.set_xlim(-n - 1, n + 1)  # Adjust limits according to your diamond size
        ax.set_ylim(-n - 1, n + 1)  # Adjust limits according to your diamond size
        ax.axis("off")  # Hide axes
        return plt.gca()  # Use plt.gca() instead of plt.show()
    return (plot_aztec_diamond2,)


@app.cell
def _():
    import matplotlib.pyplot as plt
    import math
    import marimo as mo

    slider = mo.ui.number(
        start=1, stop=70, label="Size of Diamond"
    )  # mo.ui.slider(start=2, stop=50, label="Size of Diamond", value=3)
    first_button = mo.ui.run_button(label="Randomize")

    randomize_button = mo.ui.run_button(label="Randomize")
    return first_button, math, mo, plt, randomize_button, slider


@app.cell
def _(mo):
    slider2 = mo.ui.number(
        start=1, stop=50, label="Size of Diamond"
    )  # mo.ui.slider(start=2, stop=50, label="Size of Diamond", value=3)
    reset_button = mo.ui.run_button(label="Reset (Press Twice)")
    get_count, set_count = mo.state(0)
    text = mo.ui.text(placeholder="Set random seed...")

    get_count2, set_count2 = mo.state(0)

    get_count3, set_count3 = mo.state(0)
    return (
        get_count,
        get_count2,
        get_count3,
        reset_button,
        set_count,
        set_count2,
        set_count3,
        slider2,
        text,
    )


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
