movies = []

while True:
    print("\n--- Add a New Movie ---")
    title = input("Movie title: ")
    watched_with = input("Who did you watch it with? ")
    where = input("Where did you watch it? (e.g., cinema, home, etc.): ")
    rating = input("Rate the movie out of 10: ")
    favourite_scene = input("Describe your favourite scene: ")

    movie = {
        "title": title,
        "watched_with": watched_with,
        "where": where,
        "rating": rating,
        "favourite_scene": favourite_scene
    }
    movies.append(movie)

    print("\n=== Movies Collected So Far ===")
    for m in movies:
        print(f"\n🎥 {m['title']}")
        print(f"  Watched with: {m['watched_with']}")
        print(f"  Where: {m['where']}")
        print(f"  Rating: {m['rating']}/10")
        print(f"  Favourite scene: {m['favourite_scene']}")

    cont = input("\nAdd another movie? (yes/no): ").lower()
    if cont != "yes":
        print("\nThanks for using the Movie Collector!")
        break
