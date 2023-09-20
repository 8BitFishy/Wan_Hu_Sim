
class Logger():
    def __init__(self, filename):

        self.file = filename
        self.logs = []


    def Clear_Log_File(self):
        with open(self.file, "w") as file:
            file.close()
 

    def Write_To_File(self):

        with open(self.file, "a") as file:
            for i in range(len(self.logs)):
                file.write(f"{self.logs[i]}")
                file.write(f"\n")

        file.close()

    def Write_To_Log(self, message):
        self.logs.append(message)

    def Clear_Logs(self):
        self.logs = []


def Generate_Logger(filename):
    logger = Logger(filename)
    logger.Clear_Log_File()

    return logger