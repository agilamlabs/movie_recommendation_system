import streamlit as st
from imdb import Cinemagoer

st.set_page_config(page_title="Movie Recommendation and Search", layout="wide")
st.title("\U0001F3A5 Movie Search")

st.markdown("""
<div style="display: flex; align-items: center; background-color: black; padding: 5px; border-radius: 3px;">
    <span style="font-size: 18px; color: #2e8b57; font-weight: bold; margin-right: 10px;">Created by:</span>
    <a href="https://www.linkedin.com/in/gn-raavanan" target="_blank" style="text-decoration: none; display: flex; align-items: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 5px;">
        <span style="font-size: 18px; font-weight: bold; color: #fff;">Gokul nath</span>
    </a>
</div>
""", unsafe_allow_html=True)

# Initialize Cinemagoer
ia = Cinemagoer()

# Search input
st.write("## Search for a Movie")
search_query = st.text_input("Enter Movie Title :", "")

st.write("---")
st.write("## Filters")

# Rating Range
st.write("### Rating Range")
col1, col2 = st.columns(2)
with col1:
    min_rating = st.number_input("Minimum Rating", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
with col2:
    max_rating = st.number_input("Maximum Rating", min_value=0.0, max_value=10.0, value=10.0, step=0.1)

# Year range (using selectboxes for years)
st.write("### Release Year Range")
years = ["Any"] + list(range(2025, 1949, -1))
col3, col4 = st.columns(2)
with col3:
    start_year = st.selectbox("From Year:", years, index=0)
with col4:
    end_year = st.selectbox("To Year:", years, index=0)

# Genre dropdown
st.write("### Genre")
genre_options = ["Any", "Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller", "Adventure", "Animation"]
genre = st.selectbox("Select Genre:", genre_options)

# Country dropdown
st.write("### Country of Origin")
country_options = ["Any", "USA", "UK", "India", "France", "Germany", "Japan", "Canada", "Australia", "Italy"]
country = st.selectbox("Select Country:", country_options)

# Language dropdown
st.write("### Language")
language_options = ["Any", "English", "Tamil", "Telugu", "Kannada", "Malayalam", "French", "German", "Japanese", "Spanish", "Chinese", "Italian", "Korean"]
selected_language = st.selectbox("Select Language:", language_options)

# Cast and Crew Name
st.write("### Cast or Crew")
cast_crew_query = st.text_input("Enter Cast or Crew Name:", "")

# Submit button
submit = st.button("Submit")

def movie_matches_filters(movie_obj):
    """
    Check if a movie matches the given filters.
    """
    # Check rating
    rating = movie_obj.get('rating')
    if rating is not None and (rating < min_rating or rating > max_rating):
        return False

    # Check year range
    movie_year = movie_obj.get('year')
    if start_year != "Any" and movie_year is not None and movie_year < int(start_year):
        return False
    if end_year != "Any" and movie_year is not None and movie_year > int(end_year):
        return False

    # Check genre
    if genre != "Any":
        movie_genres = movie_obj.get('genres', [])
        if not movie_genres or genre.lower() not in [g.lower() for g in movie_genres]:
            return False

    # Check country
    if country != "Any":
        movie_countries = movie_obj.get('countries', [])
        if not movie_countries or not any(country.lower() in c.lower() for c in movie_countries):
            return False

    # Check language
    if selected_language != "Any":
        movie_langs = movie_obj.get('languages', [])
        if not movie_langs or not any(selected_language.lower() in lang.lower() for lang in movie_langs):
            return False

    # Check cast/crew
    if cast_crew_query:
        query_lower = cast_crew_query.lower()

        cast_list = movie_obj.get('cast', [])
        cast_names = [person.get('name', '').lower() for person in cast_list]

        director_list = movie_obj.get('director', [])
        director_names = [person.get('name', '').lower() for person in director_list]

        writer_list = movie_obj.get('writer', [])
        writer_names = [person.get('name', '').lower() for person in writer_list]

        if not (any(query_lower in name for name in cast_names) or
                any(query_lower in name for name in director_names) or
                any(query_lower in name for name in writer_names)):
            return False

    return True

if submit:
    with st.spinner("\U0001F50D Searching..."):
        # Search for a movie
        results = ia.search_movie(search_query) if search_query.strip() else ia.get_top250_movies()
        if not results:
            st.warning("No movies found for your query.")
        else:
            filtered_results = []
            for r in results:
                try:
                    movie_id = r.movieID
                    movie_obj = ia.get_movie(movie_id)
                    if movie_matches_filters(movie_obj):
                        filtered_results.append(movie_obj)
                except Exception as e:
                    st.error(f"Error processing movie ID {r.movieID}: {e}")
                    continue

            if filtered_results:
                st.success(f"### Found {len(filtered_results)} result(s):")
                for fr in filtered_results:
                    title = fr.get('title', 'Untitled')
                    year = fr.get('year', 'N/A')
                    rating = fr.get('rating', 'N/A')
                    wiki_url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
                    st.markdown(f"- **[{title} ({year})](<{wiki_url}>)** - Rating: {rating}")
            else:
                st.warning("No movies match the given filters.")
