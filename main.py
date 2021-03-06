#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re


#writes the basic form
form = """
<form method = 'post'>
    <h2>Signup</h2>
    <label>Username: </label>
    <input type='text' name='username' value='%(username)s'>
    <label style="color: red"> %(unerror)s </label>
    <br>
    <label>Password: </label>
    <input type='password' name='password'></label>
    <label style="color: red"> %(pwerror)s </label>
    <br>
    <label>Verify password: </label>
    <input type='password' name='verifypw'>
    <label style="color: red"> %(vperror)s </label>
    <br>
    <label>Email (optional): </label>
    <input type='text' name='email' value='%(email)s'>
    <label style="color: red"> %(emailerror)s </label>
    <br>
    <input type = 'submit'>
</form>
"""

# these four functions check user input to confirm that it is valid
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASS_RE.match(password)

def valid_verifypw(password, verifypw):
    if password == verifypw:
        return True

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):

# write_form function takes variables, defaults set to empty strings
    def write_form(self, username="", unerror="", pwerror="", vperror="", email="", emailerror=""):
        values = {
            'username': username,
            'unerror': unerror,
            'pwerror': pwerror,
            'vperror': vperror,
            'email': email,
            'emailerror': emailerror
            }
        response = form % values
        self.response.write(response)

# This is your get function - writes a blank form when page is loaded
    def get(self):
        self.write_form()

# # This is your post function - it takes what the user submitted...
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verifypw = self.request.get('verifypw')
        email = self.request.get('email')
        unerror = ""
        pwerror = ""
        vperror = ""
        emailerror = ""
# ...and runs it through the validity functions
        good_username = valid_username(username)
        good_password = valid_password(password)
        good_verifypw = valid_verifypw(password, verifypw)
        good_email = valid_email(email)

# if the user has submitted good data, we redirect them to the welcome page
        if (good_username and good_password and good_verifypw) and (good_email or not email):
            self.redirect("/welcome?username=%s" % username)

# if not good data, we fill up our error strings to substitute back into the form...
        else:
            if not good_username:
                unerror = "Invalid Username"

            if not good_password:
                pwerror = "Invalid Password"

            if not good_verifypw:
                vperror = "Passwords Do Not Match"

            if not good_email:
                emailerror = "Invalid E-mail Address"
# ...and re-write the form with the error strings
            self.write_form(unerror=unerror, pwerror=pwerror, vperror=vperror, emailerror=emailerror)


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        welcome_greeting = "<h2>Welcome, %s!</h2>" % username
        self.response.write(welcome_greeting)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
