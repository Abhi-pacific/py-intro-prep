nemo = 'nemo'

def findnemo(array) -> None:
    for _ in range(len(array)):
        if array[_] == nemo:
            print('found')
    #using list comprehension
    print(['found nemo' for _ in range(len(array)) if array[_] == nemo ])
def main():
    if __name__ == "__main__":
        ar = ['Abhishek','Chauhan','Aditya','Chauhan','Naveen','nemo']
        findnemo(ar)
main()