import time

try:
    plat = 'osx'
    import win32con, win32api
    plat = 'win'
except:
    pass

def _down(x, y):
    if plat == 'win':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(x), int(y))
    
def _up(x, y):
    if plat == 'win':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int(x), int(y))
    
def click(x, y, delay=0.05):
    print "CLICK x: %s y: %s" % (x, y)
    _down(x, y)
    time.sleep(delay)
    _up(x, y)

def move(x, y):
    print "Move x: %s y: %s" % (x, y)
    if plat == 'win':
        win32api.SetCursorPos((int(x), int(y)))
    
if __name__ == '__main__':
    print "Demo:"
    move(50, 50)
    click(50, 50)
    time.sleep(2)
    move(300, 100)
    click(300, 100)
    