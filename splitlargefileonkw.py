import sys
def largefilesplitonkw(filename,splitstring="DROP TABLE IF EXISTS `"):
    from pathlib import Path
    import os
    out_n = 0
    done = False
    folder = Path(filename).parent
    actualfilename = str(Path(filename).name).rsplit(".",1)[0]
    actualfilename1 = f"{actualfilename}_DB1"
    with open(filename,encoding="utf8",errors="replace") as in_file:
        while not done: #loop over output file names
            with open(os.path.join(folder,f"{actualfilename1}.txt"), "w",encoding="utf8") as out_file: #generate an output file name
                while not done: #loop over lines in inuput file and write to output file
                    try:
                        line = next(in_file).strip() #strip whitespace for consistency
                    except StopIteration:
                        done = True
                        break
                    if splitstring in line: #more robust than 'if line == "SPLIT\n":'
                        try:
                            tablename=line.replace(splitstring,"").strip(";`")
                            actualfilename1=f"{actualfilename}_{tablename}"
                        except:
                            actualfilename1 = f"{actualfilename}_{out_n}"
                        break
                    else:
                        out_file.write(line + '\n') #must add back in newline because we stripped it out earlier
                out_n += 1 #increment output file name integer

if __name__ == '__main__':
    largefilesplitonkw(sys.argv[1])
