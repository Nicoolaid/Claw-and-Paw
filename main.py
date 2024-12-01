from flask import Flask, render_template, request  
import random  
  
app = Flask(__name__)  
  
cat_probabilities = {  
   "Whiskers": 0.2,  
   "Mittens": 0.15,  
   "Fluffy": 0.1,  
   "Snowball": 0.05,  
   "Puddles": 0.02,  
   "Ginger": 0.2,  
   "Simba": 0.15,  
   "Luna": 0.1  
}  
  
  
cat_info = {  
   "Whiskers": {  
      "first_name": "Whiskers",  
      "last_name": "Jenkins",  
      "birthday": "December 25, 2010",  
      "age": 12,  
      "favorite_activities": "Chasing laser pointers, playing with yarn",  
      "species_breed": "Domestic Shorthair",  
      "background_info": "Whiskers was born on Christmas Day and loves to get into the holiday spirit. She's a playful and mischievous cat who loves to chase laser pointers and play with yarn.",  
      "image": "whiskers.jpg"  
   },  
   "Mittens": {  
      "first_name": "Mittens",  
      "last_name": "Blackwood",  
      "birthday": "October 31, 2012",  
      "age": 10,  
      "favorite_activities": "Playing with spiders, chasing ghosts",  
      "species_breed": "Maine Coon",  
      "background_info": "Mittens was born on Halloween and loves all things spooky. She's a brave and adventurous cat who loves to explore the unknown.",  
      "image": "mittens.jpg"  
   },  
   "Fluffy": {  
      "first_name": "Fluffy",  
      "last_name": "Bunnykins",  
      "birthday": "April 1, 2015",  
      "age": 7,  
      "favorite_activities": "Chasing Easter eggs, playing with bunnies",  
      "species_breed": "Ragdoll",  
      "background_info": "Fluffy was born on Easter Sunday and loves all things cute and fluffy. She's a sweet and gentle cat who loves to cuddle and play.",  
      "image": "fluffy.jpg"  
   },  
   "Snowball": {  
      "first_name": "Snowball",  
      "last_name": "Frostbite",  
      "birthday": "January 1, 2018",  
      "age": 4,  
      "favorite_activities": "Playing in the snow, chasing snowflakes",  
      "species_breed": "Siberian",  
      "background_info": "Snowball was born on New Year's Day and loves all things winter. She's a playful and energetic cat who loves to explore the outdoors.",  
      "image": "snowball.jpg"  
   },  
   "Puddles": {  
      "first_name": "Puddles",  
      "last_name": "Lovestruck",  
      "birthday": "February 14, 2020",  
      "age": 2,  
      "favorite_activities": "Playing with hearts, chasing Cupid",  
      "species_breed": "British Shorthair",  
      "background_info": "Puddles was born on Valentine's Day and loves all things love. She's a sweet and affectionate cat who loves to cuddle and play.",  
      "image": "puddles.jpg"  
   },  
   "Ginger": {  
      "first_name": "Ginger",  
      "last_name": "Snap",  
      "birthday": "March 17, 2011",  
      "age": 11,  
      "favorite_activities": "Chasing leprechauns, playing with gold coins",  
      "species_breed": "Orange Tabby",  
      "background_info": "Ginger was born on St. Patrick's Day and loves all things Irish. She's a feisty and playful cat who loves to explore and have fun.",  
      "image": "ginger.jpg"  
   },  
   "Simba": {  
      "first_name": "Simba",  
      "last_name": "Turkeyleg",  
      "birthday": "November 22, 2016",  
      "age": 6,  
      "favorite_activities": "Playing with turkey feathers, chasing pilgrims",  
      "species_breed": "Abyssinian",  
      "background_info": "Simba was born on Thanksgiving Day and loves all things food. She's a curious and adventurous cat who loves to explore and try new things.",  
      "image": "simba.jpg"  
   },  
   "Luna": {  
      "first_name": "Luna",  
      "last_name": "Firework",  
      "birthday": "July 4, 2019",  
      "age": 3,  
      "favorite_activities": "Watching fireworks, playing with sparklers",  
      "species_breed": "Calico",  
      "background_info": "Luna was born on the 4th of July and loves all things patriotic. She's a playful and energetic cat who loves to celebrate and have fun.",  
      "image": "luna.jpg"  
   }  
}  
  
@app.route("/")  
def index():  
   return render_template("index.html")  
  
@app.route("/play", methods=["POST"])  
def play():  

   cat = random.choices(list(cat_probabilities.keys()), weights=cat_probabilities.values())[0]  
   return render_template("play.html", cat=cat, cat_info=cat_info[cat])  
  
if __name__ == "__main__":  
   app.run(debug=True)
