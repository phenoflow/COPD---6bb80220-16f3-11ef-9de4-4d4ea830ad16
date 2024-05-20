# Eleanor L Axson, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"63480004","system":"readv2"},{"code":"195951007","system":"readv2"},{"code":"84409004","system":"readv2"},{"code":"826111000000109","system":"readv2"},{"code":"313299006","system":"readv2"},{"code":"716281000000103","system":"readv2"},{"code":"713731000000102","system":"readv2"},{"code":"414087000","system":"readv2"},{"code":"270473001","system":"readv2"},{"code":"40100001","system":"readv2"},{"code":"866901000000103","system":"readv2"},{"code":"716901000000101","system":"readv2"},{"code":"736283006","system":"readv2"},{"code":"135836000","system":"readv2"},{"code":"196027008","system":"readv2"},{"code":"68328006","system":"readv2"},{"code":"848431000000106","system":"readv2"},{"code":"77690003","system":"readv2"},{"code":"723245007","system":"readv2"},{"code":"413845009","system":"readv2"},{"code":"293991000000106","system":"readv2"},{"code":"61937009","system":"readv2"},{"code":"857661000000104","system":"readv2"},{"code":"195963002","system":"readv2"},{"code":"185086009","system":"readv2"},{"code":"716241000000106","system":"readv2"},{"code":"394703002","system":"readv2"},{"code":"195949008","system":"readv2"},{"code":"198901000000105","system":"readv2"},{"code":"390891009","system":"readv2"},{"code":"716358000","system":"readv2"},{"code":"717021000000106","system":"readv2"},{"code":"383611000000102","system":"readv2"},{"code":"195959009","system":"readv2"},{"code":"16003001","system":"readv2"},{"code":"198401000000104","system":"readv2"},{"code":"45145000","system":"readv2"},{"code":"1823851000006103","system":"readv2"},{"code":"313296004","system":"readv2"},{"code":"198411000000102","system":"readv2"},{"code":"4981000","system":"readv2"},{"code":"313297008","system":"readv2"},{"code":"401184000","system":"readv2"},{"code":"717521000000104","system":"readv2"},{"code":"266355005","system":"readv2"},{"code":"89549007","system":"readv2"},{"code":"195957006","system":"readv2"},{"code":"741056003","system":"readv2"},{"code":"266356006","system":"readv2"},{"code":"401185004","system":"readv2"},{"code":"195958001","system":"readv2"},{"code":"390941006","system":"readv2"},{"code":"8743301","system":"readv2"},{"code":"74417001","system":"readv2"},{"code":"195953005","system":"readv2"},{"code":"196001008","system":"readv2"},{"code":"87433001","system":"readv2"},{"code":"170628003","system":"readv2"},{"code":"13645005","system":"readv2"},{"code":"10692761000119107","system":"readv2"},{"code":"196026004","system":"readv2"},{"code":"760601000000107","system":"readv2"},{"code":"394702007","system":"readv2"},{"code":"52571006","system":"readv2"},{"code":"760621000000103","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('copd-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["copd---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["copd---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["copd---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
