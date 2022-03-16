import os
import sys

def parse_filename(filename):
    datetime = filename.split('.')[1]
    date = datetime.split('-')
    year = '20'+ date[0]
    month = date[1]
    day = date[2][:2]
    return '%s/%s/%s/' % (year,month,day)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: %s <source directory path> <destination directory path>" % sys.argv[0])
        exit(1)
    else:
        source_path = sys.argv[1]
        dest_path = sys.argv[2]
        if not os.path.isdir(dest_path):
            os.makedirs(dest_path)
        files = os.listdir(source_path)
        for file in files:
            if file.endswith('.avi'):
                print(file)
                path = dest_path + '/' + parse_filename(file)
                if not os.path.isdir(path):
                    os.makedirs(path)
            
                os.rename(source_path + '/' + file,path + file)
        exit()