import curses

def draw_screen ( scr = curses.initscr() ) :

    scr.addstr ( 0 , 0 , "    |   |" )      #coordinates 0 , 2 ; 0 , 6 ; 0 , 10
    scr.addstr ( 1 , 0 , "-------------" )
    scr.addstr ( 2 , 0 , "    |   |" )      #coordinates 2 , 2 ; 2 , 6 ; 2 , 10
    scr.addstr ( 3 , 0 , "-------------" )
    scr.addstr ( 4 , 0 , "    |   |" )      #coordinates 4 , 2 ; 4 , 6 ; 4 , 10

    scr.move ( 0 , 2 )

    scr.refresh()
