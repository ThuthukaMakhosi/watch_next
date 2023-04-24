def movies(description):
  #stores similaritty values
  sim_list = []
  for i in movie_dictionary.values():
    model_description = nlp(description)

    #Each movie description is compared to the given movie description then the similarities are printed
    similarity = nlp(i).similarity(model_description)
    print(i + " - " + str(similarity))
    print('\n')
    sim_list.append(similarity)

    movie_title = []
  for x in movie_dictionary.keys():
    movie_title.append(x)

  #returns the  title of the most similar movie
  return print("Most similar movie: "+movie_title[sim_list.index(max(sim_list))])

#----------------------------------------------------------------------
#Importing spacy library
import spacy
nlp = spacy.load('en_core_web_md')


#Reading file movies text file
file = open("movies.txt").read()
file = file.split('\n')
file.pop()

#dictionary to store contents from the text file
movie_dictionary={}
for movie in file:
  movie_dictionary[movie.split(":")[0]] = movie.split(":")[1]

#description of the movie
movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

#calling the movies function
movies(movie_description) 