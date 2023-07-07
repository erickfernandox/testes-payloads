import argparse

def format_parameters(lst):
    params = []
    line = ""
    for item in lst:
        param = f"{item}=FUZZ"
        if len(param) > 20:
            params.append(line)
            line = ""
        if line:
            line += "&"
        line += param
    if line:
        params.append(line)
    return params

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listfile", help="File containing the list", required=True)
    args = parser.parse_args()

    with open(args.listfile, "r") as file:
        lst = file.read().splitlines()

    params = format_parameters(lst)
    for param in params:
        print(f"?{param}")

if __name__ == "__main__":
    main()
