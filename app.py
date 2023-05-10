import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import os


# Function to run Huffman Coding C++ Script
def runHuffman(args,function) -> str:
    '''Runs the Huffman Code program for the given function'''
    print(args)
    if function == 'Run':
        command = ['.\\HuffmanCoding.exe',str(args).strip()]
        
    result = subprocess.run(command,stdout=subprocess.PIPE,check=True)
    output = result.stdout.decode().strip()
    
    print(output)
    
    return output
 
    
# Function to create Output Window

def createOutputWindow(OutputVal) -> None:
    '''Displays the output on different Window'''
    outputWindow = tk.Toplevel()
    outputWindow.title('Output')
    outputWindow.geometry("500x500")
    outputText = scrolledtext.ScrolledText(outputWindow,wrap=tk.WORD,width=60,height=25)
    outputText.pack(fill=tk.BOTH,expand=True)
    outputText.insert(tk.END,OutputVal)
    



def runGUI() -> None:
    # create the main window
    root = tk.Tk()

    # set the window title
    root.title("Huffman Coding")

    # set the window dimensions
    root.geometry("400x300")


    # Frames
    inputFrame = tk.Frame(root)
    inputFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=False)

    buttonFrame = tk.Frame(root,padx=20,pady=20)
    buttonFrame.pack(fill=tk.BOTH,expand=True)


    # Widget

    # Widget for inputFrame
    inputLabel = tk.Label(inputFrame, text="Enter Text")
    inputLabel.pack(side=tk.TOP)
    inputEntry = tk.Text(inputFrame,width=30,height=2,xscrollcommand=True)
    inputEntry.pack(side=tk.TOP,padx=5,pady=5)

        
    # Button Commands
    def runButtonCommand() -> None:
        inputText = inputEntry.get("1.0", "end-1c")
        encodedOutput = runHuffman(inputText,"Run")
        createOutputWindow(encodedOutput)
        
    def quitButtonCommand() -> None:
        root.destroy()
        
    # Buttons to buttonFrame
    runButton = ttk.Button(buttonFrame,text='Run',command=runButtonCommand)
    runButton.pack(side=tk.LEFT,padx=10)

    quitButton = ttk.Button(buttonFrame,text='Quit',command=quitButtonCommand)
    quitButton.pack(side=tk.RIGHT,padx=10)


    # run the main event loop
    root.mainloop()


if __name__ == "__main__":
    os.system("g++ HuffmanCoding.cpp -o HuffmanCoding.exe")
    runGUI()
