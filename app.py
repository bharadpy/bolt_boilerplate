# Set below as an env variables before starting python app
# export SLACK_SIGNING_SECRET=
# export SLACK_BOT_TOKEN=
# export SLACK_APP_TOKEN=


import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.message(":wave:")
def say_hello(message, say):
    user = message['user']
    say(f"Hi there <@{user}>")


@app.command('/test-slash-ngrok')
def handle_slash_command_test(ack, respond):
    ack()
    t = 'Test asdsadasd'
    respond(t)


@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )


@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
