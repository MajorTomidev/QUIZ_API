from rest_framework import serializers
from quiz.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = [
            'question',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    
    class Meta:

        model = Question
        fields = [
            'question',
            'answer',
        ]


class CourseSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    question = serializers.StringRelatedField(many=True)
    
    class Meta:
        
        model = Question
        fields = [
            'question',
            'course',
            'answer',  
        ]

