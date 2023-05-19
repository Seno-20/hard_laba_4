import pandas as pd
import re
import csv

"""

input_file = open("import_1.txt", "r")
output_file = open("output12121щ.txt", "w")
line = input_file.readlines()

while (
    line
    != "[NAME][100][1]	[COMMENT][211][1]	[TYPE][101][1]	[LENGTH][105][1]	[FORMAT][106][1]	[CONNECTION][102][1]	[GROUP][104][1]	[ADDRPARAMS][108][1]	[SCALEVALID][112][2]	[SCALEPARAM1][113][1]	[SCALEPARAM2][114][1]	[SCALEPARAM3][115][1]	[SCALEPARAM4][116][1]	[MINLIMIT][117][1]	[MAXLIMIT][118][1]	[STARTVALUE][119][1]	[SUBSTVALUE][120][1]	[SUBSTVALUE_ON_MINLIMIT][121][2]	[SUBSTVALUE_ON_MAXLIMIT][122][2]	[SUBSTVALUE_AS_STARTVALUE][123][2]	[SUBSTVALUE_ON_ERROR][124][2]	[UPDATEMODE][111][2]	[SYNCHRONIZATION][125][2]	[RUNTIMEPERSISTENCE][126][2]	[PLCVARIABLENAME][209][1]	[PLCBLOCKNAME][210][1]"
):
    for item in line:
        output_file.write(item + "\n")
    line = input_file.readline()

input_file.close()
output_file.close()
"""
tabl = pd.read_csv("import copy.csv", sep="\t", encoding="utf-16")


def f(Address):
    line = Address
    if line[0].isdigit() or line[1].isdigit():
        num = re.search(r"\d+", line).group()
        line = re.sub(r"in  Word", "", line)
        # Проверяем, попадает ли число в заданный промежуток
        if 8 <= int(num) <= 15:
            # Выполняем операции
            num = str(int(num) - 8)
            line = re.sub(
                r"(DB)(\d+)", lambda match: "DB" + str(int(match.group(2)) * 2), line
            )
            # Заменяем исходные значения
            line = re.sub(r"\d+", "", line, count=1)
            line = line + "." + num
            return line

        elif 0 <= int(num) <= 8:
            # Выполняем операции
            line = re.sub(
                r"(DB)(\d+)",
                lambda match: "DB" + str(int(match.group(2)) * 2 + 1),
                line,
            )
            # Заменяем исходные значения
            line = re.sub(r"\d+", "", line, count=1)
            line = line + "." + num
            return line

    elif line[0] == "D":
        line = re.sub(
            r"(DW|DD)(\d+)",
            lambda match: "DB" + match.group(1)[1:] + str(int(match.group(2)) * 2),
            line,
        )
        return line

    else:
        eror = "ERROR"
        return eror


tabl["Address"] = tabl["Address"].apply(f)
tabl.to_csv("export_1.csv", sep="\t", index=False)
