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


int_to_mark_switcher = {
0 : "o" ,
1 : "x"
}


def place_mark ( scr = curses.initscr() ) :

    [ y , x ] = scr.getyx()

    if chr ( scr.inch ( y , x ) ) == " " :

        global _move_count

        scr.addstr ( int_to_mark_switcher.get ( _move_count % 2 ) )

        scr.move ( y , x )

        _move_count = _move_count + 1

        return True

    return False


def empty_function ( *args ) :

    pass



mark_to_int_switcher = {
"o" : -1 ,
"x" : 1 ,
" " : 0
}


def check_win ( scr = curses.initscr() ) :

# checking horizontals and verticals with h and v diagnol and anti-diagnol with d and ad

    total_d = 0
    total_ad = 0

    for j in range ( 3 ) :

        total_d = total_d + mark_to_int_switcher.get ( chr ( scr.inch ( j * 2 , 2 + j * 4 ) ) )
        total_ad = total_ad + mark_to_int_switcher.get ( chr ( scr.inch ( j * 2 , 2 + ( 2 - j ) * 4 ) ) )

        total_h = 0
        total_v = 0

        for i in range ( 3 ) :

            total_h = total_h + mark_to_int_switcher.get ( chr ( scr.inch ( j * 2 , 2 + i * 4 ) ) )
            total_v = total_v + mark_to_int_switcher.get ( chr ( scr.inch ( i * 2 , 2 + j * 4 ) ) )

        if total_h == -3 or total_v == -3 :

            return -1

        elif total_h == 3 or total_v == 3 :

            return 1

    if total_d == -3 or total_ad == -3 :

        return -1

    elif total_d == 3 or total_ad == 3 :

        return 1

    return 0


move_switcher = {
curses.KEY_UP : move_up ,
curses.KEY_DOWN : move_down ,
curses.KEY_LEFT : move_left ,
curses.KEY_RIGHT : move_right ,
32 : place_mark
}


def play_move ( scr = curses.initscr() ) :

    global _move_count

    scr.move ( 0 , 2 )

    while True :

        keypress = scr.getch()
        move = move_switcher.get ( keypress , empty_function )
        check_turn_end = move ( scr )

        if check_turn_end == True :

            scr.addstr ( 6 , 0 , "move no. {}".format ( _move_count ) )

            return check_win ( scr )


def check_full ( scr = curses.initscr() ) :

    for j in range ( 0 , 5 , 2 ) :

        for i in range ( 2 , 11 , 4 ) :

            if chr ( scr.inch ( j , i ) ) == " " :

                return 0

    return 1
