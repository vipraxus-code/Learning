alien = {"color": "green", "points": 5, "effects": {"constant": ["power"], "temporary": ["poison", "stun"]}}

print(f"You have {len(alien["effects"]["temporary"])} temporary {"effect" if len(alien["effects"]["temporary"]) <= 1 else "effects"}: {', '.join(effect.title() for effect in alien["effects"]["temporary"])}")