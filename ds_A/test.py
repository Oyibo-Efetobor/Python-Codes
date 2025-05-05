import csv

jan_weather = {}

with open('nyc_weather.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    #read each row
    
    for row in csv_reader:
        jan_weather[row[0]] = row[1]
        
#what was the avg temp in the first week of january

def find_avg_temp(no_of_days):
    sum = 0
    for i in range(no_of_days):
        sum += int((jan_weather['Jan '+ str(i+1)]))
    jan_avg_f_week = sum/no_of_days
    return print(int(jan_avg_f_week))


find_avg_temp(7)

#what was the maximum in temp in the first 10 days

def find_max_temp(no_of_days):
    max = ((jan_weather['Jan '+ str(1)]))
    for i in range(no_of_days - 2):
        if ((jan_weather['Jan '+ str(i+1)])) > ((jan_weather['Jan '+ str(i+2)])):
            max = ((jan_weather['Jan '+ str(i+1)])) 
    
    return print(int(max))

find_max_temp(10)

#what was the temp on Jan.9 & Jan.4

print(jan_weather['Jan 9'], jan_weather['Jan 4'])





