# AutomaticWhatsappMessage

Python script to send WhatsApp messages.

# Prerequisites
1. Have a Python installation on your computer.
2. Having previously linked your WhatsApp app with WhatsApp Web.

# How to use it

You must run it from a terminal. You can open one pressing
**Windows + R** and writting `cmd`. Go to the script to execute
it and type the following instruction:

~~~
python3 messsage_whatsapp.py [phone number] [message to send] [number of repetitions of the message]
~~~

### Considerations

1. The first argument [phone number] must be written with your phone prefix.
For example, if the telephone number is from Spain, it should have the prefix +34.
Here is a [list of prefixes](https://es.wikipedia.org/wiki/Anexo:Prefijos_telef%C3%B3nicos_mundiales).
You can write the number with whitespaces, the script will handle it, but the correct format is `+34916xxxxxx`.

2. The second argument is a string. You can write it without quotes if it's just one word.
For example
~~~
python3 message_whatsapp.py +34916xxxxxx Hello 1
~~~
With this, we are going to send the message 'Hello' once to the indicated phone number.
If you want to send a longer string with spaces between them, the syntax changes.
You must surround it in quotes so that the Python interpreter does not understand it as arguments.
For example
~~~
python3 message_whatsapp.py +34916xxxxxx "Hello, How are you?" 1
~~~
With this, we are going to send the message 'Hello, How are you?' once to the indicated phone number.

3. The third argument must be a number and specifies the number of times
that the message will be released. If it is not a number the script will return an error.

4. All three arguments must be in the script call, otherwise the script
will return an error writing on the screen how to call the script.
