import os, sys, time, msvcrt

def input_with_timeout_windows(prompt, timeout, default):
    start_time = time.time()
    print (prompt)
    sys.stdout.flush()
    input = ''
    while True:
        if msvcrt.kbhit():
            chr = msvcrt.getche().decode('utf-8')
            if ord(chr) == 13: # enter_key
                break
            elif ord(chr) >= 32: #space_char
                input += chr
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break
    if len(input) > 0:
        return input
    else:
        return default

def _handle_keyboard_message():
    data = None
    #print(sys.platform)
    if sys.platform in ['linux', 'darwin']:
        import select
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            data = sys.stdin.readline().rstrip()
    elif sys.platform == 'win32':
        import msvcrt
        if msvcrt.kbhit():
            data = msvcrt.getch().decode('utf-8')
            if data == '\r':
                # Enter is pressed
                data = self.__q_kb
                self.__q_kb = ''
            else:
                print(data)
                self.__q_kb += data
                data = None
    else:
        pass
    return data


#main function
if __name__ == "__main__":
    dd = _handle_keyboard_message()
    dd = input_with_timeout_windows('>', 5, 'default')
    print(dd)
