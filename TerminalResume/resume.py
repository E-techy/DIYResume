import curses



def main(stdscr):

    # --- SETUP ---

    # hide the flashing cursor

    curses.curs_set(0)

    # enable Keypad mode (allows reading Arrow keys and Function keys)

    stdscr.keypad(1)

    

    # --- MOUSE SETUP ---

    # This line tells the terminal to report mouse clicks to us.

    # curses.ALL_MOUSE_EVENTS captures clicks, releases, and drags.

    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)



    # --- COLORS ---

    # Initialize colors if the terminal supports them

    if curses.has_colors():

        curses.start_color()

        # Pair 1: Cyan text on Black (Headers)

        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

        # Pair 2: Black text on White (Selected Menu Item)

        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # Pair 3: White text on Black (Regular text)

        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # Pair 4: Green text on Black (Avatar/Accent)

        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)



    # --- CONTENT DATA ---

    pages = ["About", "Experience", "Skills", "Contact"]

    current_page = 0

    

    # Your ASCII Avatar

    avatar = "holla"

    content = {

        "About": [

            "NAME: John Doe",

            "ROLE: Creative Developer",

            "",

            "I build terminal apps and cool",

            "interactive scripts.",

            "",

            "Based in: The Grid"

        ],

        "Experience": [

            "2023 - Present: Senior Engineer",

            "   * Built the core system",

            "   * Optimized pipelines",

            "",

            "2020 - 2023: Junior Dev",

            "   * Fixed bugs",

            "   * Drank coffee"

        ],

        "Skills": [

            "PROGRAMMING:",

            " [#####     ] Python",

            " [#######   ] Bash",

            " [######### ] Linux",

            "",

            "TOOLS:",

            " Git, Docker, Vim"

        ],

        "Contact": [

            "EMAIL: hello@example.com",

            "GITHUB: github.com/johndoe",

            "",

            "Press 'q' to quit."

        ]

    }



    # --- MAIN LOOP ---

    while True:

        stdscr.clear()

        

        # Get current screen dimensions

        # height (y), width (x)

        height, width = stdscr.getmaxyx()



        # 1. DRAW HEADER

        header_text = " TERMINAL RESUME "

        # Center the header

        header_x = max(0, (width // 2) - (len(header_text) // 2))

        stdscr.addstr(1, header_x, header_text, curses.color_pair(1) | curses.A_BOLD)

        

        # 2. DRAW SIDEBAR (LEFT)

        sidebar_x = width // 4

        # Draw vertical line

        for y in range(3, height - 2):

            stdscr.addch(y, sidebar_x, '|')

        

        # Draw Avatar (Centered in the left sidebar space)

        # sidebar center point is sidebar_x / 2

        avatar_center_x = sidebar_x // 2

        start_y_avatar = 5

        

        for i, line in enumerate(avatar):

            # Calculate x to center this specific line

            line_x = max(0, avatar_center_x - (len(line) // 2))

            if start_y_avatar + i < height:

                stdscr.addstr(start_y_avatar + i, line_x, line, curses.color_pair(4))



        # 3. DRAW NAVIGATION BAR (TOP) AND STORE CLICK ZONES

        nav_y = 3

        nav_start_x = sidebar_x + 5

        # We will store the button positions to check against mouse clicks later

        # Format: {'PageName': (start_x, end_x)}

        button_zones = {} 



        current_x_pos = nav_start_x

        

        for i, page in enumerate(pages):

            label = f" {page} "

            

            # Styling: Invert colors if selected

            if i == current_page:

                style = curses.color_pair(2) | curses.A_BOLD

            else:

                style = curses.color_pair(3)

            

            # Draw the button

            stdscr.addstr(nav_y, current_x_pos, label, style)

            

            # Store the coordinates for mouse hit-testing

            # zone starts at current_x_pos and ends at current_x_pos + len(label)

            button_zones[i] = (current_x_pos, current_x_pos + len(label))

            

            # Move x position for next button (label width + 2 spaces gap)

            current_x_pos += len(label) + 2



        # 4. DRAW PAGE CONTENT (RIGHT SIDE)

        content_y = 6

        content_x = sidebar_x + 5

        

        page_data = content[pages[current_page]]

        for i, line in enumerate(page_data):

            if content_y + i < height - 2:

                # Highlight lines with colons (Titles)

                style = curses.color_pair(1) | curses.A_BOLD if ":" in line else curses.color_pair(3)

                stdscr.addstr(content_y + i, content_x, line, style)



        # 5. DRAW FOOTER

        footer = "KEYBOARD: Left/Right Arrows | MOUSE: Click Tabs above | 'q' to Quit"

        # Truncate footer if screen is too narrow

        footer = footer[:width-1]

        stdscr.addstr(height - 1, 2, footer, curses.color_pair(3) | curses.A_DIM)



        # Apply changes to screen

        stdscr.refresh()



        # --- INPUT HANDLING ---

        # Wait for user input

        key = stdscr.getch()



        if key == curses.KEY_RIGHT:

            current_page = (current_page + 1) % len(pages)

        

        elif key == curses.KEY_LEFT:

            current_page = (current_page - 1) % len(pages)

        

        elif key == ord('q') or key == ord('Q'):

            break



        # --- MOUSE LOGIC ---

        elif key == curses.KEY_MOUSE:

            try:

                # getmouse() returns a tuple: (id, x, y, z, bstate)

                _, mx, my, _, _ = curses.getmouse()

                

                # Check if the click happened on the Navigation Row (nav_y)

                if my == nav_y:

                    # Check which button zone the X coordinate falls into

                    for page_index, (start_x, end_x) in button_zones.items():

                        if start_x <= mx <= end_x:

                            current_page = page_index

                            break

            except curses.error:

                # Some terminals throw an error if getmouse is called 

                # but the event wasn't a valid click. We safely ignore it.

                pass



if __name__ == "__main__":

    # curses.wrapper handles initialization and cleanup automatically

    # (Restores your terminal to normal if the script crashes)

    curses.wrapper(main)
