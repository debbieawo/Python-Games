#Christmas Guess that Song game!!!!
import random
score = 0
num_attempts = 1
print("Welcome to Guess that Song, CHRISTMAS EDITION!!!\n For every lyric, guess the Title or Artist for 5 points each!")

#song dictionaries
rudolph = {"Title": "Rudolph the Red Nose Reindeer", "Lyric": "Had a very shiny nose, And if you ever saw it You would even say it glow", "Artist": "Gene Autry"}
frosty = {"Title": "Frosty the Snowman", "Lyric": "There must have been some magic In that old top hat they found", "Artist": "Gene Autry and Cass County Boys"}
oChristmas = {"Title": "O Christmas Tree", "Lyric": "Each year you bring to us delight with brightly shining Christmas light!", "Artist": "Ernst Anschutz"}
santaClaus = {"Title": "Santa Claus is Coming to Town", "Lyric": "And curly haired dolls that toddle and coo", "Artist": "Frank Sinatra"}
allIWantFor = {"Title": "All I Want for Christmas Is You", "Lyric": "Don't care about the presents underneath the Christmas tree I don't need", "Artist": "Mariah Carey"}

songs = [rudolph, frosty, oChristmas, santaClaus, allIWantFor]
#chosenSong = random.shuffle(songs, 1)[0]

random.shuffle(songs)

for chosenSong in songs:
    for i in range(0, num_attempts):
        songGuess = input("Guess the Title and Artist of the lyric: " + chosenSong["Lyric"])
        songGuess = songGuess.split(",")
        songGuess[0] = songGuess[0].strip()
        songGuess[1] = songGuess[1].strip()
        if songGuess[0] == chosenSong["Title"] and songGuess[1] == chosenSong["Artist"]:
            score += 10
            print("Correct!! You got both right for 10 Points!!!")
        elif songGuess[0] == chosenSong["Title"] or songGuess[1] == chosenSong["Artist"]:
            score += 5
            print("Correct! You got 5 points")
        else:
            print("Incorrect, try Again!")

print(score)
