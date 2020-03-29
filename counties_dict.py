counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
#for county in counties_dict:
 #   print(county)


    
#or county in counties_dict.keys():
  #  print (county)
#for voters in counties_dict.values():
    #print(voters)
#for tomatos in counties_dict.values():
    #print(tomatos)
#for counties in counties_dict:
   # print(counties_dict[county]



#voting_data = [{"county" : "Arapahoe", "registered_voters" : 422829}, {"county" : "Denver", "registered_voters" : 463353}, {"county" : "Jefferson", "registered_voters" : 432428}]
#    for county_dict in voting_data:
#     print(county_dict)
#for county_dict in voting_data:
 #   for value in county_dict.values():
    #        print(value)

for county, voters in counties_dict.items():
    print(county + " county has " str(voters) + " registered voters.")

