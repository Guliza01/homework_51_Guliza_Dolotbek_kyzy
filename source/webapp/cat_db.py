from random import randint

class CatDB:
    def __init__(self):
        self.context = {
            'img': "/static/img/images.jpg",
            'age': 1,
            'happiness': 10,
            'satiety': 40
        }
        self.is_sleeping = False


    def put_to_bed(self):
        self.is_sleeping = True
        self.context['img'] = "/static/img/sleep.jpg"


    def feed_the_cat(self):
        if self.is_sleeping:
            return None
        else:
            if self.context['satiety'] > 100:
                self.context['happiness'] = self.context['happiness']-30
            else:
                self.context['satiety'] = min(self.context['satiety']+15, 100)
                self.context['happiness'] = self.context['happiness']+5
            return self.context


    def play_with_the_cat(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.context['happiness'] = max(self.context['happiness']-5, 0)
            self.context['img'] = "/static/img/sad.png"
        else:
            chance = randint(1,3)
            if chance == 1:
                self.context['img'] = "/static/img/angry.jpg"
                self.context['happiness'] = 0
            else:
                self.context['happiness'] = min(self.context['happiness']+15, 100)
                self.context['img'] = "/static/img/images.jpg"
                self.context['satiety'] = max(self.context['satiety']-10, 0)
        return self.context


catdb = CatDB()