from mood_response import mood_happy,mood_angry,mood_calm,mood_sad

def main():
    mood = input("Enter your mood: (happy,sad,angry,calm) ").lower()
    try:
        if mood == "happy":
            print(mood_happy())
        elif mood == "Sad":
            print(mood_sad())
        elif mood == "angry":
            print(mood_angry())
        elif mood == "calm":
            print(mood_calm())
    except ValueError:
        print("Wrong input Try Again")
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()

