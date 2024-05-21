# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"J64zz00","system":"readv2"},{"code":"J64z.00","system":"readv2"},{"code":"J64..00","system":"readv2"},{"code":"26889.0","system":"readv2"},{"code":"47536.0","system":"readv2"},{"code":"15181.0","system":"readv2"},{"code":"3599.0","system":"readv2"},{"code":"35469.0","system":"readv2"},{"code":"44649.0","system":"readv2"},{"code":"4416.0","system":"readv2"},{"code":"48587.0","system":"readv2"},{"code":"109379.0","system":"readv2"},{"code":"107004.0","system":"readv2"},{"code":"42694.0","system":"readv2"},{"code":"27437.0","system":"readv2"},{"code":"760.0","system":"readv2"},{"code":"15602.0","system":"readv2"},{"code":"39025.0","system":"readv2"},{"code":"31650.0","system":"readv2"},{"code":"49202.0","system":"readv2"},{"code":"61996.0","system":"readv2"},{"code":"40075.0","system":"readv2"},{"code":"69721.0","system":"readv2"},{"code":"49106.0","system":"readv2"},{"code":"12140.0","system":"readv2"},{"code":"36879.0","system":"readv2"},{"code":"17959.0","system":"readv2"},{"code":"29142.0","system":"readv2"},{"code":"12316.0","system":"readv2"},{"code":"61298.0","system":"readv2"},{"code":"96679.0","system":"readv2"},{"code":"71134.0","system":"readv2"},{"code":"4429.0","system":"readv2"},{"code":"62988.0","system":"readv2"},{"code":"930.0","system":"readv2"},{"code":"35046.0","system":"readv2"},{"code":"34683.0","system":"readv2"},{"code":"47888.0","system":"readv2"},{"code":"7306.0","system":"readv2"},{"code":"8620.0","system":"readv2"},{"code":"22697.0","system":"readv2"},{"code":"8723.0","system":"readv2"},{"code":"29663.0","system":"readv2"},{"code":"17323.0","system":"readv2"},{"code":"66713.0","system":"readv2"},{"code":"61367.0","system":"readv2"},{"code":"94302.0","system":"readv2"},{"code":"6285.0","system":"readv2"},{"code":"64132.0","system":"readv2"},{"code":"34063.0","system":"readv2"},{"code":"12438.0","system":"readv2"},{"code":"54853.0","system":"readv2"},{"code":"96795.0","system":"readv2"},{"code":"24866.0","system":"readv2"},{"code":"42278.0","system":"readv2"},{"code":"63208.0","system":"readv2"},{"code":"45836.0","system":"readv2"},{"code":"K80","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cholelithiasis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cholelithiasis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cholelithiasis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cholelithiasis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
