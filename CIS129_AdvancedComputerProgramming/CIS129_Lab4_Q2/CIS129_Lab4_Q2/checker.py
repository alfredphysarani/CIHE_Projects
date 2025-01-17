from collections import Counter

passage = """ Today we live in an era where information is processed almost at the speed of light. Through computers, the technological revolution is drastically changing the way we live and communicate with one another. Terms such as the Internet, which was unfamiliar just a few years ago, are very common today. With the help of computers you can send
letters to, and receive letters from, loved ones within
seconds. You no longer need to send a resume by mail to apply
for a job; in many cases you can simply submit your job
application via the Internet. You can watch how stocks perform
in real time, and instantly buy and sell them. Students
regularly surf the Internet and use computers to design
their classroom projects. They also use powerful word
processing software to complete their term papers. Many
people maintain and balance their checkbooks on computers. """


c = Counter(passage.upper())

print(c)