# hiding implimentation details and showing essential features

from abc import ABC,abstractmethod

class Editor(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod

    def exexute(self):
        pass


    @abstractmethod
    def debug(self):
        pass


class vscode(Editor):
    def open(self):
        print("vscode open using code")

    def exexute(self):
        print("vscode exexute")

    def debug(self):
        print("vscode deebug method") 


vscode_instance=vscode()

vscode_instance.open()