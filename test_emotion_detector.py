import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad this happened")
        self.assertEqualt(result1['dominant_emotion'], 'joy')
        result2 = emotion_detector("I am really mad about this")
        self.assertEqualt(result2['dominant_emotion'], 'anger')
        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqualt(result3['dominant_emotion'], 'disgust')
        result4 = emotion_detector("I am so sad about this")
        self.assertEqualt(result4['dominant_emotion'], 'sadness')
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqualt(result5['dominant_emotion'], 'fear')

unitttest.main()
        
