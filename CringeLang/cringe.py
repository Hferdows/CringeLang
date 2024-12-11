from os.path import dirname, join
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
from twilio.rest import Client
from playsound import playsound
import cv2
import random
import pywhatkit 
from PIL import Image
import time
import psutil


class Cringe:

    global varmap;
    varmap = {}

    def play_bruh_sound(self, times):
        a = 0
        b = True
        
        while(b):
            playsound('Bruh.mp3')
            a+=1
            if(a == times):
                b = False

        response = "Okay 😂"
        return response 
        
    def based_command(self):
        im = Image.open('./DomDabby.png')
        im.show()
        # display image for 10 seconds
        time.sleep(4)
        # hide image
        for proc in psutil.process_iter():
            if proc.name() == "display":
                proc.kill()
        return "You so based Dom Dabby"
    
    def jk(self):
        im = Image.open('./MemeLangImg.png')
        im.show()
        # display image for 10 seconds
        time.sleep(2)
        # hide image
        for proc in psutil.process_iter():
            if proc.name() == "display":
                proc.kill()
        return "Or are you 😈"
    
    def equality(self, var, value):
        varmap.update({var: value})
    
    def var_declaration(self, var, value):
       if value == "ligma":
           varmap.update({var: True})
       elif value == "notLigma":
        varmap.update({var: False})
       else:
           varmap.update({var: value})
       i = value
       var = i
       return var
    
    def send_message(self, number):
        message = self.generate_random_phrase()
        phone_number = (f"+1{number}")
        pywhatkit.sendwhatmsg_instantly(phone_number, message)

    
    def generate_random_phrase(self):
        adjectives = ["trifling", "based", "cooked", "fried", "adorbs", "sus, but cute...", "cooked"]
        nouns = ["baddie", "bad lil vibe","gyatt"]
        verbs = ["mew", "rizzmaxx"]
        phrase1 = ("What do you think will happen if u fall? \nActually on second thought probably nothing cuz I'll catch u everytime")
        phrase3 = ("Hahahahahahhaaahaha. Hey. Hahahahhahahahahahahaha. Boyfriend? 🫣")
        phrase4 = ("You must be a parking ticket because you've got FINE written all over you")
        phrase5 = ("I've GYATT to get your number. \nOops. I guess I'm already texting it?? BRUH")
        phrase6 = "if you were a booger I'd pick you first."

        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        phrase2 = f"Hey, you a {adjective} {noun}, lunch?!"
        phrase7 = f"I'm trynna {verb} you {adjective} {noun}. Pick you up at noon?"
        phrases = [phrase1, phrase2, phrase3, phrase4, phrase5, phrase6] 
        phrase = random.choice(phrases)

        return phrase
    
    def interpret(self, model):
        # model is an instance of Program
        for c in model.commands:
            if c.__class__.__name__ == "BruhCommand":
                print(self.play_bruh_sound(c.times))
            elif c.__class__.__name__ == "BasedCommand":
                print(self.based_command())
            elif c.__class__.__name__ == "JKCommand":
                print(self.jk())
            elif c.__class__.__name__ == "Equality":
                self.equality(c.var, c.varValue)
                print(f"Yes! {c.var} has been set equal to {c.varValue}")
            elif c.__class__.__name__ == "VarDeclaration":
                print(self.var_declaration(c.var, c.varValue))
            elif c.__class__.__name__ == "VarAssign":
                print(self.var_declaration(c.var, c.varValue))
            elif c.__class__.__name__ == "Loop":
                if c.bool != "ligma" or c.bool != "notLigma":
                    if varmap.get(c.bool) != None:
                        while(varmap.get(c.bool)):
                            print("1")
                            c.loopCommands
                    else:
                        print(f"{varmap}")
                        break
                else:
                    while(c.bool):
                        print("1")
                        c.loopCommands
            elif c.__class__.__name__ == "RizzCommand":
                number = input(f"Fine 😜 What's {c.name}'s number?: (10 digit number no spaces or special characters plz \n")
                self.send_message(number)
                print("Yeah. You wouldn't know how to talk to girls would you you CS dweeb")
            else:
                print("Not done")
    
def main(debug=False):

    this_folder = dirname(__file__)

    cringe_mm = metamodel_from_file(join(this_folder, 'cringe.tx'), debug=False)
    metamodel_export(cringe_mm, join(this_folder, 'cringe_meta.dot'))

    cringe_model = cringe_mm.model_from_file(join(this_folder, 'program.crl'))
    model_export(cringe_model, join(this_folder, 'program.dot'))

    cringe = Cringe()
    cringe.interpret(cringe_model)

if __name__ == "__main__":
    main()