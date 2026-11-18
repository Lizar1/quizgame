


Data = {
    "Bedroom": {
        "text": "6:30 AM. Today is the TLF CS exam. You are tired and hungry. Your actions:",
        "Actions": [
            ("Get up and have breakfast", "kitchen"),
            ("Sleep 5 more minutes", "overslept")
        ]
    },
    "kitchen": {
        "text": "Coffee and toast. You feel better. You have 20 minutes.",
        "Actions": [
            ("Leave for the bus", "bus_stop"),
            ("Go back to bed for a quick nap", "bedroom")
        ]
    },
    "bus_stop": {
        "text": "The bus arrives. A friend asks: “What is a PCB?”",
        "Actions": [
            ("Explain it to them", "exam"),
            ("Ignore them and miss the bus", "overslept")
        ]
    },
    "exam": {
        "text": "Question 1: “Why must the OS keep processes’ memory separate?”",
        "Actions": [
            ("Answer in simple words", "victory"),
            ("Panic and freeze", "breathe")
        ]
    },
    "breathe": {
        "text": "You take a deep breath. You remember: keep it simple.",
        "Actions": [("Try again", "exam")]
    },
    "victory": "Full marks! You walk out like a legend.",
    "overslept": "You are too late. The exam room door is closed."
}
