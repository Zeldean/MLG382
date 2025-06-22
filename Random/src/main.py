from housing_market import housing_market

def main(): 
    try:
        choice = 1
        if choice == 1:
            housing_market.run()
        elif choice == 2:
            script2.run()
        elif choice == 3:
            script3.run()
        else:
            print("Invalid choice. Please select a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()