# Eleanor L Axson, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"66YS.00","system":"readv2"},{"code":"66YB200","system":"readv2"},{"code":"66YD.00","system":"readv2"},{"code":"66YT.00","system":"readv2"},{"code":"66YB.00","system":"readv2"},{"code":"9Oi..00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('copd-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["copd-monitoring---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["copd-monitoring---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["copd-monitoring---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
