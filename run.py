from app.common.db_utils import (
    db_create_models,
    create_categories,
    create_labels
    )
from app import create_app
from dotenv import load_dotenv
import os
load_dotenv()

settings_module = os.getenv("APP_ENV_MODE")
app = create_app(settings_module)

app_context_execution = lambda: (
    # db_create_models(),
    # create_categories(),
    # create_labels(),
    )


if __name__ == '__main__':
    with app.app_context():
        app_context_execution()
    app.run('0.0.0.0')