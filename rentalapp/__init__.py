from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy  import SQLAlchemy
from flask_mail import Mail,Message
import config



rent = Flask(__name__,instance_relative_config=True)
csrf = CSRFProtect(rent)
rent.config.from_pyfile("config.py")
rent.config.from_object(config.ProductionConfig)
mail=Mail(rent)
db = SQLAlchemy(rent)


from rentalapp.routes  import user_route,admin_route
from rentalapp import models