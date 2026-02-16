web_users = ['Vecna','Voldemort','Victor','Victoria','Vesuvius']
new_users = ['Vecna','Voldemort','Henry','Tom','Whatsit']
for new_user in new_users:
    if new_user in web_users:
         print('This user name "'+new_user+'" is already in use. Please choose a different user name.')
    else:
        print('This user name "'+new_user+'" is available')
cities = {'Vilnius':{'country':'Lithuania','population':607667,'fact':'established 1387'},'Kyiv':{'country':'Ukraine','population':3000000,'fact':'established 482 AD'},'Baltimore':{'country':'United States','population':568000,'fact':'established 1729'}}
for city in cities:
    print("City: "+city+" Country: "+cities[city]['country']+" Population: "+str(cities[city]['population'])+" Fact: "+cities[city]['fact'])