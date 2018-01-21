
from os import *


'''
.xcodeproj
/Users/gamal/Desktop/testprojct
'''


def main():
    path = input("Please enter xcode project path:")
    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/"):
        path = path + "/"
    pathComponents = path.split("/")
    projectName = pathComponents[-2]
    try:
        phomeDirFiles = listdir(path)
        xcodeFile = projectName + ".xcodeproj"
        if xcodeFile in phomeDirFiles:
            workingPath = path + projectName + "/"
            print("workig directory", workingPath)
            removeFiles(workingPath)
            makeDirectories(workingPath)
        else:
            print("Invalid xcode project path.")
    except FileNotFoundError:
        print("Invalid xcode project path.", FileNotFoundError)
    except Exception:
        print("Error occured.", Exception)

''' Remove unownted files '''
def removeFiles(path: str):
    if type(path) == str:
        try:
            remove(path + "ViewController.swift")
        except FileExistsError:
            print("File removed in advance.", FileExistsError)
        except FileNotFoundError:
            print("File removed in advance.", FileNotFoundError)
        except Exception:
            print("Error occured", Exception)
    else:
        print("invalid path.")


''' Create directories '''
def makeDirectories(path: str):
    if type(path) == str:
        try:
            mkdir(path + "Cells")
            mkdir(path + "Cells/Controllers")
            mkdir(path + "Cells/Scenes")
            mkdir(path + "Modules")
            mkdir(path + "Modules/Home")
            mkdir(path + "Resources")
            mkdir(path + "Extensions")
            mkdir(path + "Protocols")
        except OSError:
            print("directories exist.")
    else:
        print("invalid path.")




if __name__ == '__main__':
        main()
