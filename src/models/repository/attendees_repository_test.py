import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason= "Novo registro em banco de dados")
def test_insert_ateendee():
    event_id = "meu-uuid-e-nois"
    attendee = {
        "uuid" : "meu-uuid-attendee",
        "name": "meu nome",
        "email": "meu_email@email.com",
        "event_id": event_id
        
    }
    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendee)
    print(response)
    
def test_get_attendee_by_id():
    attendee_id = "meu-uuid-attendee"
    attendee_repository = AttendeesRepository()
    response = attendee_repository.get_attendee_by_id(attendee_id)
    print(response)
    
    
    
