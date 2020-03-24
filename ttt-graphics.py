import curses


def draw_screen ( scr = curses.initscr() ) :

    scr.addstr ( 0 , 0 , "    |   |" )      #coordinates 0 , 2 ; 0 , 6 ; 0 , 10
    scr.addstr ( 1 , 0 , "-------------" )
    scr.addstr ( 2 , 0 , "    |   |" )      #coordinates 2 , 2 ; 2 , 6 ; 2 , 10
    scr.addstr ( 3 , 0 , "-------------" )
    scr.addstr ( 4 , 0 , "    |   |" )      #coordinates 4 , 2 ; 4 , 6 ; 4 , 10

    scr.refresh()



class movement :

    @staticmethod
    def move_up ( scr = curses.initscr() ) :

        [ y , x ] = scr.getyx ( y , x )

        if y != 0 :
            y = y - 2

        scr.move ( y , x )
        scr.refresh()


    @staticmethod
    def move_down ( scr = curses.initscr() ) :

        [ y , x ] = scr.getyx()

        if y != 4 :
            y = y + 2

        scr.move ( y , x )
        scr.refresh()


    @staticmethod
    def move_left ( scr = curses.initscr() ) :

        [ y , x ] = scr.getyx()

        if x != 2 :
            x = x - 4

        scr.move ( y , x )
        scr.refresh()


    @staticmethod
    def move_right ( scr = curses.initscr() ) :

        [ y , x ] = scr.getyx()

        if x != 10 :
            x = x + 4

        scr.move ( y , x )
        scr.refresh()


    @staticmethod
    def empty_function ( *args ) :
        pass


    switcher = {
    curses.KEY_UP : move_up.__func__ ,
    curses.KEY_DOWN : move_down.__func__ ,
    curses.KEY_LEFT : move_left.__func__ ,
    curses.KEY_RIGHT : move_right.__func__
    }



def cursor_movement ( scr = curses.initscr() ) :

    keypress = scr.getch()

    move = movement.switcher.get ( keypress , movement.empty_function )

    move ( scr )

    scr.refresh()



def main ( stdscr ) :

    draw_screen ( stdscr )
    stdscr.move ( 0 , 2 )
    cursor_movement ( stdscr )
    cursor_movement ( stdscr )
    cursor_movement ( stdscr )
    cursor_movement ( stdscr )



if __name__ == "__main__":

    curses.wrapper ( main )
