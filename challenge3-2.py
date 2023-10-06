import csv

with open('./PyPoll/Resources/election_data.csv') as csvfile:
    csvreader=csv.reader(csvfile)

    next(csvreader)

    print('Election Results')

    print('--------------------')

    
    total_votes=0
    candidate_op=[]
    candidate_votes={}

    county_op=[]
    county_votes={}

    win_candidate=""
    win_count=0
    win_county=0
    win_porc=0
    win_c_porc=0

    lrg_to_county=""
    lrg_turn_count=0

    for row in csvreader:
        total_votes=total_votes+1

        candidate_name=row[2]

        county_name=row[1]

    if candidate_name not in candidate_op:
        candidate_op.append(candidate_name)

        candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1

        print(f'Total Votes {total_votes}')
  
 
     
    

        


    
