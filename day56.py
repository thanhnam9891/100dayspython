import os,time,csv

songlist = {}
artists = []
songs = []

if os.path.exists('day56dir') == False:
    os.makedirs("day56dir")

try:
    with open("100MostStreamedSongs.csv") as file:
        #reader = csv.reader(file)
        songlist = csv.DictReader(file) # Treats the file as a dictionary

        for row in songlist:
            name = row["Artist(s)"]
            song = row["Song"]

            if song not in songs:
                songs.append(song)
                songpath = f"day56dir/{name}/{song}.txt"
                artistpath = f"day56dir{name}"

                if name not in artists:
                    artists.append(name)
                    os.mkdir(os.path.join("day56dir",name))
                    f = open(songpath,"w")
                    f.close()
                else:
                    f = open(songpath,"w")
                    f.close()

    print("Completed")
        
except Exception as errorcode:
    print(errorcode)