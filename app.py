from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipe_directory_table.sql")

# Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# print("# List them out")
# for artist in artists:
#     print(artist)

# album_repo = AlbumRepository(connection)

# print("# list all albums")
# for album in album_repo.all():
#     print (album)

# print("# find album with id 10")
# print(album_repo.find(10))

recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()
print(" - Print all recipes")
print(recipes)

recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.find(3)
print(" - Print all with rating 3")
print(recipes)



