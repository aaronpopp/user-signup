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
import cgi

def build_page():
    username_label = "<label>Username:</label>"
    username_input = "<input type='text' name='username'/>"

    password_label = "<label>Password:</label>"
    password_input = "<input type='password' name='password'/>"

    verifypw_label = "<label>Verify password:</label>"
    verifypw_input = "<input type='password' name='verifypw'/>"

    email_label = "<label>Email (optional):</label>"
    email_input = "<input type='text' name='email'/>"

    submit = "<input type = 'submit'/>"

    form = ("<form method = 'post'>" +
            username_label + username_input + "<br>" +
            password_label + password_input + "<br>" +
            verifypw_label + verifypw_input + "<br>" +
            email_label + email_input + "<br>" +
            submit + "</form>")

    header = "<h2>Signup</h2>"

    return header + form


class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page()
        self.response.write(content)

    def post(self):
        # we are filling in these variables with what the user submitted
        # now we have to validate these values and return an error if not valid

        username = self.request.get('username')
        if (" " in username) or (not username) or (username.strip() == ""):
            error1 = "That's not a valid username."
        else:
            error1 = ""

        password = self.request.get('password')
        if (" " in password) or (not password) or (password.strip() == ""):
            error2 = "That's not a valid password."
        else:
            error2 = ""

        verifypw = self.request.get('verifypw')
        if password != verifypw:
            error3 = "Passwords don't match."
        else:
            error3 = ""

        email = self.request.get('email')

        if (error1 == "") and (error2 == "") and (error3 == ""):
            self.redirect("/welcome")
        else:
            content = build_page()
            self.response.write(content + error1 + error2 + error3)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        welcome_greeting = "<h2>Welcome, " + username
        self.response.write(welcome_greeting)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
