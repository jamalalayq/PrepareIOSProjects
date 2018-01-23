
from os import *
from datetime import *
import  io


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
            print("working directory", workingPath)
            removeFiles(workingPath)
            makeDirectories(workingPath)
            createConstantsFile(workingPath, projectName)
            createCoordinatorProtocol(path=workingPath, projectName=projectName)
        else:
            print("Invalid xcode project path.")
    except FileNotFoundError as e:
        print("Invalid xcode project path.", e)
    except Exception as e:
        print("Error occurred.", e)

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
            mkdir(path + "Models")
        except OSError:
            print("directories exist.")
    else:
        print("invalid path.")



'''Create constants file'''
def createConstantsFile(path: str, projectName: str):
    resourcesPath = path + "Resources/"
    try:
        with io.open(resourcesPath + "C.swift", mode="wb") as c:
            c_text = ''' //  C.swift
//  {0}
//  Created by GeMoOo on {1}.
//  Copyright © GeMoOo. All rights reserved.

import Foundation

struct C {{
    
    struct Keys {{
        
    }}
    
    struct Localizations {{
        
    }}
    
}}'''.format(projectName, datetime.now())
            c.write(bytes(c_text, encoding='utf8'))
    except FileNotFoundError as e:
        print(__name__, e)
    except FileExistsError as e:
        print(__name__, e)
    except Exception as e:
        print("Error occurred.", e)


''' Create coordinator protocol'''
def createCoordinatorProtocol(path: str, projectName: str):
    protocols_path = path + "Protocols/"
    try:
        with io.open(protocols_path + "Coordinator.swift", mode="wb") as file:
            text = '''
            // Coordinator.swift
            // {projectName}.
            // Created by GeMoOo on {timestamp}.
            // Copyright © GeMoOo. All rights reserved.
            
            import Foundation
            
            @ojcMembers
            protocol Coordinator {{
                optional func start() -> Void
                optional var controller: UIViewController? {{ set get }}
            }}
            '''.format(projectName=projectName, timestamp=datetime.now())
            file.write(bytes(text, encoding='utf8'))
    except FileNotFoundError as e:
        print(__name__, e)
    except FileExistsError as e:
        print(__name__, e)
    except Exception as e:
        print("Error Occurred:", e)


if __name__ == '__main__':
        main()







#/Users/gamal/Desktop/testprojct











