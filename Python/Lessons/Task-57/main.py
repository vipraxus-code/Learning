def print_messages(unprinted_messages, printed_messages):
    while unprinted_messages:
        message = unprinted_messages.pop()
        printed_messages.append(message)
        print(f"Message: {message}")

def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        sent_messages.append(unsent_messages.pop())
    print(f"Messages sent: {sent_messages}")

unprinted_messages = ["Some message 1.", "Some message 2.", "Some message 3."]
printed_messages = []
unsent_messages = ["Some message 1.", "Some message 2.", "Some message 3."]
sent_messages = []

print_messages(unprinted_messages[:], printed_messages)
send_messages(unsent_messages[:], sent_messages)
print(unprinted_messages, printed_messages, unsent_messages, sent_messages)