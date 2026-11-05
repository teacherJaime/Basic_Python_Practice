#Morse code translator
def morse_to_text(morse_code):
    morse_dict = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
        "--..": "Z"
    }
    
    # Divides the string by spaces (' ') in a list of Morse symbols
    morse_symbols = morse_code.strip().split(" ")
    
    translated_letters = []
    for symbol in morse_symbols:
        # Ignores extra spaces in between
        if symbol == "":
            continue
            
        letter = morse_dict.get(symbol)
        if letter:
            translated_letters.append(letter)
        else:
            translated_letters.append("?")  #Or a mark for unknown characters
            
    # Joins all the translated letters into a single word
    return "".join(translated_letters)

while True:
    code = input("Insert your Morse code (separate each letter with a space): ")
    if code.lower() == "exit":
        break
        
    result = morse_to_text(code)
    print(f"Code word: {result}\n")