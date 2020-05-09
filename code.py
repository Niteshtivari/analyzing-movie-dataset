# --------------
from csv import reader
from collections import Counter

def explore_data(dataset, start, end, rows_and_columns=False):
    for i in range(start,end):
        print(dataset[i])
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    
    
        
     


def duplicate_and_unique_movies(dataset, index_):
    t=[]
    for i in range(len(dataset)):
        t.append(dataset[i][index_])
    t=map(tuple,t)
    fre = Counter(t)
    #print(fre)
    for (row,freq) in fre.items():
        if freq > 1:
            print(row)

    

    
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy
    """
    
    


def movies_lang(dataset, index_, lang_):
    movies_=[]
    for i in range(len(dataset)):
        if dataset[i][index_] == lang_:
            movies_.append(dataset[i])
            
    
    return movies_
    



def rate_bucket(dataset, rate_low, rate_high):
    rated_movies=[]
    for i in range(len(dataset)):
        if  float(dataset[i][11]) >= int(rate_high):
            rated_movies.append(dataset[i])
        
        


    """Extract the movies within the specified ratings.
    
    #This function extracts all the movies that has rating between rate_low and high_rate.
    #Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    #Keyword arguments:
    #dataset -- list containing the details of the movie
    #rate_low -- lower range of rating
   # rate_high -- higher range of rating
    
    #Returns:
    #rated_movies -- list of the details of the movies with required ratings
   # """

    
    return rated_movies




# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)
movies_header=movies[0]
print(movies_header)
movies.pop(0)
#print(movies)



# The first row is header. Extract and store it in 'movies_header'.


# Subset the movies dataset such that the header is removed from the list and store it back in movies




# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
#print(movies[4553])
movies.pop(4553)


# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
print(explore_data(movies,0,5,rows_and_columns=False))
duplicate_and_unique_movies(movies,13)
movies_en=movies_lang(movies,3,"en")
print(movies_en)
high_rated_movies=rate_bucket(movies_en,3,8)
print(high_rated_movies)

# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.




# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.



# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 




# Calling movies_lang(), extract all the english movies and store it in movies_en.




# Call the rate_bucket function to see the movies with rating higher than 8.



