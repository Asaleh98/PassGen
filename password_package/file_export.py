class Export:

    def export_file(self, result):
        self.results = result

        export_file = input("Would you like to export results to a text file? y/n: ")
        export_file = export_file.lower()

        if export_file == "y":
            file = open("result.txt", "a+")
            data = file.write('\n' + result + '\n')
            file.close()
            print("Results successfuly exported to a text file")
        elif export_file == "n":
            pass
