from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class ChannelForm(FlaskForm):
    title = StringField('Channel Name', validators=[DataRequired()])
    server_id = IntegerField('Server ID', validators=[DataRequired()])
