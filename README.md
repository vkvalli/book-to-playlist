# Book-to-Playlist Recommendation System  

This repository contains the code for a recommendation system that suggests music playlists based on the themes of books. The project uses advanced machine learning techniques, including BERT embeddings and FAISS, to provide accurate and meaningful song recommendations.  

NOTE: The free trail on the HDFS servers ran out, so the code has been modified to run on google colab using colab servers instead


## **Dataset Description**  

The datasets used in this project contain the following information:  

### **Books Dataset**:  
- **Title**: Name of the book.  
- **Author**: Author(s) of the book.  
- **Genre**: Genre(s) of the book.  
- **Description**: Brief summary or synopsis of the book.  

### **Songs Dataset**:  
- **Acoustic Features**: Audio characteristics like acousticness, danceability, energy, etc.  
- **Lyrics**: Song lyrics used for thematic similarity analysis.  
- **Popularity**: Popularity score of the song.  

Due to size constraints, the datasets couldn't be uploaded here but can be found at:  
- [Kaggle](https://www.kaggle.com/datasets)  
- Various open-source music and book datasets.  


## **Analysis Performed**  

1. **Text Embeddings**:  
   - Generated embeddings for book descriptions and song lyrics using BERT to capture semantic meaning.  

2. **Similarity Matching**:  
   - Used FAISS (Facebook AI Similarity Search) for fast nearest-neighbor search to find songs matching the themes of books.  

3. **Dimensionality Reduction**:  
   - Applied PCA to optimize and speed up similarity searches.  

4. **Recommendation System**:  
   - Designed to recommend top N songs for a given book based on the highest similarity scores.  


## **Usage**  

1. **Download the Code**:  
   Clone this repository and set up the required environment.  

2. **Run the Backend**:  
   - The backend code is implemented using Flask. Run the following commands to start the development server:  
     ```bash
     python app.py
     ```
   - Navigate to the link provided in the console to use the application.  

3. **Datasets**:  
   - Before running the code, place the datasets (`books.csv` and `songs.csv`) in the `datasets` folder.  
   - If you don’t have the datasets, you can download them from Kaggle or other open dataset sources.  

4. **User Interaction**:  
   - Enter the name of a book in the provided input field.  
   - The system will display a list of songs that match the book's themes.  


## **Features**  

- **Book-to-Music Recommendation**: Provides music suggestions based on the thematic analysis of books.  
- **Interactive Front-End**: A simple and user-friendly interface was created using Flask.  
- **Semantic Matching**: Ensures recommendations are meaningful using advanced embedding techniques.  
