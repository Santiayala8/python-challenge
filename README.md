# python-challenge

I had help buy a pier for the Dictionaries part

import csv

with open('./PyBank/Resources/budget_data.csv') as csvfile:

    csvreader = csv.reader(csvfile)

    next(csvreader)

    print('Financial Analysis') 



    print('-------------------------')  


    months_count=0
    total_profit=0
    dictionaries=[]
    gip=0
    gdp=0

    for row in csvreader:
        months_count+=1
        profit_loss=int(row[1])
        total_profit+=profit_loss
        data_dictionary = {}
        data_dictionary['date'] = row[0]
        data_dictionary['profit_loss'] = row[1]
        dictionaries.append(data_dictionary)

    dictionaries[0]['son']=0
    gip=dictionaries[0]
    gdp=dictionaries[0]

    for dict in range(1, len(dictionaries)): 
        dictionaries[dict]['son']=int(dictionaries[dict]['profit_loss'])-int(dictionaries[dict-1]['profit_loss'])

        if int(dictionaries[dict]['son'])>int(gip['son']):
            gip=dictionaries[dict]

        if int(dictionaries[dict]['son'])<int(gdp['son']):
            gdp=dictionaries[dict]
      
    months_count=len(dictionaries)
    max_index=len(dictionaries)-1
    avg_son=(1/max_index)*(int(dictionaries[max_index]['profit_loss']) - int(dictionaries[0]['profit_loss']))


    output_list=[
           [f"Financial Analysis"],
    [f"------------------------------"],
    [f"Total Months: {months_count}"],
    [f"Total: ${total_profit}"],
    [f"Average Change: ${avg_son:.2f}"],
    [f"Greatest Increase in Profits: {gip['date']} (${gip['son']})"],
    [f"Greatest Decrease in Profits: {gdp['date']} (${gdp['son']})"]
   ]
    
with open('./PyBank/Resources/tarea3.txt','w',newline='') as output_file:
    writer=csv.writer(output_file, delimiter='\t')
    writer.writerows(output_list)

    for line in output_list:
        for i in range(len(line)):
            print(line[i])
