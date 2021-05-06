# biogeochem-cycles-game

This is the repo for my biogeochemical cycles game, which I made as a project for environmental science. This might not be supported after the project due date (4/6/21).

[Game Link](https://replit.com/@RobertFurr/biogeochem-cycles-game?v=1) (Hosted on [replit](https://replit.com))

## Setup instructions

Clone the repo:

```
git clone https://github.com/robtech21/biogeochem-cycles-game
```

Setup the virtualenv:

```
cd biogeochem-cycles-game
mkdir venv
python3 -m venv venv/
cp -r src/lib/gamelib venv/lib/python3.*/site-packages
source venv/bin/activate
pip3 install termcolor
```

Run the game:

```
python3 src/bin/__main__.py
```

If you enounter any bugs, feel free to [email me](mailto:robert@megley.com).
