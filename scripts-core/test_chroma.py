# Sample illustration of text embeddings using ChromaDB
# taken from Data Camp web site

import chromadb


# create persistent sqlite db in this location
# chroma db requires a sqlite db
client = chromadb.PersistentClient("./chroma")

# create the collection object Students
# this object is just like a sqlite table that
# will store the test embeddings

try:
    client.delete_collection(name="Students")
except RuntimeError:
    pass
finally:
    collection = client.create_collection(name="Students")



# create the text variables
student_info = """
Alexandra Thompson, a 19-year-old computer science sophomore with a 3.7 GPA,
is a member of the programming and chess clubs who enjoys pizza, swimming, and hiking
in her free time in hopes of working at a tech company after graduating from the University of Washington.
"""

club_info = """
The university chess club provides an outlet for students to come together and enjoy playing
the classic strategy game of chess. Members of all skill levels are welcome, from beginners learning
the rules to experienced tournament players. The club typically meets a few times per week to play casual games,
participate in tournaments, analyze famous chess matches, and improve members' skills.
"""

university_info = """
The University of Washington, founded in 1861 in Seattle, is a public research university
with over 45,000 students across three campuses in Seattle, Tacoma, and Bothell.
As the flagship institution of the six public universities in Washington state,
UW encompasses over 500 buildings and 20 million square feet of space,
including one of the largest library systems in the world.
"""

# add the text variables to the collection Students
# this will automatically download a text embedding
# model from GitHub and use that for generating the
# text embeddings. So a GitHub connection is a must

collection.add(
    documents = [student_info, club_info, university_info],
    metadatas = [{"source": "student info"},{"source": "club info"},{'source':'university info'}],
    ids = ["id1", "id2", "id3"]
)

# Now query the Students collection
# asking for number of results = 1
results = collection.query(
    query_texts=["What is the student name?"],
    n_results=1
)

print(results)





