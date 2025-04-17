

from langchain_ollama import ChatOllama
from random import choice
from flux_quantized import Flux
import json
import os

concepts = ["Bohemian Rhapsody", "Mid-Century Modern", "Coastal Farmhouse", "Industrial Loft", "Scandinavian Hygge", "Hollywood Regency", "Tropical Maximalism", "Moroccan Oasis", "Art Deco Glamour", "French Country Cottage", "Contemporary Minimalism", "Japanese Wabi-Sabi", "Rustic Industrial", "Shabby Chic Romance", "Nautical Explorer", "Urban Zen", "Victorian Gothic", "Eclectic Fusion", "Global Nomad", "Desert Serenity", "Prairie Revival", "English Manor", "Mediterranean Villa", "Southwestern Adobe", "Art Nouveau Flow", "Dark Academia", "Japandi Harmony", "Biophilic Design", "Coastal Grandmother", "Dark Romantic", "Modern Organic", "Transitional Style", "Grandmillennial", "New Traditional", "Hollywood Glam", "Rustic Modern", "Minimalist Maximalism", "Coastal Contemporary", "Urban Farmhouse", "French Provincial", "Scandinavian Modern", "Tropical Modern", "Moroccan Contemporary", "Art Deco Revival", "Rustic Scandinavian", "Shabby Bohemian", "Nautical Modern", "Industrial Farmhouse", "Victorian Modern", "Eclectic Maximalism", "Global Contemporary", "Desert Modern", "Prairie Chic", "English Country", "Mediterranean Contemporary", "Southwestern Contemporary", "Art Nouveau Revival", "Japandi Rustic", "Biophilic Maximalism", "Coastal Luxe", "Dark Victorian", "Modern Farmhouse", "Transitional Contemporary", "Grandmillennial Modern", "Hollywood Regency Revival", "Rustic Bohemian", "Minimalist Organic", "Coastal Vintage", "Nautical Chic", "Industrial Vintage", "Victorian Eclectic", "Eclectic Traditional", "Global Luxe", "Desert Contemporary", "Prairie Traditional", "English Victorian", "Mediterranean Rustic", "Southwestern Modern", "Art Deco Modern", "Japandi Contemporary", "Biophilic Contemporary", "Coastal Glam", "Dark Traditional", "Modern Rustic", "Transitional Rustic", "Grandmillennial Luxe", "Hollywood Glam", "Rustic Luxe", "Minimalist Bohemian", "Coastal Industrial", "Nautical Traditional", "Industrial Chic Revival", "Victorian Grand Revival", "Eclectic Bohemian", "Global Contemporary", "Desert Luxe", "Prairie Modern Revival", "English Modern", "Mediterranean Contemporary", "Southwestern Contemporary", "Art Nouveau Contemporary", "Japandi Luxe", "Biophilic Rustic", "Coastal Traditional", "Dark Modern", "Modern Victorian", "Transitional Modern", "Grandmillennial Chic", "Hollywood Regency", "Rustic Contemporary", "Minimalist Contemporary", "Coastal Vintage", "Nautical Modern", "Industrial Modern", "Victorian Traditional", "Eclectic Modern", "Global Rustic", "Desert Contemporary Revival", "Prairie Chic Revival", "English Traditional Revival", "Mediterranean Modern Revival", "Southwestern Contemporary Revival", "Art Nouveau Modern Revival", "Japandi Traditional Revival", "Biophilic Contemporary Revival"]
colors = ["Cerulean Blue", "Forest Green", "Rose Gold", "Terracotta", "Lavender", "Charcoal Grey", "Mustard Yellow", "Coral Pink", "Slate Blue", "Olive Drab", "Burgundy Wine", "Seafoam Green", "Peach Melba", "Taupe", "Indigo", "Crimson", "Silver Sage", "Goldenrod", "Periwinkle", "Bronze", "Amethyst Purple", "Hunter Green", "Dusty Rose", "Saffron", "Cobalt", "Jade", "Magnolia", "Copper", "Lilac", "Pine Green", "Apricot", "Steel Grey", "Orchid", "Emerald", "Cream", "Brick Red", "Sky Blue", "Beige", "Plum", "Teal", "Sand", "Marigold", "Aqua", "Russet", "Mauve", "Chartreuse", "Navy Blue", "Caramel", "Viridian", "Champagne", "Fuchsia", "Ochre", "Royal Blue", "Butterscotch", "Lime Green", "Pearl White", "Deep Purple", "Ginger", "Turquoise", "Tan", "Electric Blue", "Honey", "Fern Green", "Ivory", "Wineberry", "Cinnamon", "Sapphire", "Stone Grey", "Lemon Yellow", "Mint Green", "Slate Grey", "Rosewood", "Pineapple", "Midnight Blue", "Shadow Grey", "Coral Reef", "Basil", "Antique White", "Oxblood", "Golden Honey", "Sea Glass", "Dusty Lavender", "Desert Sand", "Royal Purple", "Moss Green", "Peach Blossom", "Silver Birch", "Deep Teal", "Warm Grey", "Electric Lime", "Soft Peach", "Midnight Emerald", "Slate Teal", "Dusty Rose Pink", "Olive Branch", "Pale Gold", "Ocean Blue", "Copper Penny", "Lilac Grey", "Forest Olive", "Apricot Orange", "Royal Azure", "Shadow Plum", "Lemon Chiffon", "Seafoam Aqua", "Warm Terracotta", "Antique Gold", "Deep Indigo", "Spring Green", "Silver Grey", "Rose Quartz", "Bronze Copper", "Amethyst Smoke", "Hunter Teal", "Dusty Coral", "Saffron Spice", "Cobalt Sky", "Jade Forest", "Magnolia Bloom", "Pearl Shimmer", "Wineberry Swirl", "Cinnamon Bark", "Sapphire Dusk", "Stone Whisper", "Lemon Zest", "Mint Julep", "Slate Mist", "Rosewood Brown", "Pineapple Sorbet", "Royal Violet", "Shadow Teal", "Spring Meadow", "Silver Lining", "Rose Petal", "Bronze Age", "Amethyst Dream", "Hunter Teal", "Dusty Coral", "Saffron Glow", "Cobalt Mist", "Jadeite Green", "Magnolia Silk", "Pearl Essence", "Wineberry Blush", "Cinnamon Swirl", "Sapphire Velvet", "Stone Serenity"]
rooms = ["living room", "bedroom", "kitchen", "bathroom", "dining room", "home office", "entryway", "laundry room", "basement", "attic", "garage", "sunroom", "playroom", "media room", "guest room", "library", "den", "outdoor patio", "balcony", "garden shed"]


class Post():
    def __init__(self, id: int, len: int = 10) -> None:
        self.id: int = id
        self.len: int = len
        self.concept: str = ""
        self.color: str = ""
        self.rooms: list[str] = [ "" for _ in range(self.len) ]
        self.flux_prompts: list[str] = [ "" for _ in range(self.len) ]
        self.caption: str = ""
        self.comment: str = ""
    

    def __repr__(self) -> str:
        return f"""PostData(
            id={self.id},
            len={self.len},
            concept={self.concept},
            color={self.color},
            rooms={self.rooms},
            flux_prompts={self.flux_prompts},
            caption={self.caption},
            comment={self.comment}
        )"""


    def __str__(self) -> str:
        return self.__repr__()
    

    def save(self) -> None:
        if not os.path.exists(f"images/{self.id}"):
            os.makedirs(f"images/{self.id}", exist_ok=True)

        with open(f"images/{self.id}/metadata.json", "w") as f:
            json.dump({
                "id": self.id,
                "len": self.len,
                "concept": self.concept,
                "color": self.color,
                "rooms": self.rooms,
                "flux_prompts": self.flux_prompts,
                "caption": self.caption,
                "comment": self.comment
            }, f)


    def choose(self) -> None:   # possibly make deterministic with seed
        self.concept = choice(concepts)
        self.color = choice(colors)
        rooms_cpy = rooms.copy()
        for i in range(my_post.len):
            room = choice(rooms_cpy)
            rooms_cpy.remove(room)
            self.rooms[i] = room

        
    def generate_text(self) -> None:
        llm = ChatOllama(model = "gemma3:12b", keep_alive=1, )
        for i in range(self.len):
            self.flux_prompts[i]: str = llm.invoke(f"the goal is to create an instagram post about interior design. think of a room layout for {self.rooms[i]} use the style concept {self.concept} in the color {self.color}. create a flux image generation prompt. only respond with the prompt.").content
            print(self.flux_prompts[i]+"\n")
        self.caption = llm.invoke(f"write an instagram caption to an interior design post with the style concept of {self.concept} with the color {self.color}. start philosophical. only respond with the cpation.").content
        self.comment = llm.invoke(f"write an instagram comment to a post about interior design with the {self.concept} style concept. end with a call to action. only respond with the caption.").content


for j in range(20):
    my_post = Post(70+j)
    my_post.choose()
    print(my_post)
    my_post.generate_text()
    print(my_post.caption+"\n")
    print(my_post.comment)
    print("\n######\n\n\n")
    my_post.save()

    sleep(3)
    flux = Flux()
    for i in range(my_post.len):
        flux.generate_image(my_post.flux_prompts[i], f"images/{my_post.id}/{i}.png")
    flux.clear_memory()
    sleep(3)

