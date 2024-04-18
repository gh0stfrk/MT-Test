import random
import requests
import httpx
import asyncio

# List of sample titles and descriptions
sample_titles = [
    "The Mystery of the Dancing Traffic Cones",
    "Attack of the Giant Rubber Duck",
    "The Rebellion of the Rogue Garden Gnomes",
    "Alien Invasion: Pigeons Take Flight",
    "The Great Squirrel Nut Heist",
    "Invasion of the Inflatable Flamingos",
    "Chaos in the City: Leprechauns on the Loose",
    "Ninja Turtles vs. Sewer Problems",
    "The Tumbleweed Takeover",
    "Gang of Mischievous Garden Gnomes",
    "Haunted Crosswalk Signals: A Spooky Situation",
    "Seagulls vs. Ice Cream Trucks",
    "Time-Traveling Potholes: The Bumpy Ride",
    "Disco Fire Hydrants: Dancing in the Streets",
    "Stampede of Tiny Unicorns",
    "Rogue Shopping Carts: A Traffic Nightmare",
    "Rocket-Powered Skateboards: Billionaire Shenanigans",
    "Traffic Cones Go on Strike",
    "Invasion of the Inflatable Rubber Chickens",
    "Lights Out: Neighborhood Darkness",
    "Flash Mob or Alien Invasion?",
    "Kitten Stampede: Feline Frenzy",
    "Squirrel Gang Takes Over the Neighborhood",
    "Marshmallow Men Cause Chaos",
    "Secret Society of Garden Gnomes",
    "Subway Disco Party: Underground Fun",
    "Pigeons on a Bus: Feathered Commuters",
    "Rebellious Garden Hoses",
    "Seagull Coup: Beach Takeover",
    "Mysterious Crop Circles in the Park",
    "Rogue Shopping Carts on the Loose",
    "Giant Rubber Duck Leads Duck Parade",
    "Disco Party in the Mayor's Office",
    "Pigeon Flight Delays: Bird Traffic",
    "Squirrel Picnic Basket Heist",
    "Inflatable Octopus Invasion",
    "Runaway Garden Gnomes",
    "Giant Rubber Duck Protests Duck Sauce",
    "Disco Party in City Hall",
    "Pigeon Rooftop Takeover",
    "Squirrel Peanut Factory Hijack",
    "Inflatable Penguin Invasion",
    "Runaway Garden Hoses",
    "Giant Rubber Duck Protests Rubber Duckies",
    "Disco Party in the Fire Station",
    "Pigeon Chaos at Weddings",
    "Squirrel Picnic Basket Theft",
    "Inflatable Sheep Invasion",
    "Runaway Garden Gnomes",
    "Giant Rubber Duck Protests Duckweed",
]

sample_descriptions = [
    "Reports of traffic cones spontaneously dancing in the streets, causing confusion and amusement.",
    "A giant rubber duck mysteriously appears in the city, leading to traffic delays and photo opportunities.",
    "Garden gnomes revolt against their owners, staging elaborate pranks and mischief.",
    "Pigeons are spotted organizing in large flocks, leading to speculation of avian uprising.",
    "Squirrels launch a coordinated effort to steal all the nuts in the neighborhood, leaving residents bewildered.",
    "Inflatable flamingos invade the city, bringing a splash of color and chaos to the streets.",
    "Leprechauns wreak havoc on the city, leaving pots of gold and mischief in their wake.",
    "Ninja turtles emerge from the sewers, leading to both admiration and concern from residents.",
    "Tumbleweeds roll through urban areas, causing unexpected obstacles for pedestrians and drivers.",
    "A group of garden gnomes forms a secret society, plotting mischief under the cover of darkness.",
    "Crosswalk signals behave erratically, leading to confusion among pedestrians and drivers alike.",
    "Seagulls take over ice cream trucks, demanding better treats and more beachfront parking.",
    "Potholes seem to appear and disappear mysteriously, leading some to suspect time-traveling shenanigans.",
    "Fire hydrants are spotted dancing in the streets, spraying water and causing chaos.",
    "Tiny unicorns stampede through the city, leaving rainbows and glitter in their wake.",
    "Shopping carts break free from their corrals, forming barricades and causing traffic jams.",
    "A billionaire inventor introduces rocket-powered skateboards, leading to both excitement and chaos.",
    "Traffic cones go on strike, refusing to be moved by city workers.",
    "Giant inflatable rubber chickens invade city parks, delighting and terrifying residents.",
    "Streetlights mysteriously go out, plunging neighborhoods into darkness and confusion.",
    "An unexpected flash mob turns out to be an alien invasion, leading to a dance-off for the fate of humanity.",
    "Kittens escape from a local shelter, forming a stampeding herd in the streets.",
    "Squirrels form a gang, stealing car keys and causing mischief in the neighborhood.",
    "Marshmallow men appear in the city, causing chaos and sticky situations wherever they go.",
    "Garden gnomes stage a rebellion, refusing to stay put in people's yards and causing mischief in the streets.",
    "Late-night subway riders stumble upon a disco party in the underground tunnels, complete with glitter balls and funky music.",
    "Pigeons take over city buses, demanding better accommodations and more bread crumbs.",
    "Garden hoses rebel against their owners, spraying water indiscriminately and causing chaos in the backyard.",
    "Seagulls stage a coup, taking over popular seaside destinations and demanding better snacks.",
    "Mysterious crop circles begin appearing in city parks, sparking rumors of alien visitation.",
    "Shopping carts break free from their confines, careening down streets and causing chaos for drivers and pedestrians.",
    "A giant rubber duck leads a parade through the city streets, followed by a procession of delighted onlookers.",
    "Late-night city officials stumble upon a disco party in the mayor's office, complete with funky beats and disco lights.",
    "Pigeons cause flight delays and chaos at weddings, swooping down to steal rice and confetti.",
    "Squirrels organize a heist to steal picnic baskets from unsuspecting park-goers, leaving chaos in their wake.",
    "Giant inflatable octopuses invade the city, causing chaos and confusion wherever they go.",
    "Runaway garden gnomes are spotted causing mischief in the neighborhood, eluding capture at every turn.",
    "A giant rubber duck leads a protest against the use of duck sauce in local restaurants, demanding better treatment for his feathered friends.",
    "Late-night city officials stumble upon a disco party in city hall, complete with funky beats and flashing lights.",
    "Pigeons take over rooftops, causing chaos and confusion for residents and businesses alike.",
    "Squirrels organize a hijacking of peanut factories, leading to shortages and chaos in the snack aisle.",
    "Giant inflatable penguins invade the city, causing chaos and confusion wherever they go.",
    "Runaway garden hoses are spotted causing chaos in the backyard, spraying water indiscriminately and eluding capture.",
    "A giant rubber duck leads a protest against the use of rubber duckies in bathtubs, demanding better treatment for his brethren.",
    "Late-night city officials stumble upon a disco party in the fire station, complete with funky beats and flashing lights.",
    "Pigeons cause chaos at weddings, swooping down to steal rice and confetti, leaving brides and grooms bewildered.",
    "Squirrels organize a heist to steal picnic baskets from unsuspecting park-goers, leaving chaos in their wake.",
    "Giant inflatable sheep invade the city, causing chaos and confusion wherever they go.",
    "Runaway garden gnomes are spotted causing mischief in the neighborhood, eluding capture at every turn.",
    "A giant rubber duck leads a protest against the use of duckweed in local ponds, demanding better treatment for his fellow waterfowl.",
]

async def get_random_image():
    keywords = ['dogs', 'cats', 'donkeys', 'horse']
    try:
        keyword = random.choice(keywords)
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://source.unsplash.com/random/?{keyword}")
            if response.has_redirect_location:
                image = response.headers.get('location')
                strip_query_args = image.split("?")
                return str(strip_query_args[0])
    except Exception as e:
        print(e)
    

def issue_generator():
    title = random.choice(sample_titles)
    description = random.choice(sample_descriptions)
    yield {"title": title, "description": description}


async def main(number_of_issues: int = 20):
    for x in range(number_of_issues):
        iter_obj = issue_generator()
        issue_ = next(iter_obj)
        issue_image = await get_random_image()
        issue_['image'] = issue_image
        return issue_
        
