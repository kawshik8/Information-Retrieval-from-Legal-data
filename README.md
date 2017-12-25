# Information-Retrieval-from-Legal-data

Precedence retrieval of legal documents is an information retrieval task to retrieve prior case documents that are related to a given case document. This helps in automatic linking of related documents to ensure that identical situations are treated similarly in every case. Several methodologies, such as information extraction based on nat- ural language processing, rule-based method, and machine learning techniques, are used to retrieve the prior cases with respect to the current case.

I have implemented a document similarity approach for this IRLeD precedence retrieval task. I have used three variations of our approach namely,

i. Method-1 with concepts and TF-IDF (Term Frequency - Inverse Document Frequency) scores, 
ii. Method- 2 with concepts, relations and TF-IDF scores, and 
iii. Method-3 with concepts, relations and Word2Vec.

We have implemented our methodology in Python for this IRLeD task. The data set used to evaluate the Task 2 (Precedence retrieval task) of IRLeD shared task consists of 200 current case documents and 2000 prior case documents. The steps used in our approach are given below.

• Preprocess the given text
• Extract linguistics features from both current case docu-
ments and prior case documents
• Construct feature vectors for the documents using TF-IDF
score or Word2Vec
• Find cosine similarity score between each current case with
all the prior cases
• Rank prior cases based on the similarity score for each cur-
rent case
