import numpy as np

class DataAnalytics:

    # Constructor
    def __init__(self):
        self.__array = np.array([])

    # Getter Method
    def get_array(self):
        return self.__array

    # Setter Method
    def set_array(self, arr):
        self.__array = arr

    # Class Method
    @classmethod
    def project_info(cls):
        print("\n====================================")
        print("        NUMPY ANALYZER")
        print("====================================")

    # Static Method
    @staticmethod
    def welcome_message():
        print("Welcome to NumPy Analyzer Project")

    # Private Method
    def __show_message(self):
        print("\nArray Created Successfully.")

    # Array Creation
    def create_array(self):

        print("\n----- Create Array -----")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter Choice : ")

        if choice == "1":

            n = int(input("Enter Number of Elements : "))
            data = []

            for i in range(n):
                value = float(input("Enter Element : "))
                data.append(value)

            self.__array = np.array(data)

        elif choice == "2":

            row = int(input("Enter Rows : "))
            col = int(input("Enter Columns : "))

            data = []

            for i in range(row):

                temp = []

                for j in range(col):

                    value = float(input("Enter Element : "))
                    temp.append(value)

                data.append(temp)

            self.__array = np.array(data)

        elif choice == "3":

            depth = int(input("Enter Depth : "))
            row = int(input("Enter Rows : "))
            col = int(input("Enter Columns : "))

            data = []

            for i in range(depth):

                layer = []

                for j in range(row):

                    temp = []

                    for k in range(col):

                        value = float(input("Enter Element : "))
                        temp.append(value)

                    layer.append(temp)

                data.append(layer)

            self.__array = np.array(data)

        else:
            print("Invalid Choice")
            return

        self.__show_message()

        print("\nArray is :")
        print(self.__array)
            # Indexing and Slicing
    def indexing_slicing(self):

        if self.__array.size == 0:
            print("Please Create Array First.")
            return

        print("\n1. Indexing")
        print("2. Slicing")

        choice = input("Enter Choice : ")

        if choice == "1":

            if self.__array.ndim == 1:

                index = int(input("Enter Index : "))
                print("Element :", self.__array[index])

            elif self.__array.ndim == 2:

                row = int(input("Enter Row Index : "))
                col = int(input("Enter Column Index : "))
                print("Element :", self.__array[row][col])

            elif self.__array.ndim == 3:

                depth = int(input("Enter Depth : "))
                row = int(input("Enter Row : "))
                col = int(input("Enter Column : "))
                print("Element :", self.__array[depth][row][col])

        elif choice == "2":

            if self.__array.ndim == 1:

                start = int(input("Enter Start Index : "))
                end = int(input("Enter End Index : "))
                print(self.__array[start:end])

            elif self.__array.ndim == 2:

                rs = int(input("Row Start : "))
                re = int(input("Row End : "))
                cs = int(input("Column Start : "))
                ce = int(input("Column End : "))

                print(self.__array[rs:re, cs:ce])

            else:
                print("Slicing for 3D Array is not implemented.")

        else:
            print("Invalid Choice")


    # Mathematical Operations
    def mathematical_operations(self):

        if self.__array.size == 0:
            print("Please Create Array First.")
            return

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = input("Enter Choice : ")

        rows = len(self.__array)
        cols = len(self.__array[0])

        data = []

        if choice in ["1","2","3","4"]:

            print("\nEnter Second Matrix")

            for i in range(rows):

                temp = []

                for j in range(cols):

                    value = float(input("Enter Element : "))
                    temp.append(value)

                data.append(temp)

            second = np.array(data)

            if choice == "1":
                print(self.__array + second)

            elif choice == "2":
                print(self.__array - second)

            elif choice == "3":
                print(self.__array * second)

            elif choice == "4":
                print(self.__array / second)

        elif choice == "5":

            print("\nEnter Second Matrix")

            for i in range(rows):

                temp = []

                for j in range(cols):

                    value = float(input("Enter Element : "))
                    temp.append(value)

                data.append(temp)

            second = np.array(data)

            print(np.dot(self.__array, second))

        elif choice == "6":

            c = int(input("Enter Columns of Second Matrix : "))

            data = []

            for i in range(cols):

                temp = []

                for j in range(c):

                    value = float(input("Enter Element : "))
                    temp.append(value)

                data.append(temp)

            second = np.array(data)

            print(np.matmul(self.__array, second))

        else:
            print("Invalid Choice")
            # Combine and Split Arrays
    def combine_or_split(self):

        if self.__array.size == 0:
            print("Please Create Array First.")
            return

        print("\n1. Combine Arrays")
        print("2. Split Array")

        choice = input("Enter Choice : ")

        if choice == "1":

            rows = len(self.__array)
            cols = len(self.__array[0])

            data = []

            print("\nEnter Second Matrix")

            for i in range(rows):

                temp = []

                for j in range(cols):

                    value = float(input("Enter Element : "))
                    temp.append(value)

                data.append(temp)

            second = np.array(data)

            print("\nCombined Array")
            print(np.vstack((self.__array, second)))

        elif choice == "2":

            part = int(input("Enter Number of Parts : "))

            result = np.array_split(self.__array, part)

            print("\nSplit Array")

            for i in range(len(result)):
                print("Part", i + 1)
                print(result[i])

        else:
            print("Invalid Choice")


    # Search, Sort and Filter
    def search_sort_filter(self):

        if self.__array.size == 0:
            print("Please Create Array First.")
            return

        print("\n1. Search")
        print("2. Sort")
        print("3. Filter")

        choice = input("Enter Choice : ")

        if choice == "1":

            value = float(input("Enter Value : "))

            index = np.where(self.__array == value)

            print("Position :", index)

        elif choice == "2":

            print("\n1. Ascending")
            print("2. Descending")

            order = input("Enter Choice : ")

            if order == "1":

                print(np.sort(self.__array))

            elif order == "2":

                print(np.sort(self.__array)[::-1])

            else:

                print("Invalid Choice")

        elif choice == "3":

            value = float(input("Show Elements Greater Than : "))

            print(self.__array[self.__array > value])

        else:

            print("Invalid Choice")
            # Statistics
    def compute_aggregates_statistics(self):

        if self.__array.size == 0:
            print("Please Create Array First.")
            return

        print("\n1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation Coefficient")

        choice = input("Enter Choice : ")

        if choice == "1":
            print("Sum :", np.sum(self.__array))

        elif choice == "2":
            print("Mean :", np.mean(self.__array))

        elif choice == "3":
            print("Median :", np.median(self.__array))

        elif choice == "4":
            print("Standard Deviation :", np.std(self.__array))

        elif choice == "5":
            print("Variance :", np.var(self.__array))

        elif choice == "6":
            print("Minimum :", np.min(self.__array))

        elif choice == "7":
            print("Maximum :", np.max(self.__array))

        elif choice == "8":

            p = int(input("Enter Percentile : "))
            print(np.percentile(self.__array, p))

        elif choice == "9":

            print("Enter Second Array")

            data = []

            for i in range(self.__array.size):

                value = float(input("Enter Element : "))
                data.append(value)

            second = np.array(data)

            first = self.__array.reshape(self.__array.size)

            print(np.corrcoef(first, second))

        else:
            print("Invalid Choice")


    @classmethod
    def project_info(cls):
        print("\nProject : NumPy Analyzer")


    @staticmethod
    def welcome_message():
        print("Welcome to NumPy Analyzer")
def main():

    obj = DataAnalytics()

    DataAnalytics.project_info()
    DataAnalytics.welcome_message()

    while True:

        print("\n========== MENU ==========")
        print("1. Create Array")
        print("2. Indexing and Slicing")
        print("3. Mathematical Operations")
        print("4. Combine / Split")
        print("5. Search / Sort / Filter")
        print("6. Statistics")
        print("7. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            obj.create_array()

        elif choice == "2":
            obj.indexing_slicing()

        elif choice == "3":
            obj.mathematical_operations()

        elif choice == "4":
            obj.combine_or_split()

        elif choice == "5":
            obj.search_sort_filter()

        elif choice == "6":
            obj.compute_aggregates_statistics()

        elif choice == "7":
            print("\nThank You")
            break

        else:
            print("Invalid Choice")



        
