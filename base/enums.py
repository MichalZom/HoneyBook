from enum import Enum


class Gender(Enum):
    def __str__(self):
        return str(self.value)

    MALE          = 'male'
    FEMALE        = 'female'


class Preferences(Enum):
    def __str__(self):
        return str(self.value)

    DISCOUNT         = 'promosLabel'
    NEW_STUFF        = 'newnessLabel'
    EXCLUSIVES       = 'lifestyleLabel'
    ASOS_PARTNERS    = 'partnerLabel'
