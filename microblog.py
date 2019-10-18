from app import app, db
from app.models import Suggestion

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Suggestion': Suggestion}
