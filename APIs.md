# Paytory APIs
Paytory APIs and how to use it.
> [!WARNING]
> This is only for developers. Don't use it unless you know what are you doing.

## How to use it?
First, make sure server is running. Use this command:
```
python manage.py runserver <port: It use 8000 if you leave empty>
```

Open a terminal.

Write the command below:
```
curl --data "token=<your_token>&amount=<amount>&text=<title: what you do. etc: Buying hamburger>" http://127.0.0.1:8000/submit/<expense | income>/
```
> [!NOTE]
> If you're using online, You need to get token. Follow these steps in TOKEN.md
## APIs
/submit/expense/
  POST, returns a JSON.

  input: date (optional), text, amount, user

  output: status: ok

/submit/income/
  POST, returns a JSON

  input: date (optional), text, amount, user

  output: status: ok
