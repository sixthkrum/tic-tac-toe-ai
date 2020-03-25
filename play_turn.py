import curses


_move_count = 0


class turn_completed ( BaseException ) :

    pass


def move_up ( scr = curses.initscr() ) :

    [ y , x ] = scr.getyx()

    if y != 0 :
        y = y - 2

    scr.move ( y , x )
    scr.refresh()


def move_down ( scr = curses.initscr() ) :

    [ y , x ] = scr.getyx()

    if y != 4 :
        y = y + 2

    scr.move ( y , x )
    scr.refresh()


def move_left ( scr = curses.initscr() ) :

    [ y , x ] = scr.getyx()

    if x != 2 :
        x = x - 4

    scr.move ( y , x )
    scr.refresh()


def move_right ( scr = curses.initscr() ) :

    [ y , x ] = scr.getyx()

    if x != 10 :
        x = x + 4

    scr.move ( y , x )
    scr.refresh()


def place_mark ( scr = curses.initscr() ) :

    global _move_count

    [ y , x ] = scr.getyx()

    scr.addstr ( str ( _move_count % 2 ) )

    scr.move ( y , x )

    _move_count = _move_count + 1

    raise turn_completed()


def empty_function ( *args ) :

    pass


switcher = {
curses.KEY_UP : move_up ,
curses.KEY_DOWN : move_down ,
curses.KEY_LEFT : move_left ,
curses.KEY_RIGHT : move_right ,
32 : place_mark
}


def play_move ( scr = curses.initscr() ) :

    global _move_count

    scr.move ( 0 , 2 )

    try :
        while True :

            keypress = scr.getch()
            move = switcher.get ( keypress , empty_function )
            move ( scr )

    except turn_completed :
        scr.addstr ( 6 , 0 , "move no. {}".format ( _move_count ) )
