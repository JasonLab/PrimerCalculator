print ("Welcome to the Primer  Calculator")
print ("Note that this program uses the Wallace rule for melting temp estimation ")
StrandInfo= input("Enter your DNA strand: ")
StrandInfo= StrandInfo.lower()
StrandInfo= StrandInfo.strip()
Avalue= StrandInfo.count('a')
Cvalue= StrandInfo.count('c')
Tvalue= StrandInfo.count('t')
Gvalue= StrandInfo.count('g')
GCcontent= (Cvalue + Gvalue)/ len(StrandInfo)
GCcontent= round(GCcontent*100,1)  #Converting to %
MeltTemp = 4*Gvalue + 4*Cvalue + 2*Avalue + 2*Tvalue
print ("Primer Length is " + str(len(StrandInfo)) + "bp")
print ("Your Melting Temp is " + str(MeltTemp) + "°C")
print ("Your GC content is " + str(GCcontent)+ "%")
StrandInfo= StrandInfo.replace("a","T") #Changed to capital letter to avoid being re-replaced in sequence
StrandInfo= StrandInfo.replace("t","A")
StrandInfo= StrandInfo.replace("c","G")
StrandInfo= StrandInfo.replace("g","C")
print ("Your complementary strand is in the 5'-3' direction(Assuming you entered it 5'-3':)  " + StrandInfo[::-1])
#Strandinfo changes reverse the direction for a more sensical 5-3 direction
