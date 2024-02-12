

def startGUI():
    import GUI as G
    G.main()
    


# CLI version
def start():
    import data
    import CLI_GUI
    obj = data.INFO()
    while (True):
        choice = CLI_GUI.main()
        if (choice == 1):
            file_name = CLI_GUI.solveFromFile()
            if (file_name):
                obj.parse(file_name)
                obj.print()
                input("Press Enter to continue...")
                res = obj.solve()
                CLI_GUI.printResult(res, obj.matrix, obj.time_executed)
                input("Press Enter to continue...")
        elif (choice == 2):
            obj.random(*CLI_GUI.solveFromInput())
            obj.print()
            input("Press Enter to continue...")
            res = obj.solve()
            CLI_GUI.printResult(res, obj.matrix, obj.time_executed)
            input("Press Enter to continue...")
        obj.reset()


if __name__ == "__main__":
    startGUI()