import os, re, PIL, sys, getopt, shutil

def main(argv):
    inputfolder = ''
    outputfolder = ''
    try:
        opts, args = getopt.getopt(argv, 'hf:')
    except getopt.GetoptError:
        print 'imageextractor.py -f <rootfolder>'
    for opt, arg in opts:
        if opt == '-h':
            print 'imageextractor.py -f <rootfolder>'
            sys.exit()
        elif opt == '-f':
            inputfolder = arg

    if os.path.isdir(inputfolder):
        files = []
        for root, dirs, fname, in os.walk(inputfolder):
            for _file in fname:
                files.append(os.path.join(root, _file))
        
    else:
        print 'This is not a valid directory, try again?'


if __name__ == '__main__':
    main(sys.argv[1:])
