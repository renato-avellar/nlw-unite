import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason= "Novo registro em banco de dados")
def test_insert_event():
    event = {
        "uuid" : "meu-uuid-e-nois2",
        "title": "meu title",
        "slug": "meu_slug_aqui2",
        "maximum_attendees": 20
        
    }
    event_repository = EventsRepository()
    response = event_repository.insert_event(event)
    print(response)
    
@pytest.mark.skip(reason= "idk")    
def test_get_event_by_id():
    event_id = "meu-uuid-e-nois2"
    event_repository = EventsRepository()
    response = event_repository.get_event_by_id(event_id)
    print(response)
    
    
    
