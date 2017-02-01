# re-do your page layout
# make a header, body (with CSS styling like flicklist)
# and have each line of the input display on its own (with error text at end)

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        Sign Up
    </h1>
"""

page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):

    def get(self):

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
