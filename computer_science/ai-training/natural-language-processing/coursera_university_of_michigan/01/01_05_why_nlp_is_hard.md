# Why NLP is hard

There can be different interpretations for same sentence, Ex: `Time flies like an arrow.`

* The most obvious meaning is
  * time flies very fast; as fast as an arrow.
* This is a metaphorical interpretation. 
  * Computers are not really good at metaphors.
* Other interpretations:
  * Taking the `like` as verb.
    * Flies like honey -> flies like an arrow -> fruit flies like an arrow
  * Taking the `time` as verb.
    * Take a stopwatch and time the race -> time the flies 

## More Classical Examples / Ambiguous Sentences

* Name of City and Name of Person
  * `Beverly Hills` which is a city, if we teach a computer to recognize it as a `city`, 
   then the computer will probably recognize the next one `Beverly Sills` as a `city`
   but the actual one is a `name` of a `person`.
* Word Order
  * `The box is in the pen` vs `The pen is in the box`. The first one cannot be interpreted directly
    since usually `box(es)` are much larger than `pen`, here the interpretation could be the word `pen`
    may not be referring to a writing instrument, rather than it could be something like which can a place
    where the `box(es)` can be kept, the second one is directly interprerable since here `pen` refers to a writing
    instrument which can fit in the `box`.
* Semantic Representation and Relationship
  * `Mary and Sue are mothers` vs `Mary and Sue are sisters`. The first one talks about both `Mary` and `Sue` are `mothers`
    so from the sentence, there are `two` `mothers` can be interpreted, whereas the second one is similar to first one, 
    but the interpretation talks about the relationship between `Mary` and `Sue` who are `sisters`.
  * `Every American has a mother` vs `Every American has a President`. From the first one it talks about there are as many
    `mothers` as number of(magnitude) `Americans`, but if we just change a word from `mother` to `President`, now the interpretation
    has to be changed to there is only one `President` for every `American`.
  * Who is `they` in `We gave the monkeys the bananas because they were hungry` vs `We gave the monkeys the bananas because they over-ripe`.
    From the first sentence, it is obvious that the word `they` refers to `monkeys` since `bananas` cannot be `hungry`, where as the second
    one the word `they` refers to `bananas`.


Take away : Two sentences may look very similar but when we want to translate them into some semantic representation it cannot be done in straight forward because there are many subtle interactions that come into play.

## Syntax(Grammatic) vs Semantics.

Sentences that are not Syntactically correct they are usually represented by `*` and sentences that are Semantics(meaning) are not proper are done by `?`

* `*` Little a has Mary lamb.
* `?` Colorless green ideas sleep furiously.

The second sentence has 

Subject: `Colorless green ideas`

Verb phrase: `sleep furiously`

But the meaning is not proper, see below

* `Ideas cannot sleep`, because it doesn't fall under the category of entities who has the capacity to sleep.
* `Sleep furiously`, normally we describe `sleep` with peacefully but not `furiously`.
* `Colorless green`, these are contradicting each other.
* `Colorless green ideas`, again `ideas` doesn't the property of having a `color` to it.

## Ambiguous Words

* ball, board, plant
  * meaning - these daily used words do have different meanings in different senses.
* fly, rent, tape
  * parts of speech(POS) - these words not only have different senses, but also has different POS, Ex: `fly` can be a `noun` and it can also be a `verb`

### Other Words

* address
  * The stress can be on either syllable. Compare with transport, effect, outline
* resent
  * As a verb infinitive or as `"re-sent"` a letter
* entrance
  * As a noun or as a verb meaning to put someone in a trance
* number
  * As a noun but also as the comparative of the adjective "numb"

## UnAmbiguous design language

`Lojban` is designed to be `UnAmbiguous`

* Noun-noun phrases: (XY)Z vs. X(YZ)
  * science fiction writer
    * `science fiction` is type of `literature`, where as `science fiction writer` is somebody who writes `science fiction`
  * customer service representative
    * `customer service` is a `unit`, where as `customer service representative` is somone who provides `customer service`.
  * state chess tournament
    * this one is different from the first two, cannot assume first two words are connected as `state` and `chess` whereas here `chess` and `tournament`
      are connected `chess tournament` is a unit and `state chess tournament` is a kind of `chess tournament`.

## NALCO

Problems [Here](http://www.naclo.cs.cmu.edu/)

## Types of Ambiguity

* Morphological
  * Joe is quite impossible. Joe is quite important.
    * `impossible` is morphologically analyzed as `not possible`, but the similar word `important` is not `not portant`, and to add `portant` itself is not a word.
* Phonetic
  * Joe's finger got number.
    * As we seen earlier `number` here should be pronounced as `numer`, here it is referred to as `numb` but rather than the `numbers`, and word `finger` is
      similar to the word `singer` which comes from the word `sing` but the word `finger` doesn't come from `fing` which by itself doesn't exist.
* Parts of Speech(POS)
  * Joe won the first round.
    * The word `round` can be a `verb` or a `noun` or an `adjective`, in this case it is a `noun` because it is preceeded by an `article` and an `adjective`, where as in other contexts it can be different POS.
* Syntactic
  * Call Joe a taxi.
    * Want to hear a cab for `Joe` or want to name `Joe` with the name `taxi`
* Pp(Propositional phase) attachment
  * Joe ate pizza with a fork / with meatballs / with Samantha / with pleasure.
    * `With a fork` here it can relate to `pizza` or `ate`, `pizza` definitely not related to `fork` it is to be related to modify `ate`
    * `with meatballs` which modifies `pizza`
    * `with Samantha` which modifies the `ate`
    * `with pleasure` which modifies the `ate`
* Sense
  * Joe took the bar exam
    * The word `bar` here may refer to legal sense association of lawyers, to be on funny side it can be interpreted as `exam` is been took place where can have drinks.
* Modality
  * Joe may win the lottery.
    * These gives two different worlds where `Joe` wins the `lottery` and other is `Joe` loses the `lottery` so it is referred to two alternative futures.
* Subjectivity
  * Joe believes that stocks will rise.
    * Should not lead you to believe that `stocks will rise` just indicates that `somebody believes` that `stocks will rise`
* Cc (Coordinating Conjunction) attachments - Words like `and`, `or`, `but`
  * Joe likes ripe apples and pears.
    * Here the ambiguity can rise between the `and` conjunction, where it can link just `apples` and `pears` but it can also link `ripe apples` and `pears`.
* Negation
  * Joe likes his pizza with no cheese and tomatoes.
    * Negation starts with word `no` but whether it applies to only `cheese` or it applies to not `cheese` and `tomatoes` is ambiguious.
* Referential
  * Joe yelled at Mike. He had broken the bike.
    * Word interested here it is `he`, does it refer to `Joe` or `Mike` or another person ? We can infer from context that it is referring to `Mike` because there is no reason for `Joe` to `yell` at `Mike`.
  * Joe yelled at Mike. He was angry at him.
    * Here the word `he` refers to `Mike` as opposite to `Joe` from above, since people `yell` when they are `angry` since `Joe` `yelled` at `Mike`, word `he` refers to `Joe`.
* Reflexive
  * `John bought him a present.` vs `John bought himself a present.`
    * What is the word `him` refers here it could not be other person but not `John` since to present to self, normally use `Reflexive` pronoun `himself` as we see in second sentence.
* Ellipsis and parallelism
  * Joe gave Mike a beer and Jeremy a glass of wine.
    * From the above sentence it is missing who gave `Jeremy` the wine, but from `parallelism` it can be inferred that there is someone who is giving here it is `Joe` and someone who is recieving here the first one is `Mike` and the second one is `Jeremy`, so `Joe` gave wine to `Jeremy` as well.
* Metonymy
  * Boston called and left a message for Joe.
    * The word `Boston` here is not used in its literal sense as the city of `Boston` instead the sentence means that the office in `Boston` called or more specifically a person in the office in `Boston` called and after message for Joe. So when word or expression is used to refer to some other expression instead and we have an instance of `Metonymy`.

## Other Sources of Difficulties

* Non-standard, slang, and novel words and usages
  * A360 (Plane Number), 7342.67 (float number), +1-646-555-2223 (Phone Number)
  * "spam" or "friend" as verbs
  * yolo, selfie, chillax – recently recognized as dictionary words
* Inconsistencies
  * junior college, college junior
  * pet spray, pet llama
* Typoes and gramattical erors :)
  * Reciept, John Hopkins, should of
* Parsing problems
  * Cup holder
  * Federal Reserve Board Chairman
* Complex sentences
* Counterfactual sentences (Ex: If you were to do this, then that would happen)
* Implicature/inference/world knowledge: 
  * I was late because my car broke down. 
  * Implies I have a car, I use the car to get to places, the car has wheels, etc.
  * What is not explicitly mentioned, what is world knowledge?
* Semantics vs. pragmatics 
  * Do you know the time?
    * Here the answer could be `yes` or `I do`, but the interlocutor wants to hear the current time now.
* Language is hard even for humans (both L1(Native language for a child) and L2(foreign language))

## Synonyms and Paraphrases

Synonyms refers to words that have similar senses and Paraphrases refers to phrases taht have similar senses.

* The S&P 500 `climbed` 6.93, or 0.56 percent, to 1,243.72, `its best close` since June 12, 2001.
* The Nasdaq `gained` 12.22, or 0.56 percent, to 2,198.44 for `its best showing` since June 8, 2001.
* The DJIA `rose` 68.46, or 0.64 percent, to 10,705.55, `its highest level` since March 15.

The three `words` on `left` are `synonyms` and the three `phrases` on `right` are `paraphrases`

[YouTube Video](https://www.youtube.com/watch?v=NHtohvD7gxY)

Next [Background](01_06_background.md)