from src.models.settings.connection import db_connection_handler
from src.models.entitities.check_ins import CheckIns
from src.errors.error_types.http_conflict import HttpConflictError
from sqlalchemy.exc import IntegrityError

class CheckInRepository:
    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:
           try:
                check_in = CheckIns(attendeeId = attendee_id)
            
                database.session.add(check_in)
                database.session.commit()
            
                return check_in
            
           except IntegrityError:
               raise HttpConflictError('Check in já cadastrado')
           
           except Exception as exception:
               database.session.rollback()
               raise exception
           