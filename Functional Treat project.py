data = []
while True:    
    print("Welcome to Functional Treat Analyzer and Transformer")
    print("1. user input data")
    print("2. data summary")
    print("3. lambda function")
    print("4. sort data")
    print("5. *args function")
    print("6. **kwargs function")
    print("7. exit")   

    choice = int(input("Enter your choice: "))
    
    if choice == 1:

        def user_input():
            """User Input Data"""
            print(user_input.__doc__)
            global data
            values = input("Enter numbers: ")
            data = list(map(int,values.split()))
            print("Data stored successfully: ")

        user_input()

    elif choice == 2:

        def data_summary():
            """Data Summary"""
            print(data_summary.__doc__)
            if not data:
                print("not found data!")
                return
            print("Total values: ", len(data))
            print("Maximum values: ", max(data))
            print("Minimum values: ", min(data))
            print("sum :", sum(data))
            print("Average :", sum(data) / len(data))

        data_summary()

    elif choice == 3:

        def filter_data():
            """Filter Data"""
            print(filter_data.__doc__)
            if not data:
                print("not data found!")
                return
            
            item = int(input("Enter threshlode value: "))
            result = list(filter(lambda x: x > item, data))
            print("Filtered data:", result)

        filter_data()

    elif choice == 4:

        def sort_data():
            """Sort Data"""
            print(sort_data.__doc__)
            if not data:
                print("not found data")
                return
            
            data.sort()
            print("sorted data:", data)

        sort_data()

    elif choice == 5:

        def args_function():
            """Args Function"""
            print(args_function.__doc__)

        values = input("Enter numbers: ")
        numbers = list(map(int, values.split()))
       
        def total_values(*args):
            return sum(args)

        print("Total:", total_values(*numbers))

    elif choice == 6:

        def kwargs_function():
            """kwargs Example"""
            print(kwargs_function.__doc__)

        def show_info(**kwargs):
            for key , value in kwargs.items():
                print(key, ":", value)

        name = input("name: ")
        course = input("course: ")
        project = input("project: ")

        show_info(name=name, course=course, project=project)
        
    elif choice == 7:
        print("Exit")
        print("Thank you to use my project.")
        print("Have nice day.")
        break

    else:
        print("Invalid choice!")


    































