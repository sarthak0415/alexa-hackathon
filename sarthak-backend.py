# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
from ask_sdk_core.utils import is_intent_name, get_slot_value
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

rooms = {
    "second": {
        "rainer": {
            "free_slots" : [2,3],
            "positions": "Just besids second floor door. Near desk 54."
        },
        "ediza": {
            "free_slots" : [4,5],
            "positions": "Its next after the pantry. Near desk 210."
        }
            
    },
    "third": {
        "Versivius": {
            "free_slots" : [1],
            "positions": "On the left hand corner of the floor. Near desk 32."
        }
    }
}
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class GetINOUTHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("getInoutIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetINOUTHandler")
        user = get_slot_value(handler_input, 'user')
        speak_output = "Inout status of %s is HYD" % user
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )
    
class getConferenceRoomHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("getConferenceRoom")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In getConferenceRoom")
        floor_no = get_slot_value(handler_input, 'FLOOR_NO')
        
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr["floor_no"] = floor_no
        
        if floor_no in rooms.keys():
            rooms_list = rooms[floor_no].keys()
            if len(rooms_list) > 1:
                speak_output = "There are %s room available on %s floor" % (len(rooms_list), floor_no)
                count = 0
                for room in rooms_list:
                    count += 1
                    if count > 1:
                        speak_output += " and %s" % room    
                    else:
                        speak_output += ", %s" % room
                speak_output += ". Would you like to book any room?"  
        else:
            speak_output = "There is no room available on %s floor" % floor_no
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class getConferenceRoomTImeSlotsHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("getConferenceRoomTImeSlots")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        session_attr = handler_input.attributes_manager.session_attributes
        floor_no = session_attr["floor_no"]
        if floor_no:
            speak_output = "Which room do you want to book? "
            rooms_list = rooms[floor_no].keys()
            count = 0
            for room in rooms_list:
                count += 1
                if count > 1:
                    speak_output += " or %s" % room    
                else:
                    speak_output += ", %s" % room
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

class SetConferenceRoomHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SetConferenceRoom")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        session_attr = handler_input.attributes_manager.session_attributes
        floor_no = session_attr["floor_no"]
        conference_room = get_slot_value(handler_input, 'CONFERENCE_ROOM')
        if floor_no and conference_room:
            session_attr["conference_room"] = conference_room
            speak_output = "%s is available for " % conference_room
            time_list = rooms[floor_no][conference_room]["free_slots"]
            count = 0
            for time in time_list:
                count += 1
                if count > 1:
                    speak_output += " and %s pm" % time    
                else:
                    speak_output += ", %s pm" % time
            speak_output += ". Do you want to book?"
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

class BookConferenceRoomHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("BookConferenceRoom")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        session_attr = handler_input.attributes_manager.session_attributes
        floor_no = session_attr["floor_no"]
        time_slot = get_slot_value(handler_input, 'TIME_SLOT')
        conference_room = session_attr["conference_room"]
        if floor_no and time_slot and conference_room:
            speak_output = "Booked %s for %s. " %(conference_room, time_slot)
            speak_output += "It can be found %s" %rooms[floor_no][conference_room]["positions"]
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .response
            )


class SetINOUTHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("setInoutIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetINOUTHandler")
        user = get_slot_value(handler_input, 'user')
        time = get_slot_value(handler_input, 'time')
        speak_output = "Inout status of %s is set to %s" % (user, time)
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class GetHotlineNumbersHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("GetHotlineNumbers")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetHotlineNumbers")
        hotline_station = get_slot_value(handler_input, 'hotline_station')
        speak_output = "Hotline number for %s is 23974123" % (hotline_station)
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

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
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()
BookConferenceRoomHandler
sb.add_request_handler(GetINOUTHandler())
sb.add_request_handler(getConferenceRoomHandler())
sb.add_request_handler(getConferenceRoomTImeSlotsHandler())
sb.add_request_handler(BookConferenceRoomHandler())
sb.add_request_handler(SetConferenceRoomHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GetHotlineNumbersHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
