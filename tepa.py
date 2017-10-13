import tensorflow as tf

# This is Tepa, an emotional chatbot

# Constants that are the cutoff points and other configurations
# for the brain model of Tepa's intelligence and emotions.


# Emotions scale basics definition: 3 segments

# Below gloomy, Tepa will become quiet and withdrawing.
THRESH_GLOOMY = 0.12

# Indifference threshold. If she's happier than this, she doesn't
# interpret others as being rude, when in fact others either
# ARE rude or MIGHT APPEAR rude.
THRESH_INDIFF = 0.45
# If she's happier than this, then she wrongly disses signals
# that would be meant for her; "don't bother me", and others.
# Overhappy Tepa might run arut the friendships. However,
# as friendship count is one thing that affects her moods,
# the over-happy period will not last forever, as the
# friends become ex-friends.
THRESH_BIASED_TO_HAPPY = 0.92

# I want to teach you a little bit of TensorFlow, neural nets,
# the joy of programming in Python, and the magic
# of making artificial "agents" that seem to have a human element
# in them.

# This is Python 3 usage of Tensorflow: We make 'constant'
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
# Always the sess.run will start the Tensorflow's computational engine
print(sess.run(hello))

# Doing arithmetics, the basics of mathematics. Define constant numbers
# to be added. Seems a bit clumsy, but everything has a meaning,
# once you get to know the TensorFlow.
a = tf.constant(10)
b = tf.constant(32)
# Again, we run the Tensorflow computational engine. The kind of
# simple constant and one simple arithmetic '+' addition operation
# will not overheat the CPU, I hope ;-) Still really mild.
print(sess.run(a + b))

# ---------------------------------------------------------------------
# Here on, you can peek into the plans of Tepa's mind.
# She wants to be meticulous and know what others think
# of the things she has collected.
# ---------------------------------------------------------------------

# The 3-way cross-verification of claims, by her (O)
# Cross-verifying data. O wants to know what an outsider 'U' thinks
#   of a clause x, that she (O) has stored.
#   O can either claim (x, O)
#   or           claim (x, K)
#   K = a person. The K might or might not be known by U
#   U can react by 3 ways:
#     => Say outright based on her knowledge and emotions:
#        1. Say outright based on her true knowledge the opinion of claim ()
#        2. Ask more details
#        3. Leave unanswered
def xverf():
    print("OK")
    # The (3) unanswered is interpreted by the filter that O
    # has in emotions, especially the Happy attribute.
    # Being unhappy, and having no answer from K, will
    # downgrade the relationship between K<->O.
    # If happy > THRESH_INDIFF then K<-> is unaffected.

# Plan for the medium intelligent chatbot with rudimentary attribute-based
# emotions
#
# Attributes in chatbot-human interpersonal relationships
#
# W,    wary
# V,    vengeful
# T,    truthful
# H     happy (how easy for a AI, right?-)
#
# Being wary - affects the scope of answers and resolution (accuracy) of
#              answers. rather than outright lie, O answers in a way
#              that has a payoff that veers toward neutrality. So being
#              wary O (one) does not want to
# Vengeful   - having deep hatred towards P
#
# Truthful   - giving out answers that are logically of high truth value
#              in case of uncertainty, also express unequivocally the
#              level of uncertainty.
#
# Trusting   - ingesting information from P and labeling it with trust = 0.9


# Chat agents 'test reality' by spelling out the information to parties
# and validating externally the truth of claims.
#
# How does O know a piece of text is a logical "claim"
#
# Decoding the claim subject, verb and other words.