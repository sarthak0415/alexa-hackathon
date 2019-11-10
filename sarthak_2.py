food = {
    "breakfast": ["eggs"],
    "lunch": ["dal", "roti", "rice", "soup"],
    "snacks": ["samosa"]
}
current_ops = {
    "macro": {
        "name": "Shubham",
        "desk": 192,
        "phone": 74431
    },
    "risk": {
        "name": "Nishan",
        "desk": 131,
        "phone": 74431
    },
    "spyc": {
        "name": "Aneesh",
        "desk": 87,
        "phone": 74431
    },
    "djs": {
        "name": "Kirti",
        "desk": 13,
        "phone": 74431
    },
}

class LunchMenuIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LunchMenuIntent")(handler_input)

    def handle(self, handler_input):
        def flatten(l):
            return [item for sublist in l for item in sublist]
        
        # type: (HandlerInput) -> Response
        food_item = get_slot_value(handler_input, 'FOOD_ITEM')
        food_time = get_slot_value(handler_input, 'FOOD_TIME')
        logger.info(food_item)
        logger.info(food_time)
        speak_output = "Nothing"
        if food_item and food_time:
            if food_item in food[food_time]:
                speak_output = "Yes we have %s in %s today." % (food_item, food_time)
            else:
                speak_output = "No we dont have %s in %s today." % (food_item, food_time)
        elif food_item:
            all_foods = flatten([f for t,f in food.items()])
            if food_item in all_foods:
                food_time_for_food_item = [t for t,f in food.items() if food_item in f][0]
                speak_output = "Yes we have %s in %s today." % (food_item, food_time_for_food_item)
            else:
                speak_output = "No we dont have %s today." % (food_item)
        elif food_time:
            all_foods = ' and '.join(food[food_time])
            speak_output = "We have %s in %s today" %(all_foods, food_time)
        else:
            speak_output = "Sorry I didnt get you!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class CurrentOpsPersonHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CurrentOpsPerson")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        team = get_slot_value(handler_input, 'team').lower()
        speak_output = "%s is currently on ops for %s team, he sits at %s desk number and his phone number is %s" %(
            current_ops[team]["name"], team, current_ops[team]["desk"], current_ops[team]["phone"]
        )

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hey, I can help you with batch failures, ops contacts, inout statuses, book conference rooms, events and cabs. I can also search public information on circuit for you."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


{
    "interactionModel": {
        "languageModel": {
            "invocationName": "change me",
            "intents": [
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": [
                        "What do you do",
                        "How can you help",
                        "what can you do ",
                        "What all can you do",
                        "help"
                    ]
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "HelloWorldIntent",
                    "slots": [],
                    "samples": [
                        "hello",
                        "how are you",
                        "say hi world",
                        "say hi",
                        "hi",
                        "say hello world",
                        "say hello"
                    ]
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                },
                {
                    "name": "LunchMenuIntent",
                    "slots": [
                        {
                            "name": "FOOD_ITEM",
                            "type": "FOOD_ITEM"
                        },
                        {
                            "name": "FOOD_TIME",
                            "type": "FOOD_TIME"
                        }
                    ],
                    "samples": [
                        "what do we have in {FOOD_TIME} today",
                        "is {FOOD_ITEM} in {FOOD_TIME} today",
                        "do we have {FOOD_ITEM} in {FOOD_TIME} today",
                        "do we have {FOOD_ITEM} today",
                        "is there {FOOD_ITEM} in {FOOD_TIME} today"
                    ]
                },
                {
                    "name": "CurrentOpsPerson",
                    "slots": [
                        {
                            "name": "team",
                            "type": "TEAM"
                        }
                    ],
                    "samples": [
                        "who is the current ops person",
                        "who is the current ops person for {team} team"
                    ]
                }
            ],
            "types": [
                {
                    "name": "FOOD_ITEM",
                    "values": [
                        {
                            "name": {
                                "value": "eggs"
                            }
                        },
                        {
                            "name": {
                                "value": "soup"
                            }
                        },
                        {
                            "name": {
                                "value": "rice"
                            }
                        },
                        {
                            "name": {
                                "value": "yello daal"
                            }
                        },
                        {
                            "name": {
                                "value": "roti"
                            }
                        },
                        {
                            "name": {
                                "value": "samosa"
                            }
                        }
                    ]
                },
                {
                    "name": "FOOD_TIME",
                    "values": [
                        {
                            "name": {
                                "value": "snacks"
                            }
                        },
                        {
                            "name": {
                                "value": "breakfast"
                            }
                        },
                        {
                            "name": {
                                "value": "dinner"
                            }
                        },
                        {
                            "name": {
                                "value": "lunch"
                            }
                        }
                    ]
                },
                {
                    "name": "TEAM",
                    "values": [
                        {
                            "name": {
                                "value": "djs"
                            }
                        },
                        {
                            "name": {
                                "value": "spyc"
                            }
                        },
                        {
                            "name": {
                                "value": "risk"
                            }
                        },
                        {
                            "name": {
                                "value": "macro"
                            }
                        }
                    ]
                }
            ]
        },
        "dialog": {
            "intents": [
                {
                    "name": "LunchMenuIntent",
                    "confirmationRequired": false,
                    "prompts": {},
                    "slots": [
                        {
                            "name": "FOOD_ITEM",
                            "type": "FOOD_ITEM",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        },
                        {
                            "name": "FOOD_TIME",
                            "type": "FOOD_TIME",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        }
                    ]
                },
                {
                    "name": "CurrentOpsPerson",
                    "confirmationRequired": false,
                    "prompts": {},
                    "slots": [
                        {
                            "name": "team",
                            "type": "TEAM",
                            "confirmationRequired": false,
                            "elicitationRequired": true,
                            "prompts": {
                                "elicitation": "Elicit.Slot.858999895099.1157390348325"
                            }
                        }
                    ]
                }
            ],
            "delegationStrategy": "ALWAYS"
        },
        "prompts": [
            {
                "id": "Elicit.Slot.1105602038048.830772796984",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "which food item are you talking about"
                    }
                ]
            },
            {
                "id": "Elicit.Slot.858999895099.1157390348325",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "for which team"
                    }
                ]
            }
        ]
    }
}
