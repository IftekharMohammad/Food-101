import os 

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    for filename in os.listdir(dir_path):
        i = 0
        if filename.endswith(".py"):
            continue
        for files in os.listdir(filename):
            if files.endswith(".py"):
                continue
            else:
                dst = filename + "(" + str(i) + ").jpg"
                src = dir_path + "/" + filename + "/" + files
                dst = dir_path + "/" + filename + "/" + dst
                print("From: {src}".format(src=src))
                print("To: {dst}".format(dst=dst))
                os.rename(src, dst)
                i += 1


if __name__ == '__main__': 
    main()