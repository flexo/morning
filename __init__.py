from enum import Enum, auto

generic = 1
enquiry = 2
reciprocal = 4

class state(Enum):
    """How-are-you state."""
    # TODO - Might have to reimplement to get eval(state.*) to actually print
    # anything.
    NOT_BAD = auto()
    TIRED = auto()

class __Greeting:
    def __call__(self, what, *who):
        message = []
        if what & reciprocal:
            message.append('hey,')
        if what & generic:
            message.append('morning')
        if who:
            message.append(', '.join(who))
        if what & enquiry:
            message.append('how goes?')
        print(' '.join(message))

    def ugt(self):
        print('morning')

    def __rtruediv__(self, other):
        raise TypeError('I don\'t know what this was supposed to do, sorry!')


greeting = __Greeting()
