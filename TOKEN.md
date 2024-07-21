# Paytory Token
Use tokens to manage Paytory.
> [!WARNING]
> Please note that this option is for developers, only! Don't use it unless you know what are you doing

## Generate Token
### Local
Make sure you have a superuser. Create it using:
```
python manage.py createsuperuser
```
and follow instructions

Next, Go to Django admin at 127.0.0.1:<port>/devoptions and go to `Generate Token`.
It gives you a token. You can use it in APIa.
> [!WARNING]
> Save it somewhere! You won't see it again.

You can use token in API. SEE [APIs.md](https://github.com/MaArasteh/paytory/blob/master/APIs.md). 
