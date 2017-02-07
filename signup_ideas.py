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
    <input type = 'submit'>
</form>
"""

class MainHandler(webapp2.RequestHandler):

# write_form function takes variables, defaults set to empty strings
    def write_form(self, username="", unerror=""):
        values = {
            'username': username,
            'unerror': unerror
            # 'pwerror': pwerror,
            # 'vperror': vperror,
            # 'email': email,
            # 'emailerror': emailerror
            }
        response = form % values
        self.response.write(response)

# these four functions check user input to confirm that it is valid
    def check_username(self, username):
        return re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

    # def check_password(self, password):
    #     return re.compile(r"^.{3,20}$")
    #
    # def check_verifypw(self, password, verifypw):
    #     if password == verifypw:
    #         return verifypw
    #
    # def check_email(self, email):
    #     return re.compile(r"^[\S]+@[\S]+.[\S]+$")
    #
    def get(self):
        self.write_form()

# takes what the user submitted...
    def post(self):
        username = self.request.get('username')
        username_is_valid = self.check_username(username)
        # if username_is_valid:
        #     self.redirect('/welcome?username=%s' % username)

        unerror = "Invalid Username"
        self.write_form(username=username, unerror=unerror)
#
#
#
#         username = self.request.get('username')
#         password = self.request.get('password')
#         verifypw = self.request.get('verifypw')
#         email = self.request.get('email')
# # ...and runs it through the validity functions
#         good_username = self.check_username(username)
#         good_password = self.check_password(password)
#         good_verifypw = self.check_verifypw(password, verifypw)
#         good_email = self.check_email(email)

# Like Warren said, when the thing hits (or doesn't hit), it's done with the rest of this branch - figure out
# # how to change this so it goes through all of them
#         if good_username and good_password and good_verifypw and good_email:
#             self.redirect("/welcome?username=%s" % username)
#
#         else:
#             if not good_username:
#                 unerror = "Invalid Username"
            #
            # elif not good_password:
            #     pwerror = "Invalid Password"
            #
            # elif not good_verifypw:
            #     vperror = "Passwords Do Not Match"
                #
                # self.write_form(unerror=unerror)


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        welcome_greeting = "<h2>Welcome, %s!</h2>" % username
        self.response.write(welcome_greeting)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
