# Identity Access Management

- Authentication systems - design, implementation, and use of third party services.
- Common vulnerabilities while working with passwords and how to avoid these pitfalls.
- Authorization systems - design and implementation for backend and frontend.
- Basic security best practices and key principals to keep in mind.

## Implement Autho0
https://www.youtube.com/watch?v=Mikr9g_JBaE&t=81s


## Validating Auth Header Formats and Defining Decorator

```python
from flask import Flask, redirect, session, url_for, request, abort
from functools import wraps

app = Flask(__name__)
def requires_auth(f):
    @wraps(f)
    def wrapper( *args, **kwargs):
        jwt = get_token_auth_header()
        return f(jwt, *args, **kwargs)
    return wrapper

def get_token_auth_header():
   ## check if authorization is not in request
    if 'Authorization' not in request.headers:
        abort(401)
    ## get the token   
    auth_header = request.headers['Authorization']
    header_parts = auth_header.split(' ')
    ## check if token is valid
    if len(header_parts) != 2:
        abort(401)
    elif header_parts[0].lower() != 'bearer':
        abort(401) 
    return header_parts[1]
 
@app.route("/header")
@requires_auth
def header(jwt):
    print(jwt)
    return "not implemented"

```

### Sending Tokens from Popular Frontend Frameworks
- [React + Redux - JWT Tutorial](https://jasonwatmore.com/post/2017/12/07/react-redux-jwt-authentication-tutorial-example) There are many ways to include JWTs in requests from frontend frameworks. Jason Watmore has many tutorials for your frontend flavor of choice.
- [Angular Interceptors for Authorization Headers](https://medium.com/@ryanchenkie_40935/angular-authentication-using-the-http-client-and-http-interceptors-2f9d1540eb8)

## Cryptography Python Package
### Installation
    `$pip install cryptography`
### sample
```python
from cryptography.fernet import Fernet

## Define a Key and instantiate a Fernet Instance
key=b'8cozhW9kSi5poZ6TWFuMCV123zg-9NORTs3gJq_J5Do='
f = Fernet(key)

message = input('Enter message you would like encrypt: ')

## Encrypt
ciphertext = f.encrypt(message.encode())
print(f'encrypt: {ciphertext}')

## Decrypt
decryptedtext = f.decrypt(ciphertext)
print(f'decrypt: {decryptedtext}')


```


### Document
- https://cryptography.io/en/latest/




# References

- Oath2: https://oauth.net/2/
- Auth0 Identity Providers: https://auth0.com/docs/authenticate/identity-providers
- Google Identity Platform: https://developers.google.com/identity/
- Magic Links: https://hackernoon.com/magic-links-d680d410f8f7
- iOS Biometrics: https://developer.apple.com/documentation/localauthentication
- Google Authenticator: https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_US&pli=1
- Dance Dance Authentication : https://www.youtube.com/watch?v=VgC4b9K-gYU

Common Auth Services:
- Auth0: https://auth0.com
- AWS Cognito: https://aws.amazon.com/cognito/
- Firebase Auth: https://firebase.google.com/docs/auth
- Okta: https://www.okta.com

- https://pypi.org/project/jwt/

Additional Resources:
- [JWT.io](https://jwt.io/introduction/) a useful guide and list of popular JSON Web Token implementations.
- [Base64](https://en.wikipedia.org/wiki/Base64) Encoding
- [HMAC](https://en.wikipedia.org/wiki/HMAC) keyed-hash message authentication code
