from poloniex import poloniex
import smtplib
from email.mime.text import MIMEText
polo = poloniex('API Key Here','Secret Here')

#openorders = polo.returnOpenOrders("BTC_NAUT")
x = 0
import time
starttime=time.time()
while True:
    balance = polo.returnBalances()
    values = dict((k, v) for k, v in balance.items() if k != 'BTC' and v!= '0.00000000')
    btcvalue = dict((k, v) for k, v in balance.items() if k == 'BTC')
    print(values)
    print(btcvalue.values())
    afterValue = btcvalue.values()
    try:
        beforeValue
    except NameError:
        beforeValue = afterValue
    else:
        print "Proceed"
    #if all coins are on orders
    if bool(values) == False and afterValue == beforeValue:
        x = 0
    #if there is a BUY order that was filled
    elif bool(values) == True and x == 0:
        print "Not Empty"
        gmail_user = 'xxxxxx@gmail.com'
        gmail_password = 'Password Here'

        sent_from = gmail_user
        to = ['xxxxxx@gmail.com']
        subject = 'A Buy Order Was Filled'
        body = 'A Buy Order Was Filled'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            print 'Email sent for Bought!'
            x = 1

        except:
            print 'Something went wrong...'
    elif afterValue > beforeValue :
        print "Not Empty"
        gmail_user = 'xxxxxx@gmail.com'
        gmail_password = 'PAssword Here'

        sent_from = gmail_user
        to = ['xxxxxx@gmail.com']
        subject = 'A Sell Order Was Filled'
        body = 'A Sell Order Was Filled'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            print 'Email sent for Sold!'
            beforeValue = afterValue
        except:
            print 'Something went wrong...'

    #if an email was already sent
    else:
        print 'Wait'
        beforeValue = btcvalue.values()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
