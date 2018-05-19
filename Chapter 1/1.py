def isUnique(string):
	l=len(string)
	for i in range(l):
		for j in range(i+1,l):
			if (string[i] == string[j]):
				return False

	return True

print(isUnique("hola mund"))