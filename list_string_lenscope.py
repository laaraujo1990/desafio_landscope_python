"""
Searching Challenge
Have the function SearchingChallenge(strArr) read in the strArr parameter containing 
key:value pairs where the key is a string and the value is an integer. Your program should 
return a string with new key:value pairs separated by a comma such that each key appears 
only once with the total values summed up.

For example: if strArr is ["B:-1", "A:1", "B:3", "A:5"] then your program should return 
the string A:6,B:2.

Your final output string should return the keys in alphabetical order. Exclude keys that 
have a value of 0 after being summed up.
Examples
Input: ["X:-1", "Y:1", "X:-4", "B:3", "X:5"]
Output: B:3,Y:1
Input: ["Z:0", "A:-1"]
Output: A:-1
"""

def SearchingChallenge(strArr):

  resp = []
  resp2 = []
  resp3 = []
  count = 0
  t = 0
  for i in strArr:
    resp.append(strArr[count].split(":"))
    count = count + 1
  for i in range(0, len(resp)):
    for y in range(0, len(resp)):
      if i != y :
        if resp[i][0] == resp[y][0] :
          t = (int(resp[i][1]) + int(resp[y][1]))
          resp[i][1] = str(0)
          resp[y][1] = str(t)
  for z in range(0, len(resp)):
    #print(resp[z])
    if int(resp[z][1]) != 0:
      #print('x')
      #print(resp[z])
      resp2.append(':'.join(resp[z]))
  resp3 = sorted(resp2)
  #print(resp3)
  resp3 = (','.join(resp3))
  #print(resp3)

  return resp3

# keep this function call here 
print(SearchingChallenge(input()))
