import curses
import graphics
import play_turn


def main ( stdscr ) :

    graphics.draw_screen ( stdscr )

    while not play_turn.check_full ( stdscr ) :

        state = play_turn.play_move ( stdscr )

        if state == -1 :

            stdscr.addstr ( 7 , 0 , "o wins")
            stdscr.refresh()

            break

        elif state == 1 :

            stdscr.addstr ( 7 , 0 , "x wins")
            stdscr.refresh()

            break

    if state == 0 :

        stdscr.addstr ( 7 , 0 , "draw")
        stdscr.refresh()

    stdscr.getch()

    return 1


if __name__ == '__main__':

    curses.wrapper ( main )
