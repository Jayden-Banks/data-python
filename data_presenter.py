from matplotlib import pyplot as plt
f = open("CupcakeInvoices.csv")

#cupcake cost tracker
total_cost = 0
choc = []
vani = []
stra = []

#cupcake count tracker
amount_choc = []
amount_vani = []
amount_stra = []

for line in f:
    #print(line) #prints every line
    line = line.split(',')
    #print(line[2]) #prints only flavors
    temp_count = float((line[3]))
    temp_cost = float((line[4]))
    #total_cost = temp_count * temp_cost #This is just for the total of each line, remove global total_cost also
    total_cost = round(total_cost + (temp_count * temp_cost),2) #this is not the best way, but it works.
    #print(total_cost) #for total cost per line


    if (line[2] == 'Chocolate'):
        if (amount_choc):
            choc.append(round(choc[-1]+ (temp_count * temp_cost),2))
            amount_choc.append(amount_choc[-1] + int(line[3]))
        else:
            choc.append(round((temp_count * temp_cost),2))
            amount_choc.append(int(line[3]))

    
    elif (line[2] == 'Vanilla'):
        if (amount_vani):
            vani.append(round(vani[-1]+ (temp_count * temp_cost),2))
            amount_vani.append(amount_vani[-1] + int(line[3]))
        else:
            vani.append(round((temp_count * temp_cost),2))
            amount_vani.append(int(line[3]))
        
    elif (line[2] == 'Strawberry'):
        if (amount_stra):
            stra.append(round(stra[-1]+ (temp_count * temp_cost),2))
            amount_stra.append(amount_stra[-1] + int(line[3]))
        else:
            stra.append(round((temp_count * temp_cost),2))
            amount_stra.append(int(line[3]))
f.close()

#adds a 0 to each array to start the graph at 0
choc.insert(0,0)
amount_choc.insert(0,0)
vani.insert(0,0)
amount_vani.insert(0,0)  
stra.insert(0,0)
amount_stra.insert(0,0)  

print(f"Total income = ${total_cost}")

#displays the graph
plt.style.use('dark_background')
plt.plot(choc, amount_choc, color='brown',label='Chocolate cupcakes')
plt.plot(vani, amount_vani, color='gold',label='Vanilla cupcakes')
plt.plot(stra, amount_stra, color='magenta',label='Strawberry cupcakes')

plt.title('Cupcakes YUMMY!')
plt.xlabel('Total Income (USD)')
plt.ylabel('Cupcakes Sold')
plt.legend()
plt.tight_layout()
plt.show()
#print(plt.style.available)