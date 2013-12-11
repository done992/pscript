sport_map = {'Tom Wang':'football', 
		'Mike Sui':'basketball',
		'Tony Li':'swimming',
		'Lily Zhang':'PingPong'
		}

print(sport_map)
print(sport_map['Tony Li'])
del sport_map['Tony Li']
print(sport_map)

#replace
sport_map['Tom Wang'] = 'swimming'
print(sport_map)

#you can’t join maps with the plus operator(+)