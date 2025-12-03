voted_users = {
    "james": 12,
    "emily": 30,
    "william": 5,
    "olivia": 22,
    "noah": 7,
    }
must_vote = ["james",
    "ava",
    "george",
    "emily",
    "william",
    "Isabella",
    "noah",
    ]

for name in must_vote:
    if name in voted_users.keys():
        print(f"Thanks for voting, {name.title()}!")
    else:
        print(f"You hasn`t voted yet, {name.title()}!")