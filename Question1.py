path="C:\\PythonFiles\\Question1.txt"
fopen=open(path, "a+")
fopen.write("derave1577\n")
fopen.flush()
fopen.seek(0)
for line in fopen:
    print(line)
fopen.close
