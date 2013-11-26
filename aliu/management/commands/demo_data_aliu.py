from django.core.management.base import BaseCommand

from aliu.tests.scenario import (
    default_scenario_aliu,
)
from cms.tests.model_maker import (
    make_section,
    make_simple,
)


def _make_about():
    about = make_section('about')
    make_simple(
        section=about,
        order=0,
        title=(
            "ALIU ACADEMY is an initiative that aims to use technology to "
            "bring rich and world class educational opensource contents "
            "from some of the best institutions in the world to "
            "University communities in Africa such that students can "
            "access the resources in an offline environment at speeds "
            "comparable to high speed broadband in other parts of the "
            "world with high speed internet."
        ),
        description=(
            "Fast internet technologies have not reached most parts of "
            "the world and Africa is not an exception, in fact 65% of the "
            "world have no access to high speed internet connection. But "
            "the world does not wait. Technology keeps pushing beyond to "
            "the limit and there is an exponential spread of knowledge in "
            "what has grown to be known as massive online open courses "
            "(MOOC) where some of the best schools in the world such as "
            "MIT, Harvard, Stanford, Yale, University of Califonia "
            "Berkeley, IIT india, etc offer educational resources for "
            "free mostly real life lecture videos. But to watch these "
            "videos and make any sense of them requires high speed "
            "internet which for now is not totally practicable across "
            "Africa. What should we do? We can't fold our hands and wait "
            "till high speed broadband comes before we tap into these "
            "technologies and join the world in advancement of knowledge! "
            "Hence the motivation to build a platform that will locally "
            "distribute the contents of these resources such that "
            "University communities can have access to these resources at "
            "super fast speed through a wifi based local area network. "
            "Students can access materials on the server from their "
            "mobile devices like android, iphone,ipad and laptops as well "
            "as desktops at a speed that will make them feel they are "
            "truly in the 21st century. We hope to expand and collaborate "
            "more with stakeholders to spread knowledge for free and "
            "light up the continent for present and future generations."
        ),
        moderated=True,
    )


def _make_mandela():
    mandela = make_section('mandela')
    make_simple(
        section=mandela,
        order=0,
        title=(
            "Education is the great engine of personal development. It is "
            "through education that the daughter of a persant can become a "
            "doctor, that a son of a mineworker can become the head of the "
            "mine, that a child of farm workers can become the president of "
            "a great nation. It is what we make out of what we have, not "
            "what we are given, that separates one person from another."
            "(Nelson Mandela)"
        ),
        moderated=True,
    )


def _make_vision():
    vision = make_section('vision')
    make_simple(
        section=vision,
        order=0,
        title=(
            "Our vision at ALIU ACADEMY is to use technology to spread "
            "education across Africa and other parts of the world because "
            "we believe in the words of Nelson Mandela that \"Education is "
            "the most powerful weapon which you can use to change the world. "
            "It is the great engine of personal development. It is through "
            "education that the daughter of a peasant can become a doctor, "
            "that a son of a mineworker can become the head of the mine, "
            "that a child of farm workers can become the president of a "
            "great nation."
        ),
        moderated=True,
    )


class Command(BaseCommand):

    help = "Create demo data for 'aliuacademy_org'"

    def handle(self, *args, **options):
        default_scenario_aliu()
        _make_about()
        _make_mandela()
        _make_vision()
        print("Created 'aliuacademy_org' demo data...")
