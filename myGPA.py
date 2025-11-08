
import os

class myGPA:
    def __init__(self):
        # File name
        self.fileName = "myGPA.csv"

        # Text default content
        self.fileDefaultContent     = "Course Code, Score, Credit, GPA\n"
        self.defaultText_courseCode = "Enter course code: (Number Only) "
        self.defaultText_score      = "Enter the overall score of the course: "
        self.defaultText_credit     = "Enter the course credit: (Default: 10) "

        # Initialise the file
        if not os.path.isfile(self.fileName) or os.path.getsize(self.fileName) == 0:
            with open(self.fileName, "w") as f:
                f.write(self.fileDefaultContent)

    def showList(self, printResult=True):
        # Show all list
        # printResult is True then print, or return list
        with open(self.fileName, "r") as f:
            try:
                if printResult:
                    for line in f:
                        print(line, end="")
                else:
                    # Jump to second line
                    next(f)

                    return f.readlines()

            except StopIteration:
                print("The gpa file is empty!")

    def countGPA(self):
        # Only count GPA
        allLines    = self.showList(printResult=False)
        totalScore  = 0
        totalCredit = 0

        if allLines:
            for line in allLines:
                item = line.strip().split(",")
                totalScore  += float(item[2]) * float(item[3])
                totalCredit += float(item[2])

            finalGPA = totalScore / totalCredit

            print(f"Your current GPA is {finalGPA:.1f}/7.0")
        else:
            print("Your record is empty!")
        
    def add(self):
        # Add course, score and credit
        courseCode  = int(input(self.defaultText_courseCode))
        score       = input(self.defaultText_score) or 0
        credit      = input(self.defaultText_credit) or 10

        confirm = input(f"Are you sure you want to add a course code named \"{courseCode}\"? (y/n) ")

        if confirm == "y":
            # Determined if the same course code exists
            is_exists = False
            allLines = self.showList(printResult=False)
            for line in allLines:
                if line.startswith(str(courseCode)):
                    is_exists = True
                    break

            if is_exists:
                print(f"The course code \"{courseCode}\" exists. Please check the list by command \"list\"")
            else:
                row = self.recordFormat(courseCode, score, credit)

                with open(self.fileName, "a") as f:
                    f.writelines(row)

    def update(self):
        # Update the score of a course
        courseCode  = int(input(self.defaultText_courseCode))
        score       = input(self.defaultText_score) or 0
        credit      = input(self.defaultText_credit) or 10

        confirm = input(f"Are you sure you want to update the course code named \"{courseCode}\"? (y/n) ")

        if confirm == "y":
            # Read file
            allLines = self.showList(printResult=False)
            
            # Clear file
            self.clear(confirm="y")

            is_exists = False
            with open(self.fileName, "a") as f:
                for line in allLines:
                    if line.startswith(str(courseCode)):
                        row = self.recordFormat(courseCode, score, credit)
                        is_exists = True

                        f.writelines(row)
                    else:
                        f.writelines(line)

            if not is_exists:
                print(f"The couse code named \"{courseCode}\" is not exists.")
    
    def remove(self):
        # Remove course and score
        courseCode = int(input(self.defaultText_courseCode))

        confirm = input(f"Are you sure you want to delete the course code named \"{courseCode}\"? (y/n) ")

        if confirm == "y":
            # Read file
            allLines = self.showList(printResult=False)
            
            # Clear file
            self.clear(confirm="y")

            with open(self.fileName, "a") as f:
                for line in allLines:
                    if not line.startswith(str(courseCode)):
                        f.writelines(line)

    def clear(self, confirm="n"):
        # Clear all file
        if confirm == "n":
            confirm = input("Are you sure you want to clear all records? (y/n) ")

        if confirm == "y":
            with open(self.fileName, "w") as f:
                f.write(self.fileDefaultContent)

    def verifyGPA(self, score):
        # Determine GPA by score
        score = int(score)

        if 85 <= score:
            return 7.0
        elif 75 <= score <= 84:
            return 6.0
        elif 65 <= score <= 74:
            return 5.0
        elif 50 <= score <= 64:
            return 4.0
        elif 46 <= score <= 49:
            return 3.0
        elif 30 <= score <= 45:
            return 2.0
        elif score <= 29:
            return 1.0
        
    def recordFormat(self, courseCode, score=0, credit=0):
        # Record format
        singleGPA = self.verifyGPA(score)

        return f"{courseCode},{score},{credit},{singleGPA}\n" 
    
    @staticmethod
    def help():
        print(
            "listed Commands and descriptions below:",
            "   add: Create a new record with course code, score and credit.",
            "   update: Update a course data by course code once.",
            "   remove: Delete the course data by course code.",
            "   list: Show all records.",
            "   gpa: Counting GPA by current records.",
            "   clear: Clear all records.",
            sep="\n"
        )

def main():
    req_text = "Enter a request: "

    print("Enter \"help\" for more information.")
    req = input(req_text)

    gpa = myGPA()
    while req != "q" and req != "quit" and req!="quit()":
        match req:
            case "list":
                gpa.showList()
            case "gpa":
                gpa.countGPA()
            case "add":
                gpa.add()
            case "update":
                gpa.update()
            case "remove":
                gpa.remove()
            case "clear":
                gpa.clear()
            case "help":
                gpa.help()

        req = input(req_text)

if __name__ == "__main__":
    main()
