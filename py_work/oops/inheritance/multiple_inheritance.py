class father:

    def cricket_skill(self):

        print("father criket skills")


class mother:

    def cooking_skill(self):

        print("mother cooking skills")


class child (mother,father):

    def learning_skills(self):

        print("child learning skills")


child_instance=child()

child_instance.learning_skills()

child_instance.cooking_skill()

