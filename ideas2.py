




# you need to do the class stuff for .error!!!

form = """
<h1>Signup</h1>
    <form method="post">
        <table>
            <tr>
                <td><label for="username">Username</label>
                <td>
                    <input name="username" type="text" value="%(username)s" required>
                    <span class="error">%(username_error)s</span>
                </td>
            </tr>
        </table>
        
