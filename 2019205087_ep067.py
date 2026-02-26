import time 
begin = time.time()

#----------#
import urllib.request #We are importing the urllib.request module to fetch the triangle data from the provided URL if the local file is not found.
def get_triangle_from_epwebsite(url):
    raw_data = urllib.request.urlopen(url).read().decode('utf-8') 
    triangle = []       
    for line in raw_data.strip().split('\n'):
        numbers = [int(num) for num in line.strip().split()]
        triangle.append(numbers)
    return triangle 
try: #First, we are trying to read the triangle data from a local file named "triangle.txt". 
    with open("0067_triangle.txt", 'r') as file:
        raw_data = file.read()
    triangle = []       
    for line in raw_data.strip().split('\n'):
        numbers = [int(num) for num in line.strip().split()]
        triangle.append(numbers)
except FileNotFoundError: #If the file is not found, we are fetching the triangle data from the provided URL using the get_triangle_from_epwebsite function.
    triangle = get_triangle_from_epwebsite("https://projecteuler.net/resources/documents/0067_triangle.txt")
#----------#

def max_path_sum(triangle):
    n = len(triangle) #We are getting the number of rows in the triangle
    for i in range(1,n): #Starting from the second row since the first row is consist of only one element.
        for j in range(i+1): #We are iterating through each element in the current row. 
                             #Since it is lower triangular matrix, the number of elements in the i-th row is i+1.
            if j == 0: #Left Edge Status
                triangle[i][j] += triangle[i-1][j] 
            elif j == i: #Right Edge Status
                triangle[i][j] += triangle[i-1][j-1] 
            else:       #Middle Status
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1]) #Getting and adding the maximum of two upper adjacent numbers.
    return max(triangle[n-1]) #The maximum path sum will be the maximum number in the last row after processing all rows.
print(max_path_sum(triangle))

end = time.time()
print(f"Finished in {end - begin} seconds.")