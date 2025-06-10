import random

def show_study_nudge():
    nudges = [
        "🧘 Take a 2-minute stretch break!",
        "💧 Drink water and breathe deeply.",
        "🧠 Quick recall: What did you study 10 minutes ago?",
        "📵 Mute distractions for 25 minutes. Focus Mode ON!",
        "🎯 Review a past topic for 2 minutes now."
    ]
    return random.choice(nudges)
