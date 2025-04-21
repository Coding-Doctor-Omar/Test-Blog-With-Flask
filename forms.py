from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Length, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

# Create a contact form
class ContactForm(FlaskForm):
    name = StringField(label="Your Name", validators=[DataRequired(), Length(min=3)], render_kw={"style": "width: 60ch", "placeholder": "Name"})
    email = StringField(label="Email", validators=[DataRequired(), Email()], render_kw={"style": "width: 60ch", "placeholder": "Email"})
    telephone = StringField(label="Telephone", validators=[DataRequired()], render_kw={"style": "width: 60ch", "placeholder": "Telephone"})
    message = StringField(label="Message", validators=[DataRequired(), Length(max=1000)], render_kw={"style": "width: 60ch", "placeholder": "Type your message here"})
    send = SubmitField(label="Send")
