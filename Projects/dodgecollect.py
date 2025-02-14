#section 1 - setup
import codesters, random
from codesters import StageClass 
stage = StageClass()
stage.disable_all_walls()
player = codesters.Sprite("princess", 0,-160)
stage.set_background("ballroom")
player.set_size(0.4)
object_speed = -1
lives = 5

#section 2 -objects
def falling_object():
    global object_speed,lives
    if lives > 0 :
        x = random.randint(-250,250)
        y = 250
        object = codesters.Sprite("highheels",x,y)
        object.set_y_speed(object_speed)
        object.set_size(0.3)
stage.event_interval(falling_object,7)

#section 3-collision
def collision(player,object):
    global lives
    if object.get_image_name() == "highheels":
        stage.remove_sprite(object)
        lives -=1
        if lives == 0:
            player.say(f"out of lives - you lose!",5)
        else:
            player.say(f"{lives} lives",0.5)
player.event_collision(collision)

#section 4-controls
def go_right():
    player.move_right(10)

player.event_key("right",go_right)

def go_left():
    player.move_left(10)

player.event_key("left",go_left)