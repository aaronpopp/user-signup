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

#writes the basic form
form = """
<form method = 'post'>
    <h2>Signup</h2>
    <label>Username: <input type='text' name='username'> </label>
    <div style "color: red"> %(unerror)s </div>
    <br>
    <label>Password: <input type='password' name='password'</label>
    <div style "color: red"> %(pwerror)s </div>
    <br>
    <label>Verify password: <input type='password' name='verifypw'></label>
    <div style "color: red"> %(vperror)s </div>
    <br>
    <label>Email (optional): <input type='text' name='email'></label>
    <br>
    <input type = 'submit'>
</form>
"""
# checks to see if user typed something without spaces
def check_username(username):
    if username and (" " not in username) and (username.strip() != ""):
        return username

# checks to see if user typed something without spaces
def check_password(password):
    if password and (" " not in password) and (password.strip() != ""):
        return password

# checks to see if password and verifypw match
def check_verifypw(password, verifypw):
    if password == verifypw:
        return verifypw

# TODO - you still need to figure out valid email function and incorporate it


class MainHandler(webapp2.RequestHandler):
# write_form function takes 3 variables, defaults set to empty strings
    def write_form(self, unerror="", pwerror="", vperror=""):
        self.response.out.write(form % {"unerror": unerror, "pwerror": pwerror, "vperror": vperror})

    def get(self):
        self.write_form()

# takes what the user submitted and runs it through the validity functions
    def post(self):
        good_username = check_username(self.request.get('username'))
        good_password = check_password(self.request.get('password'))
        good_verifypw = check_verifypw(self.request.get('password'),self.request.get('verifypw'))

# WILL THIS WORK? for every one that's not good, we change the variable to house the error message
        if not good_username:
            unerror = "Invalid Username"
        elif not good_password:
            pwerror = "Invalid Password"
        elif not good_verifypw:
            vperror = "Passwords Do Not Match"
            self.write_form(unerror, pwerror, vperror)
        else:
            self.redirect("/welcome")

# need to put the username in the URL somehow
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        welcome_greeting = "<h2>Welcome, " + username
        self.response.write(welcome_greeting)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
