class Kangaroo(object):
    """A Kangaroo Is A Marsupial"""

    def __init__(self, contents=[]):
        """Initialize The Pouch Contents; The Default Value Is An Empty List"""
        self.pouch_contents = contents

    def __str__(self):
        """Return A String Representation Of This Kangaroo And The Contents Of The Pouch, With One Item Per Line"""

        t = [object.__str__(self) + ' with pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)


kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('Wallet')
kanga.put_in_pouch('Car Keys')
kanga.put_in_pouch(roo)

print(kanga)
