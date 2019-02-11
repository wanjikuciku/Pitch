from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    text = TextAreaField('Pitch',validators = [Required()])
    category = SelectField('Category', choices = [('pickup lines', 'Pickup lines'),('interview','Interview'), ('product','Product'),('promotion','Promotion')], validators = [Required()])
    submit = SubmitField('Post')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Update Bio', validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a Comment',validators = [Required()])
    submit = SubmitField('Add Comment')