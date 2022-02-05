# TheBirth
## Want to check who's in room C1/2?
We can use def isInC12
The result will tell 
- True mean "in C1/2 
- False mean "isn't in C 1/2

## how many people of only this age are there?
We can use def ***whoOld***
And then we can see the result is the name of a person of that age.
> TheBirth.whoOld(22)

## how many days until my friend's birthday.
We can use ***countdowntobirth***
The result will show how many days until.

you want how many days before Ron's Birthday.
> TheBirth.countdowntobirth("Ron")


## Who's birthday is closest?
We can use ***nearestBirthDay***
Then you will see Who's birthday is closest from now.
> TheBirth.nearestBirthDay

## We have information about a friend's birthday, but  don't know who's birthday.
We can use ***whoBornIn***
The result will show who born in information that you input.
(day, weekday, month, year)
> TheBirth.whoBornIn(day=17,weekday="wed",month="aug",year=2005)

this mean who was born in **Wednesday 17th August 2005**

## how many days this person has been on earth.
We can use ***timeLived***.
Then the result will tell how many days this person has been on earth.
> TheBirth.timeLived("poom")

for example, if today is Poom's 2th Birthday, the function will return 730 (365*2 days)

## how many days this person was born, is it true?
We can use ***checkDate***
Then result will show person who have days that equal input.

for easy, this is swaped input and output of timeLived function. 
Exactly, this function we use this function for calculate in other function. this quite hard and not be able to practical usage
> TheBirth.checkDate(timeLived("poom"))  # the function return "poom"

## find the oldest and youngest person.
We can use ***theOldest***
The result is name of oldest person in our Database.
same idea with ***theYoungest***
> ```TheBirth.theOldest()```

> ```TheBirth.theYoungest()```
## who is in what zodiac sign?
We can use ***isZodiac***
The result will show zodiac of that person.

## who is in this zodiac?
We can use ***whoInZodiac***
The result will show all person who is in this zodiac.


# format of input
- day : (date) integer 1, 2, 3,... , (28, 29, 30, 31)
- weekday : for interger; 1 means monday, 2 means tueday, and goes on. || for string; 3 first letter abbreviation "mon", "tue", "wed", ...
- month : for integer; 1 means January, 2 means February, ... || for string; first letter abbreviation "jan", "tue", "Mar", ...
- year : interger 1998, 2006, 1970
- any string input is accepted for sensitive case (uppercase, lowercase, capitalized)

# developers
- Pear
- Mangkorn
- J
- Kankrai
- Poom
- Mapraw
