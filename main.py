
from os import *
from datetime import *
import io
import platform


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
            createProtocols(workingPath, projectName)
            create_observer_class(workingPath, projectName)
            createLocalizableFile(workingPath, projectName)
        else:
            print("Invalid xcode project path.")
    except FileNotFoundError as e:
        print("Invalid xcode project path.", e)
    except Exception as e:
        print("Error occurred.", e)


''' Create protocols'''
def createProtocols(path: str, projectName: str):
    createCoordinatorProtocol(path=path, projectName=projectName)
    createModelProtocol(path=path, projectName=projectName)
    createViewModelProtocol(path, projectName)
    create_controller_protocol(path, projectName)
    create_notifier_protocol(path, projectName)
    create_threading_protocol(path, projectName)
    create_naming_protocol(path, projectName)


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
            mkdir(path + "Common")
            mkdir(path + "Storyboards")
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
//  Created by {2} on {1}.
//  Copyright © {2}. All rights reserved.

import Foundation

struct C {{
    
    struct Keys {{
        
    }}
    
    struct Localizations {{
        
    }}
    
}}'''.format(projectName, datetime.now(), platform.node())
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
            // Created by {platformName} on {timestamp}.
            // Copyright © {platformName}. All rights reserved.
            
            import Foundation
            import UIKit
            
            @objc
            protocol Coordinator {{
                @objc optional func start() -> Void
                @objc optional var controller: UIViewController? {{ set get }}
            }}
            '''.format(projectName=projectName, timestamp=datetime.now(), platformName=platform.node())
            file.write(bytes(text, encoding='utf8'))
    except FileNotFoundError as e:
        print(__name__, e)
    except FileExistsError as e:
        print(__name__, e)
    except Exception as e:
        print("Error Occurred:", e)


''' Create model protocol '''
def createModelProtocol(path: str, projectName: str):
    modelPath = path + "Protocols/Model.swift"
    try:
        with io.open(modelPath, mode="wb") as file:
            content = """
            // Model.swift
            // {projectName}.
            // Created by {platformName} on {timestamp}.
            // Copyright © {platformName}. All rights reserved.
                
            import Foundation
                        
            protocol Model {{
                            
            }}
            """.format(projectName=projectName, timestamp=datetime.now(), platformName=platform.node())
            file.write(bytes(content, encoding='utf8'))
    except FileExistsError as e:
        print(__name__, e)
    except FileNotFoundError as e:
        print(__name__, e)
    except Exception as e:
        print(__name__, e)


''' Create view model protocol '''
def createViewModelProtocol(path: str, projectName: str):
    view_model_file = path + "Protocols/ViewModel.swift"
    try:
        with io.open(view_model_file, mode="wb") as file:
            content = """
            // ViewModel.swift
            // {projectName}.
            // Created by {platformName} on {timestamp}.
            // Copyright © {platformName}. All rights reserved.
                
            import Foundation
                        
            protocol ViewModel {{
                            
            }}
            """.format(projectName=projectName, timestamp=datetime.now(),platformName=platform.node())
            file.write(bytes(content, "utf8"))
    except FileNotFoundError as e:
        print(__name__, e)

    except FileExistsError as e:
        print(__name__, e)

    except Exception as e:
        print(__name__, e)


''' Create controller protocol '''
def create_controller_protocol(path: str, projectName: str):
    controller_path_file = path + "Protocols/Controller.swift"
    try:
        with io.open(controller_path_file, mode="wb") as file:
            content = """
            // Controller.swift
            // {projectName}.
            // Created by {platformName} on {timestamp}.
            // Copyright © {platformName}. All rights reserved.
                
            import Foundation
            import UIKit
                        
            protocol Controller: Notifier, Threading, Naming  {{   }}
            
            extension Controller where Self: UIViewController {{
            
            
            }}
            
            
            """.format(projectName=projectName, timestamp=datetime.now(), platformName=platform.node())
            file.write(bytes(content, "utf8"))
    except FileNotFoundError as e:
        print(__name__, e)
    except FileExistsError as e:
        print(__name__, e)
    except Exception as e:
        print(__name__, e)


''' Create notifier protocol '''
def create_notifier_protocol(path: str, projectName: str):
    notifier_path_file = path + "Protocols/Notifier.swift"
    try:
        with io.open(notifier_path_file, mode="wb") as file:
            content = """
                // Notifier.swift
                // {projectName}.
                // Created by {platformName} on {timestamp}.
                // Copyright © {platformName}. All rights reserved.

                import Foundation
                import UIKit

                protocol Notifier: Threading  {{

                }}

                extension Notifier where Self: UIViewController {{
                
                    internal func notify(with message: String?, _ completed: (()->())? = nil) -> Void {{
                        runMainThread {{ [weak self] in
                            let alert = UIAlertController.init(title: "Set title", message: message ?? "", preferredStyle: .alert)
                            alert.addAction(UIAlertAction(title: "Set title", style: .cancel))
                            self?.present(alert, animated: true, completion: completed)
                        }}
                    }}
                    
                }}
                """.format(projectName=projectName, timestamp=datetime.now(), platformName=platform.node())
            file.write(bytes(content, "utf8"))
    except FileNotFoundError as e:
        print(__name__, e)
    except FileExistsError as e:
        print(__name__, e)
    except Exception as e:
        print(__name__, e)


''' Create Threading protocol '''
def create_threading_protocol(path: str, projectName: str):
    threading_path_file = path + "Protocols/Threading.swift"
    try:
        with io.open(threading_path_file, mode="wb") as file:
            content = """
                    // Threading.swift
                    // {projectName}.
                    // Created by {platformName} on {timestamp}.
                    // Copyright © {platformName}. All rights reserved.

                    import Foundation

                    protocol Threading  {{

                    }}

                    extension Threading {{

                        internal func runMainThread(_ execuation: @escaping ()->()) -> Void {{
                            DispatchQueue.main.async(execute: execuation)
                        }}
    
                        internal func runThread(qos: DispatchQoS.QoSClass, _ execuation: @escaping ()->()) -> Void {{
                            DispatchQueue.global(qos: qos).async(execute: execuation)
                        }}

                    }}
                    """.format(projectName=projectName, timestamp=datetime.now(), platformName=platform.node())
            file.write(bytes(content, "utf8"))
    except FileNotFoundError as e:
        print(__name__, e)
    except FileExistsError as e:
        print(__name__, e)
    except Exception as e:
        print(__name__, e)


''' Create naming protocol '''
def create_naming_protocol(path: str, project_name: str):
    naming_file_path = path + "Protocols/Naming.swift"
    try:
        with io.open(naming_file_path, mode="wb") as file:
            content = """
            //  Naming.swift
            //  {project_name}
            //  Created by {platformName} on {timestamp}.
            //  Copyright © {platformName}. All rights reserved.
            
            
            import Foundation
                        
            
            protocol Naming {{ }}
            
            internal extension Naming {{
                
                internal func name(of anyClass: AnyClass) -> String {{
                    return String.init(describing: anyClass.self)
                }}
                
            }}



            """.format(project_name=project_name, timestamp=datetime.now(), platformName=platform.node())
            file.write(bytes(content, "utf8"))
    except FileExistsError as e:
        print(__name__, e)
    except FileNotFoundError as e:
        print(__name__, e)
    except Exception as e:
        print(__name__, e)


''' Create observer class '''
def create_observer_class(path: str, projectName: str):
    observer_file_path = path + "Resources/Observer.swift"
    try:
        with io.open(observer_file_path, mode="wb") as file:
            content = """
                //  Observer.swift
                //  {projectName}
                //  Created by {platformName} on {timestamp}.
                //  Copyright © {platformName}. All rights reserved.
                
                import Foundation
                
                
                internal final class Observer<Variable> {{
                    
                    
                    typealias Listener = (Variable?)->()
                    
                    private var listener: Listener?
                    
                    internal var value: Variable? {{
                        didSet {{
                            if value != nil {{
                                DispatchQueue.global(qos: .userInitiated).async {{ [weak self] in
                                    self?.listener?(self?.value)
                                }}                                
                                print("\(value.customMirror.subjectType) 💡.")
                            }}
                        }}
                    }}
                    
                    init() {{
                        print("\(value.customMirror.subjectType) initialized 🚀.")
                    }}
                    
                    internal func bind(_ listener: Listener?) -> Void {{
                        DispatchQueue.global(qos: .userInitiated).async {{ [weak self] in
                            self?.listener = listener
                            if self?.value != nil {{
                                listener?(self?.value)
                            }}
                        }}
                    }}
                    
                    deinit {{
                        print("\(value.customMirror.subjectType) 💀.")
                    }}
                    
                    
                }}
                
            """.format(projectName=projectName, timestamp=datetime.now(), platformName=platform.node())
            file.write(bytes(content, "utf8"))
    except FileNotFoundError as e:
        print(__name__, e)
    except FileExistsError as e:
        print(__name__, e)
    except Exception as e:
        print(__name__, e)


''' Create localizable file '''
def createLocalizableFile(path: str, projectName: str):
    localizable_file_path = path + "Resources/Localizable.strings"
    try:
        with io.open(localizable_file_path, mode="wb") as file:
            content = """
                   /*  Localizable.strings
                       {projectName}
                       Created by {platformName} on {timestamp}.
                       Copyright © {platformName}. All rights reserved.
                    */


               """.format(projectName=projectName, timestamp=datetime.now(), platformName=platform.node())
            file.write(bytes(content, "utf8"))
    except FileNotFoundError as e:
        print(__name__, e)
    except FileExistsError as e:
        print(__name__, e)
    except Exception as e:
        print(__name__, e)


''' Create localizer file '''
def create_localizer_class(path: str, project_name: str):
    file_path = path + "Common/Localizer.swift"
    try:
        with io.open(file_path, mode="wb") as file:
            content = """
                    //  Localizer.swift
                    //  {projectName}
                    //  Created by {platformName} on {timestamp}.
                    //  Copyright © {platformName}. All rights reserved.
                    
                    import Foundation
                    
                                        
                    // MARK:-  Constants
                    private let DefaultLanguageSign = "default.language.ia"
                    
                    internal final class Localizer: NSObject {{
                        
                        private static let defaultSign = Bundle.main.preferredLocalizations[0]
                        
                        /**
                         Get available languages from main bundle
                         - returns: array of languages signs
                         */
                        internal class func getSelectedLanguages() -> Array<String> {{
                            var languages = Bundle.main.localizations
                            if let base = languages.index(of: "Base") {{
                                languages.remove(at: base)
                            }}
                            return languages
                        }}
                        
                        /**
                         Get default language or saved language
                         - returns: language sign string
                         */
                        internal static var current: String {{
                            return UserDefaults.standard.string(forKey: DefaultLanguageSign) ?? defaultSign
                        }}
                        
                        /**
                         Save language and put it default
                         - parameter language: may be language sign to save it
                         - returns: void
                         */
                        internal class func set(language: String) -> Void {{
                            let lang = getSelectedLanguages().contains(language) ? language : defaultSign
                            guard (lang != current) else {{ return }}
                            UserDefaults.standard.set(lang, forKey: DefaultLanguageSign)
                            UserDefaults.standard.synchronize()
                            NotificationCenter.default.post(name: .LanguageDidChanged, object: nil)
                        }}
                        
                    }}
                    
                    
                    // MARK:-  Notifications.Name
                    internal extension Notification.Name {{
                        internal static var LanguageDidChanged: Notification.Name {{
                            return Notification.Name("language.did.changed.ia")
                        }}
                    }}
                    
                    
                    // MARK:-  Strings
                    internal extension String {{
                        
                        /// get localize string for key from localizable files
                        internal var localized: String {{
                            guard let languageStringsFilePath = Bundle.main.path(forResource: Localizer.current, ofType: "lproj") else {{
                                return Bundle.main.localizedString(forKey: self, value: nil, table: nil) 
                             }}
                            return Bundle(path: languageStringsFilePath)?.localizedString(forKey: self, value: nil, table: nil) ?? self
                        }}
                    }}
                    
                    



            """.format(projectName=project_name, timestamp=datetime.now(), platformName=platform.node())
            file.write(bytes(content, "utf8"))

    except FileExistsError as e:
        print(__name__, e)
    except FileNotFoundError as e:
        print(__name__, e)
    except Exception as e:
        print(__name__, e)





if __name__ == '__main__':
        main()







#/Users/gamal/Desktop/testprojct











