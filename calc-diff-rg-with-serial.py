
file = open('res-sorted.txt', 'r')
wfile = open('res-reply-diff.txt', 'w')
Lines = file.readlines()

#statistic(bytes/packets/allow_err): org=237/4/1 reply=15441/13/1 tuples=2
#serial=660d3146 tos=ff/ff app_list=0 app=0 url_cat=0

for i in range(229292):
	
	pieces1 = Lines[i].split()
	pieces2 = Lines[i+1].split()
	if(pieces1[0] == pieces2[0]):
		diff = int(pieces2[2])-int(pieces1[2])
		#print(str(diff)+" "+pieces1[0])  # print diff or org, and serial 
		wfile.write(str(diff)+" "+pieces1[0]+"\n") # print diff or org, and serial
		#wfile.write(str(diff)+"\n") # print Only org
		i=i+1
		
wfile.close()
file.close()


