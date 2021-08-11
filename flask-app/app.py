from flask import Flask, render_template
import random
app = Flask(__name__)

# list of cat images
images = [
    'https://icons.iconarchive.com/icons/iconka/saint-whiskers/256/cat-cupid-love-icon.png',
    'https://icons.iconarchive.com/icons/iconka/saint-whiskers/256/cat-food-hearts-icon.png',
    'https://icons.iconarchive.com/icons/fasticon/cat/256/Cat-Orange-icon.png',
    'https://icons.iconarchive.com/icons/iconcreme/halloween/256/Cat-icon.png',
    'https://icons.iconarchive.com/icons/iconka/meow-2/256/cat-laptop-icon.png',
    'https://icons.iconarchive.com/icons/iconka/meow/256/cat-fish-icon.png'
]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
