from threading import Timer

prompt = "You have 10 seconds to choose the correct answer..."

timeout = 10
t = Timer(timeout, print, ['Sorry, times up'])
t.start()

answer = input(prompt)
t.cancel()