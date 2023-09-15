# 2023-07-26 Python Code Dojo

## Running the program
```shell
python main.py
```

## TODOs
Suggested to-dos towards making the game more realistic, and adding expansions

### Gameplay
* [ ] implement the drawing rule of Top-Trumps; when a draw occurs, all cards are added to a pile which is awarded to
the next player to win. Multiple draws may occur in a row
* [ ] make the playing interactive, instead of the 0 player automated 

### User interface
The initial implementation just prints out text to the console. There are different directions and levels of interface
that you could go with
* console
  * using text colours and emojis where useful - this is fairly easy reasonably likely to be done for real software in a
  work/practical environment
  * using a text-based user interface (see [ncurses](https://en.wikipedia.org/wiki/Ncurses) as an example) - this is
  pretty complex and nowadays usually only used in places where web browsers are not available and there is fairly
  complex information or manual use cases
* web - a common way of allowing users to interact with a program. This has a few bits to learn (namely HTML, maybe
JavaScript and CSS) as well as a web framework (I suggest the python flask library) so can take a bit of time, but
should ultimately be rewarding, particularly as it is both practical and can allow anyone to use your app
* native app - usually web apps are preferred nowadays as they work on any machine with an internet connection. These
are normally made to provide offline access to things where possible, blend in more with the existing UI, and potentially
be faster/smoother for users, but in practice web services are generally better and are much simpler to work with. This
would be reasonably complex to do, and you might have to rewrite code to target different operating systems (e.g. iOS,
Android, Windows, ...) but libraries can help abstract away from this. Web apps can be made available like native apps
fairly easily, which is another reason to consider that instead.

### Cards
The initial version only has hardcoded example cards. These are easy to update, but exploring automation and storage
options is a potentially fun and open-ended topic that could take quite a lot of time, so probably best to explore with
small steps.

* 
